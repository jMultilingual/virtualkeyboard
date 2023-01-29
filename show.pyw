from PySide6.QtWidgets import QApplication, QTextEdit,QMainWindow
import sys

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.edit = TextEdit(self)
        self.setCentralWidget(self.edit)


class TextEdit(QTextEdit):

    def __init__(self, window, parent=None):
        super().__init__(parent)

        self._window = window

    def window(self):
        return self._window


def main():

    app = (QApplication([])
           if QApplication.instance() is None
           else
           QApplication.instance())

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
