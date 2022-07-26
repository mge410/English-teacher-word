import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.layout import Ui_MainWindow
import sqlite3
import random


name_db = "words.db"


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sqlite_connection = sqlite3.connect(f"database/{name_db}")
        self.cursor = self.sqlite_connection.cursor()

        self.check_button_cliked = False
        self.session_start = False

        self.check.clicked.connect(self.check_run)
        self.next.clicked.connect(self.next_run)
        self.change_session.clicked.connect(self.change_session_run)

    def check_run(self):
        if not self.check_button_cliked and self.session_start:
            self.label.setText(self.label.text() + " - " + str(*self.cursor.execute(f"SELECT translation FROM words WHERE word = ?", (self.label.text(),)).fetchone()))
            self.check_button_cliked = True

    def next_run(self):
        if self.session_start:
            self.label.setText(str(*random.choice(self.session_wods)))
            self.check_button_cliked = False

    def change_session_run(self):
        session = list(map(str, random.choices(range(0, 1000), k=15)))
        self.session_wods = self.cursor.execute(f"SELECT word FROM words WHERE id in ({', '.join(session)})").fetchall()
        self.label.setText(str(*random.choice(self.session_wods)))

        self.session_start = True
        self.check_button_cliked = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
