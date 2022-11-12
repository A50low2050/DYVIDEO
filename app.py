
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic.properties import QtCore

from MessagesApp import MessageInfo
from ProcessorApp import Processor
from PyQt5.QtWidgets import QFileDialog
from Config import BaseConfig, SettingsConfigMenu

import requests
import sys
import os
import configparser

from background import bg_image
from resources import resources


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)

        self.CONFIG_FILE_NAME = 'config.ini'
        self.show()

        # All widgets DownloadVideoFrame

        self.CancelEnterUrl = self.findChild(QtWidgets.QPushButton, 'CancelEnterUrl')
        self.EnterUrlText = self.findChild(QtWidgets.QLineEdit, 'EnterUrlText')
        self.EnterPathSaveLine = self.findChild(QtWidgets.QLineEdit, 'EnterPathSaveLine')
        self.PathSaveButton = self.findChild(QtWidgets.QPushButton, 'PathSaveButton')
        self.DownloadVideoButton = self.findChild(QtWidgets.QPushButton, 'DownloadVideoButton')
        self.ProgressBar = self.findChild(QtWidgets.QProgressBar, 'ProgressBar')
        self.CheckBox = self.findChild(QtWidgets.QCheckBox, 'CheckBox')

        # All widgets DescriptionFrame
        self.ImageBackground = self.findChild(QtWidgets.QLabel, 'ImageBackground')
        self.NameVideoText = self.findChild(QtWidgets.QLabel, 'NameVideoText')
        self.TitleVideoLine = self.findChild(QtWidgets.QLineEdit, 'TitleVideoLine')
        self.DescriptionVideoText = self.findChild(QtWidgets.QLabel, 'DescriptionVideoText')
        self.DescriptionUploadVideo = self.findChild(QtWidgets.QTextEdit, 'DescriptionUploadVideo')
        self.FileTypeLine = self.findChild(QtWidgets.QLineEdit, 'FileTypeLine')

        # All widgets action which use app
        self.action_exit = self.findChild(QtWidgets.QAction, 'ActionExit')
        self.ExitIcon = self.findChild(QtWidgets.QAction, 'ExitIcon')
        self.ActionConvertAudio = self.findChild(QtWidgets.QAction, 'ActionConvertAudio')
        self.ActionDefault = self.findChild(QtWidgets.QAction, 'ActionDefault')
        self.ActionYourPath = self.findChild(QtWidgets.QAction, 'ActionYourPath')

        # All connections with methods
        self.CancelEnterUrl.clicked.connect(self.clear_enter_url)
        self.PathSaveButton.clicked.connect(self.choose_directory)
        self.DownloadVideoButton.clicked.connect(self.download)

        # All actions app which assign
        self.action_exit.triggered.connect(self.exit)
        self.ExitIcon.triggered.connect(self.exit)
        self.ActionYourPath.triggered.connect(self.load_new_path)
        self.ActionDefault.triggered.connect(self.load_default_path)
        self.CheckBox.clicked.connect(self.convert_auto_audio)
        # self.ActionConvertAudio.triggered.connect(self.convert_auto_audio)

        self.load_settings()

    def clear_enter_url(self):
        self.EnterUrlText.setText('')

    def choose_directory(self):
        directory = QFileDialog.getExistingDirectory(self, directory='/Локальный диск (C:)', caption='Explorer')
        self.EnterPathSaveLine.setText(directory)

    def download(self):
        path = self.EnterPathSaveLine.text()
        url = self.EnterUrlText.text()
        check_status = self.CheckBox.checkState()
        type_file = BaseConfig().get_type_file()

        if url and path:
            self.start_thread = Processor(url, path, check_status, type_file)
            self.start_thread.start()
            self.start_thread.info_video.connect(self.show_info)
            self.start_thread.chunks.connect(self.progress)

            self.EnterPathSaveLine.setText(path)
            self.EnterUrlText.setText('')
        else:
            if url == '':
                MessageInfo.message_url(self)

            elif path == '':
                MessageInfo.message_path(self)

    def show_info(self, title: str, description: str, thumbnail: str, type_file: str):
        self.TitleVideoLine.setText(title)
        self.DescriptionUploadVideo.setText(description)
        self.FileTypeLine.setText(type_file)

        image = QImage()
        image.loadFromData(requests.get(thumbnail).content)
        self.ImageBackground.setPixmap(QPixmap(image))
        self.ImageBackground.show()

    def progress(self, chunks: int):
        self.ProgressBar.setValue(chunks)

        if self.ProgressBar.value() == 100:
            self.ProgressBar.setValue(0)
            self.TitleVideoLine.setText('')
            self.DescriptionUploadVideo.setText('')
            self.ImageBackground.setPixmap(QPixmap(os.path.join(os.getcwd(), 'background/youtube.jpg')))
            self.FileTypeLine.setText('')

    def exit(self):
        MessageInfo.app_exit(self)

    def load_settings(self):

        config = configparser.ConfigParser()
        config.read('config.ini')

        get_path_status = config.get('SETTINGS_PATH', 'status')
        get_directory = config.get('SETTINGS_PATH', 'directory')

        get_auto_convert_status = config.get('SETTINGS_AUDIO_CONVERT', 'status')

        if get_path_status == 'True':
            self.ActionDefault.setChecked(True)
            self.ActionYourPath.setChecked(False)
            self.EnterPathSaveLine.setText(get_directory)

        else:
            self.ActionDefault.setChecked(False)
            self.ActionYourPath.setChecked(True)
            self.EnterPathSaveLine.setText(get_directory)

        if get_auto_convert_status == 'True':
            self.CheckBox.setChecked(True)
        else:
            self.CheckBox.setChecked(False)

    def load_new_path(self):
        directory = QFileDialog.getExistingDirectory(self, directory='/Локальный диск (C:)', caption='Explorer')
        SettingsConfigMenu.get_user_path(self, directory)
        self.load_settings()

    def load_default_path(self):
        SettingsConfigMenu.get_default_path(self)
        self.load_settings()

    def convert_auto_audio(self):
        status = self.CheckBox.isChecked()
        SettingsConfigMenu.update_status_convert_audio(self, status)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

