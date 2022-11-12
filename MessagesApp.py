from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication


class MessageInfo(object):
    def __init__(self):
        super().__init__()

    def message_path(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowIcon(QIcon('icons/icons_messages/info.png'))
        message.setWindowTitle("No path selected")
        message.setText('Please, choose your path')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

    def message_url(self):
        message = QMessageBox()
        message.setWindowIcon(QIcon('icons/icons_messages/info.png'))
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("Not found url")
        message.setText('Please, enter url')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

    def message_wrong_enter_url(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('Ошибка ввода url')
        message.setText('Неправильный ввод url')
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

    def app_exit(self):
        message = QMessageBox()
        message.setWindowIcon(QIcon('icons/icons_messages/exit.png'))
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle('Exit')
        message.setText('Are you sure you want to get out?')
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        result = message.exec_()

        if result == QMessageBox.Ok:
            QApplication.exit()
