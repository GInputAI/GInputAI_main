import sys

#pip install PyQt6-QScintilla
from PyQt6.Qsci import QsciScintilla, QsciLexerPython
from PyQt6.QtGui import QColor, QKeyEvent
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QPoint, QObject, QEvent
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSlot

from setupUI import Ui_MainWindow


class KeyPressEater(QObject):
    def eventFilter(self, obj, event):
        # Проверяем, является ли обрабатываемое событие событием нажатия клавиши
        if event.type() == QEvent.Type.KeyPress:
            # Проверяем, была ли нажата клавиша Enter
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                scriptEditor = obj
                line, index = scriptEditor.getCursorPosition()

                # Получаем текст текущей строки
                current_line_text = scriptEditor.text(line).rstrip()

                # Проверяем, заканчивается ли строка на :
                if current_line_text.endswith(':'):
                    scriptEditor.insertAt('\n' + ' ' * (len(current_line_text) - len(
                        current_line_text.lstrip()) + scriptEditor.indentationWidth()), line + 1, 0)
                    # Устанавливаем курсор в добавленный отступ
                    scriptEditor.setCursorPosition(line + 1, len(current_line_text) - len(
                        current_line_text.lstrip()) + scriptEditor.indentationWidth())
                    return True  # Событие обработано, предотвращаем дальнейшую обработку

        # Для всех остальных событий не предотвращаем дальнейшую обработку
        return super().eventFilter(obj, event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.remove_menu_bar()
        self.__script_editor_init()


        self.ui.head_resize.clicked.connect(self.toggle_maximize_restore)
        self.ui.head_hide.clicked.connect(self.showMinimized)
        self.ui.head_exit.clicked.connect(self.close)
    def __script_editor_init(self):
        self.ui.ScriptEditorLayout.removeWidget(self.ui.ScriptEditor)
        self.ui.ScriptEditorLayout.removeWidget(self.ui.ScriptEditorBottom)
        self.ui.ScriptEditor = QsciScintilla(parent=self.ui.centralwidget)
        self.keyPressEater = KeyPressEater()
        self.ui.ScriptEditor.installEventFilter(self.keyPressEater)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.ui.ScriptEditor.sizePolicy().hasHeightForWidth())
        self.ui.ScriptEditor.setSizePolicy(sizePolicy)
        self.ui.ScriptEditor.setObjectName("ScriptEditor")
        self.ui.ScriptEditorLayout.addWidget(self.ui.ScriptEditor)
        self.ui.ScriptEditorLayout.addWidget(self.ui.ScriptEditorBottom)

        lexer = QsciLexerPython()
        self.ui.ScriptEditor.setLexer(lexer)
        # Включение нумерации строк
        self.ui.ScriptEditor.setMarginType(0, QsciScintilla.MarginType.NumberMargin)
        self.ui.ScriptEditor.setMarginWidth(0, "0000")  # Adjust for number of digits
        # Включение автодополнения
        self.ui.ScriptEditor.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)
        self.ui.ScriptEditor.setAutoCompletionCaseSensitivity(True)
        self.ui.ScriptEditor.setAutoCompletionThreshold(1)  # Сколько символов нужно ввести для начала автодополнения
        self.ui.ScriptEditor.setAutoIndent(True)  # Включаем авто-индентацию
        self.ui.ScriptEditor.setIndentationsUseTabs(False)  # Использовать пробелы вместо табов
        self.ui.ScriptEditor.setIndentationWidth(6)  # Ширина отступа: 4 пробела
        self.ui.ScriptEditor.setTabWidth(100)  # Ширина табуляции: 4 пробела
        self.ui.ScriptEditor.setBackspaceUnindents(True)  # Backspace уменьшает уровень отступа
        self.ui.ScriptEditor.setIndentationGuides(True)  # Отображение линий для ориентировки по отступам

        # Подсветка рабочей строки
        self.ui.ScriptEditor.setCaretLineVisible(True)
        self.ui.ScriptEditor.setPaper(QColor(30, 31, 34))
        self.ui.ScriptEditor.setColor(QColor(255, 255, 255))  # Устанавливаем цвет текста на белый для контраста

        # Установка цвета номеров строк
        self.ui.ScriptEditor.setMarginsBackgroundColor(QColor(30, 31, 34))
        self.ui.ScriptEditor.setMarginsForegroundColor(QColor(57, 59, 64))

        # Установка цвета подсветки текущей строки
        self.ui.ScriptEditor.setCaretLineBackgroundColor(QColor(50, 50, 50))  # Чуть светлее, чем фон

        # Настройка цветов лексера
        lexer.setDefaultPaper(QColor(30, 31, 34))  # Фон каждой строки с кодом
        lexer.setDefaultColor(QColor(255, 255, 255))  # Цвет текста по умолчанию

        # Установка шрифта
        font = QtGui.QFont()
        font.setFamily('Monospace')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.ui.ScriptEditor.setFont(font)
        self.ui.ScriptEditor.setMarginsFont(font)
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