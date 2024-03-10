# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1107, 580)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"background-color: rgb(30, 31, 34);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_menu_layout = QFrame(self.centralwidget)
        self.top_menu_layout.setObjectName(u"top_menu_layout")
        self.top_menu_layout.setMinimumSize(QSize(0, 26))
        self.top_menu_layout.setMaximumSize(QSize(16777215, 26))
        self.top_menu_layout.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(43, 45, 48);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.top_menu_layout)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.top_menu_layout)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setStyleSheet(u"margin-left: 18px;\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.head_hide = QPushButton(self.top_menu_layout)
        self.head_hide.setObjectName(u"head_hide")
        self.head_hide.setMinimumSize(QSize(26, 26))
        self.head_hide.setMaximumSize(QSize(26, 26))
        self.head_hide.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.head_hide)

        self.head_resize = QPushButton(self.top_menu_layout)
        self.head_resize.setObjectName(u"head_resize")
        self.head_resize.setMinimumSize(QSize(26, 26))
        self.head_resize.setMaximumSize(QSize(26, 26))
        self.head_resize.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 22pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.head_resize)

        self.head_exit = QPushButton(self.top_menu_layout)
        self.head_exit.setObjectName(u"head_exit")
        self.head_exit.setMinimumSize(QSize(26, 26))
        self.head_exit.setMaximumSize(QSize(26, 26))
        self.head_exit.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.head_exit)


        self.verticalLayout.addWidget(self.top_menu_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.left_layout_bar = QFrame(self.centralwidget)
        self.left_layout_bar.setObjectName(u"left_layout_bar")
        self.left_layout_bar.setMinimumSize(QSize(40, 0))
        self.left_layout_bar.setMaximumSize(QSize(40, 16777215))
        self.left_layout_bar.setStyleSheet(u"QFrame#left_layout_bar {\n"
"	background-color: rgb(43, 45, 48);\n"
"	border-top: 2px solid rgb(30, 31, 34);\n"
"	border-right: 2px solid rgb(30, 31, 34);\n"
"	border-bottom: 2px solid rgb(30, 31, 34);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.left_layout_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.left_layout_bar)

        self.WorkLayout = QVBoxLayout()
        self.WorkLayout.setSpacing(0)
        self.WorkLayout.setObjectName(u"WorkLayout")
        self.WorkLayout.setContentsMargins(-1, 0, 1, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ScriptLists = QListView(self.centralwidget)
        self.ScriptLists.setObjectName(u"ScriptLists")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ScriptLists.sizePolicy().hasHeightForWidth())
        self.ScriptLists.setSizePolicy(sizePolicy)
        self.ScriptLists.setMaximumSize(QSize(300, 16777215))
        self.ScriptLists.setStyleSheet(u"QListView#ScriptLists {\n"
"	border: none;\n"
"	background-color: rgb(43, 45, 48);\n"
"	border-top: 2px solid rgb(30, 31, 34);\n"
"	border-bottom: 2px solid rgb(30, 31, 34);\n"
"   }")

        self.horizontalLayout_4.addWidget(self.ScriptLists)

        self.ScriptEditorLayout = QVBoxLayout()
        self.ScriptEditorLayout.setSpacing(0)
        self.ScriptEditorLayout.setObjectName(u"ScriptEditorLayout")
        self.ScriptEditorLayout.setContentsMargins(-1, 0, -1, 1)
        self.ScriptEditorBar_2 = QFrame(self.centralwidget)
        self.ScriptEditorBar_2.setObjectName(u"ScriptEditorBar_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScriptEditorBar_2.sizePolicy().hasHeightForWidth())
        self.ScriptEditorBar_2.setSizePolicy(sizePolicy1)
        self.ScriptEditorBar_2.setMinimumSize(QSize(0, 39))
        self.ScriptEditorBar_2.setMaximumSize(QSize(16777215, 39))
        self.ScriptEditorBar_2.setStyleSheet(u"QFrame#ScriptEditorBar_2 {\n"
"	background-color: rgb(30, 31, 34);\n"
"	border-bottom: 1px solid rgb(57, 59, 64);\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.ScriptEditorBar = QHBoxLayout(self.ScriptEditorBar_2)
        self.ScriptEditorBar.setObjectName(u"ScriptEditorBar")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ScriptEditorBar.addItem(self.horizontalSpacer_2)

        self.ScriptRunButt = QPushButton(self.ScriptEditorBar_2)
        self.ScriptRunButt.setObjectName(u"ScriptRunButt")
        icon = QIcon()
        icon.addFile(u":/ico/assets/Run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ScriptRunButt.setIcon(icon)

        self.ScriptEditorBar.addWidget(self.ScriptRunButt)

        self.ScriptRunRepeatButt = QPushButton(self.ScriptEditorBar_2)
        self.ScriptRunRepeatButt.setObjectName(u"ScriptRunRepeatButt")
        icon1 = QIcon()
        icon1.addFile(u":/ico/assets/RunRepeat.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.ScriptRunRepeatButt.setIcon(icon1)

        self.ScriptEditorBar.addWidget(self.ScriptRunRepeatButt)

        self.horizontalSpacer_3 = QSpacerItem(11, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.ScriptEditorBar.addItem(self.horizontalSpacer_3)


        self.ScriptEditorLayout.addWidget(self.ScriptEditorBar_2)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(11)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(57, 59, 64);\n"
"   }")

        self.ScriptEditorLayout.addWidget(self.textBrowser)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 24))
        self.label_2.setMaximumSize(QSize(16777215, 24))
        self.label_2.setStyleSheet(u"margin-left: 5px;\n"
"color: rgb(157, 160, 168);")

        self.ScriptEditorLayout.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.ScriptEditorLayout)


        self.WorkLayout.addLayout(self.horizontalLayout_4)

        self.TerminalLayout = QVBoxLayout()
        self.TerminalLayout.setSpacing(0)
        self.TerminalLayout.setObjectName(u"TerminalLayout")
        self.horizontalFrame_3 = QFrame(self.centralwidget)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy3)
        self.horizontalFrame_3.setMinimumSize(QSize(0, 0))
        self.horizontalFrame_3.setMaximumSize(QSize(16777215, 34))
        self.horizontalFrame_3.setStyleSheet(u"background-color: rgb(43, 45, 48);")
        self.TerminalFrame_2 = QHBoxLayout(self.horizontalFrame_3)
        self.TerminalFrame_2.setObjectName(u"TerminalFrame_2")

        self.TerminalLayout.addWidget(self.horizontalFrame_3)

        self.TerminalText_2 = QTextBrowser(self.centralwidget)
        self.TerminalText_2.setObjectName(u"TerminalText_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.TerminalText_2.sizePolicy().hasHeightForWidth())
        self.TerminalText_2.setSizePolicy(sizePolicy4)
        self.TerminalText_2.setMaximumSize(QSize(16777215, 806))
        self.TerminalText_2.setStyleSheet(u"QTextBrowser {\n"
"       border: none;\n"
"   }")

        self.TerminalLayout.addWidget(self.TerminalText_2)


        self.WorkLayout.addLayout(self.TerminalLayout)


        self.horizontalLayout.addLayout(self.WorkLayout)

        self.verticalFrame = QFrame(self.centralwidget)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMinimumSize(QSize(40, 0))
        self.verticalFrame.setMaximumSize(QSize(40, 16777215))
        self.verticalFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(43, 45, 48);\n"
"	border-bottom: 2px solid rgb(30, 31, 34);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout.addWidget(self.verticalFrame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 29))
        self.frame_2.setMaximumSize(QSize(16777215, 29))
        self.frame_2.setStyleSheet(u"background-color: rgb(43, 45, 48);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" GInputAI", None))
        self.head_hide.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.head_resize.setText(QCoreApplication.translate("MainWindow", u"\u25ad", None))
        self.head_exit.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.ScriptRunButt.setText("")
        self.ScriptRunRepeatButt.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MainWindow > __profile_dialog", None))
    # retranslateUi

