from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from WidgetsApp import Ui_MainWindow
from MessageApp import MessageInfo
from ProcessorApp import Processor
import sys
import os
import requests


try:
    # Отображает иконку на панели задач
    from PyQt5.QtWinExtras import QtWin
    app_version = u'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(app_version)
except ImportError:
    print('[ERROR] The icon cannot be displayed')

os.environ['NO_PROXY'] = '51shucheng.net'


class App(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(App, self).__init__()

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/YouTube-icon.png'))
        self.setWindowTitle('Youtube Downloader')
        self.ButtonChoosePath.clicked.connect(self.select_directory)
        self.ButtonDownload.clicked.connect(self.download)

        self.actionExit.triggered.connect(self.exit)

    def select_directory(self):
        path = QFileDialog.getExistingDirectory(self, directory='/home', caption='Explorer')
        self.InputShowPath.setText(path)

    def download(self):

        path = self.InputShowPath.text()
        url = self.InputUrl.text()

        if path and url:

            self.start_thread = Processor(url, path)
            self.start_thread.start()
            self.start_thread.chunks.connect(self.progress)
            self.start_thread.info_video.connect(self.show_info)

            self.InputShowPath.setText(path)
            self.InputUrl.setText('')

        else:
            if path == '':
                MessageInfo.message_path(self)

            elif url == '':
                MessageInfo.message_url(self)

    def progress(self, chunks):
        self.progressBar.setValue(chunks)

        if self.progressBar.value() == 100:
            self.progressBar.setValue(0)

            self.TitleVideo.setText('Загрузка видео завершенна')
            self.ShowDescription.setText('')

    def show_info(self, title, description, thumbnails):

        self.TitleVideo.setText(title)
        self.ShowDescription.setText(description)

        image = QImage()
        image.loadFromData(requests.get(thumbnails).content)
        self.photo.setPixmap(QPixmap(image))
        self.photo.show()

    def exit(self):
        MessageInfo.app_exit(self)


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)

# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    start_app()

