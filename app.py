
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QImage, QPixmap

from MessagesApp import MessageInfo
from ProcessorApp import Processor
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QHeaderView
from Config import BaseConfig, SettingsConfigMenu

from urllib import request
import sys
import os
import configparser

from Dbase.database import *
from background import bg_image
from resources import resources

basedir = os.path.dirname(__file__)

try:
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)

        self.CONFIG_FILE_NAME = os.path.join(basedir, 'config.ini')
        self.setWindowIcon(QtGui.QIcon(os.path.join('icons/icon_app/youtube-icon.png')))
        self.setWindowTitle('ArtVideo')
        self.show()

        # All widgets DownloadVideoFrame

        self.CancelEnterUrl = self.findChild(QtWidgets.QPushButton, 'CancelEnterUrl')
        self.EnterUrlText = self.findChild(QtWidgets.QLineEdit, 'EnterUrlText')
        self.EnterPathSaveLine = self.findChild(QtWidgets.QLineEdit, 'EnterPathSaveLine')
        self.PathSaveButton = self.findChild(QtWidgets.QPushButton, 'PathSaveButton')
        self.DownloadVideoButton = self.findChild(QtWidgets.QPushButton, 'DownloadVideoButton')
        self.ProgressBar = self.findChild(QtWidgets.QProgressBar, 'ProgressBar')
        self.CheckBox = self.findChild(QtWidgets.QCheckBox, 'CheckBox')
        self.CacheTable = self.findChild(QtWidgets.QTableView, 'CacheTable')
        self.CacheButton = self.findChild(QtWidgets.QPushButton, 'CacheButton')

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
        self.CacheButton.clicked.connect(self.clear_cache)

        # All actions app which assign
        self.action_exit.triggered.connect(self.exit)
        self.ExitIcon.triggered.connect(self.exit)
        self.ActionYourPath.triggered.connect(self.load_new_path)
        self.ActionDefault.triggered.connect(self.load_default_path)
        self.CheckBox.clicked.connect(self.convert_auto_audio)

        self.CacheTable.itemSelectionChanged.connect(self.on_selection)
        self.show_cache()
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

        check_url = MessageInfo.message_wrong_enter_url(self, url)
        if check_url and path:
            self.EnterUrlText.setText(check_url)
            self.start_thread = Processor(check_url, path, check_status, type_file)
            self.start_thread.start()
            self.start_thread.info_video.connect(self.show_info)
            self.start_thread.chunks.connect(self.progress)
            self.start_thread.get_cache.connect(self.add_data_db)
            self.start_thread.show_cache.connect(self.show_cache)

            self.EnterPathSaveLine.setText(path)
        else:
            if url == '':
                MessageInfo.message_url(self)

            elif path == '':
                MessageInfo.message_path(self)

    def show_info(self, title: str, description: str, thumbnail: str, type_file: str) -> None:
        self.TitleVideoLine.setText(title)
        self.DescriptionUploadVideo.setText(description)
        self.FileTypeLine.setText(type_file)
        self.EnterUrlText.setText('')

        image = QImage()
        image.loadFromData(request.urlopen(thumbnail).read())
        self.ImageBackground.setPixmap(QPixmap(image))
        self.ImageBackground.show()

    def progress(self, chunks: int) -> None:
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

    def add_data_db(self, title: str, type_file: str) -> None:
        connect = connect_db()
        add_data_db(connect, title=title, type_file=type_file)

    def show_cache(self):
        connect = connect_db()
        data = get_data_db(connect)
        rows = get_count_rows(connect)

        self.CacheTable.setRowCount(0)
        self.CacheTable.setColumnCount(2)
        self.CacheTable.setHorizontalHeaderLabels(['Name file', 'Type file'])
        self.CacheTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        row_index = 0
        for elem in data:
            self.CacheTable.setRowCount(rows)
            col_index = 0
            self.CacheTable.setItem(row_index, col_index, QTableWidgetItem(str(elem['title'])))
            col_index += 1
            self.CacheTable.setItem(row_index, col_index, QTableWidgetItem(str(elem['type_file'])))
            row_index += 1

    def on_selection(self):
        self.CacheTable.setCurrentIndex(QModelIndex())

    def clear_cache(self):
        connect = connect_db()
        data = get_data_db(connect)

        if data:
            clear_all(connect)
            # restart app
            QtCore.QCoreApplication.quit()
            QtCore.QProcess.startDetached(sys.executable, sys.argv)


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == '__main__':
    # subprocess.call('notepad.exe')
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

