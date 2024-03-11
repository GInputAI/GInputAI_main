import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QPoint
import sys
from setupUI import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):  # Внимание на изменение структуры инициализации
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.remove_menu_bar()

        self.ui.head_resize.clicked.connect(self.toggle_maximize_restore)
        self.ui.head_hide.clicked.connect(self.showMinimized)
        self.ui.head_exit.clicked.connect(self.close)

    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.is_maximized = False
        else:
            self.showMaximized()
            self.ui.is_maximized = True

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.offset = event.position().toPoint()
        else:
            super().mousePressEvent(event)


    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def remove_menu_bar(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setMouseTracking(True)

        self.minimumHeight = 450
        self.minimumWidth = 600
        self.ui.is_maximized = False

# Секция исполняемого кода исправлена для соответствия синтаксису Python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())