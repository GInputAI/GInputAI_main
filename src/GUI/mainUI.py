import sys

#pip install PyQt5 QScintilla
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow
from setupUI import Ui_MainWindow

class MainWindow(QMainWindow):
    def toggle_maximize_restore(self):
        if self.ui.is_maximized:
            self.showNormal()
            self.ui.is_maximized = False
        else:
            self.showMaximized()
            self.ui.is_maximized = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
            super().mousePressEvent(event)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
            super().mousePressEvent(event)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.minimumHeight = 450
        self.minimumWidth = 600
        self.ui.is_maximized = False
        self.ui.main_window = MainWindow
        self.ui.pressing_move = False
        self.ui.pressing_resize = False
        self.ui.pressing_side_x = None
        self.ui.pressing_side_y = None

        MainWindow.mousePressEvent = self.mousePressEvent
        MainWindow.mouseMoveEvent = self.mouseMoveEvent
        MainWindow.mouseReleaseEvent = self.mouseReleaseEvent

        self.ui.head_resize.clicked.connect(self.toggle_maximize_restore)
        self.ui.head_hide.clicked.connect(self.showMinimized)
        self.ui.head_exit.clicked.connect(self.close)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
