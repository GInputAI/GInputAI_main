class Ui_MainWindow(object):
    def toggle_maximize_restore(self):
        if self.is_maximized:
            self.main_window.showNormal()
            self.is_maximized = False
        else:
            self.main_window.showMaximized()
            self.is_maximized = True

    def mouse_press_event(self, event):
        self.start = self.main_window.mapToGlobal(event.pos())

        if event.pos().y() < self.top_menu_layout.height():
            self.pressing_move = True

        if event.pos().x() <= 6:
            self.pressing_side_x, self.pressing_move, self.pressing_resize = 'Left', False, True
        elif event.pos().x() >= self.main_window.width() - 6:
            self.pressing_side_x, self.pressing_move, self.pressing_resize = 'Right', False, True

        if event.pos().y() <= 6:
            self.pressing_side_y, self.pressing_move, self.pressing_resize = 'Top', False, True
        elif event.pos().y() >= self.main_window.height() - 6:
            self.pressing_side_y, self.pressing_move, self.pressing_resize = 'Bottom', False, True

    def mouse_move_event(self, event):
        if self.pressing_resize:
            end = self.main_window.mapToGlobal(event.pos())
            movement = end - self.start
            self.start = end

            if self.pressing_side_x != None:
                if self.pressing_side_x == 'Right':
                    new_width, move_x = max(self.main_window.minimumWidth, event.pos().x()), self.main_window.pos().x()
                else:
                    new_width = max(self.main_window.minimumWidth, self.main_window.width() - movement.x())
                    move_x = self.main_window.pos().x() + movement.x() if self.main_window.minimumWidth < self.main_window.width() - movement.x() else self.main_window.pos().x()
            else:
                new_width, move_x = self.main_window.width(), self.main_window.pos().x()

            if self.pressing_side_y != None:
                if self.pressing_side_y == 'Bottom':
                    new_height, move_y = max(self.main_window.minimumHeight, event.pos().y()), self.main_window.pos().y()
                else:
                    new_height = max(self.main_window.minimumHeight, self.main_window.height() - movement.y())
                    move_y = self.main_window.pos().y() + movement.y() if self.main_window.minimumHeight < self.main_window.height() - movement.y() else self.main_window.pos().y()
            else:
                new_height, move_y = self.main_window.height(), self.main_window.pos().y()

            self.main_window.resize(new_width, new_height)
            self.main_window.move(move_x, move_y)
        elif self.pressing_move:
            end = self.main_window.mapToGlobal(event.pos())
            movement = end - self.start
            self.main_window.move(self.main_window.pos() + movement)
            self.start = end
    def mouse_release_event(self, event):
        self.pressing_move = False
        self.pressing_resize = False
        self.pressing_side_x, self.pressing_side_y, pressing_resize = None, None, False

    def setupUi(self, MainWindow):
        MainWindow.minimumHeight = 450
        MainWindow.minimumWidth = 600
        self.is_maximized = False
        self.main_window = MainWindow
        self.pressing_move = False
        self.pressing_resize = False
        self.pressing_side_x = None
        self.pressing_side_y = None
        self.pressing_side = self.pressing_side_x, self.pressing_side_y

        MainWindow.mousePressEvent = self.mouse_press_event
        MainWindow.mouseMoveEvent = self.mouse_move_event
        MainWindow.mouseReleaseEvent = self.mouse_release_event