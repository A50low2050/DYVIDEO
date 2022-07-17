
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 800)
        MainWindow.setStyleSheet("#centralwidget {\n"
        "    background-color: rgb(0,0,0);\n"
        "}\n"
        "\n"
        "#menubar {\n"
        "    font-size: 15px;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ButtonDownload = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDownload.setMinimumSize(QtCore.QSize(200, 40))
        self.ButtonDownload.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ButtonDownload.setFont(font)
        self.ButtonDownload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonDownload.setStyleSheet("padding: 10px;\n"
        "border-radius: 5px;\n"
        "outline: none;\n"
        "background-color: aliceblue;")
        self.ButtonDownload.setObjectName("ButtonDownload")
        self.horizontalLayout.addWidget(self.ButtonDownload)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar{\n"
        "    text-align:center;\n"
        "    font-size: 15px;\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    color: rgb(0, 0, 0);\n"
        "    border-radius: 8px;\n"
        "\n"
        "}\n"
        "\n"
        "QProgressBar::chunk{\n"
        "\n"
        "    background-color: rgb(1, 195, 17);\n"
        "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 9, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InputShowPath = QtWidgets.QLineEdit(self.centralwidget)
        self.InputShowPath.setMinimumSize(QtCore.QSize(0, 40))
        self.InputShowPath.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Unicode MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.InputShowPath.setFont(font)
        self.InputShowPath.setStyleSheet("background-color: aliceblue;\n"
        "padding-left: 10px;")
        self.InputShowPath.setText("")
        self.InputShowPath.setMaxLength(100)
        self.InputShowPath.setReadOnly(True)
        self.InputShowPath.setObjectName("InputShowPath")
        self.horizontalLayout_2.addWidget(self.InputShowPath)
        self.ButtonChoosePath = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonChoosePath.setMinimumSize(QtCore.QSize(0, 40))
        self.ButtonChoosePath.setMaximumSize(QtCore.QSize(80, 16777215))
        self.ButtonChoosePath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonChoosePath.setStyleSheet("background-color: aliceblue;")
        self.ButtonChoosePath.setObjectName("ButtonChoosePath")
        self.horizontalLayout_2.addWidget(self.ButtonChoosePath)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem4, 4, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem6, 8, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 2, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.InputUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.InputUrl.setMinimumSize(QtCore.QSize(0, 40))
        self.InputUrl.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InputUrl.setFont(font)
        self.InputUrl.setStyleSheet("padding-left: 10px;\n"
        "border-radius: 15px;\n"
        "outline: none;\n"
        "background-color: aliceblue;")
        self.InputUrl.setText("")
        self.InputUrl.setMaxLength(70)
        self.InputUrl.setObjectName("InputUrl")
        self.gridLayout.addWidget(self.InputUrl, 0, 1, 1, 2)
        self.EnterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EnterLabel.setFont(font)
        self.EnterLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "padding-left:5px;")
        self.EnterLabel.setTextFormat(QtCore.Qt.AutoText)
        self.EnterLabel.setObjectName("EnterLabel")
        self.gridLayout.addWidget(self.EnterLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TitleVideo = QtWidgets.QLabel(self.centralwidget)
        self.TitleVideo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: none;\n"
        "border-radius: 10px;\n"
        "font-size:20px;\n"
        "padding: 15px;\n"
        "text-align: center;")
        self.TitleVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleVideo.setObjectName("TitleVideo")
        self.horizontalLayout_3.addWidget(self.TitleVideo)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setMinimumSize(QtCore.QSize(0, 0))
        self.photo.setMaximumSize(QtCore.QSize(550, 400))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("images/YouTube-image.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.horizontalLayout_4.addWidget(self.photo)
        self.ShowDescription = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ShowDescription.setFont(font)
        self.ShowDescription.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: none;\n"
        "font-size:20px;\n"
        "padding: 15px;\n"
        "cursor: arrow;\n"
        "text-align: center;")
        self.ShowDescription.setFrameShape(QtWidgets.QFrame.Panel)
        self.ShowDescription.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ShowDescription.setReadOnly(True)
        self.ShowDescription.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.ShowDescription.setSearchPaths([])
        self.ShowDescription.setOpenExternalLinks(True)
        self.ShowDescription.setOpenLinks(True)
        self.ShowDescription.setObjectName("ShowDescription")
        self.horizontalLayout_4.addWidget(self.ShowDescription)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 26))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionfont = QtWidgets.QAction(MainWindow)
        self.actionfont.setObjectName("actionfont")
        self.menuSettings.addAction(self.actionExit)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonDownload.setText(_translate("MainWindow", "Скачать"))
        self.InputShowPath.setPlaceholderText(_translate("MainWindow", "Выберите папку сохранения"))
        self.ButtonChoosePath.setText(_translate("MainWindow", "..."))
        self.InputUrl.setPlaceholderText(_translate("MainWindow", "https://www.youtube.com/watch"))
        self.EnterLabel.setText(_translate("MainWindow", "Введите URL видео:"))
        self.TitleVideo.setText(_translate("MainWindow", "Название видео"))
        self.ShowDescription.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20px; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuSettings.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionfont.setText(_translate("MainWindow", "Font"))
        self.actionfont.setShortcut(_translate("MainWindow", "Ctrl+F"))
