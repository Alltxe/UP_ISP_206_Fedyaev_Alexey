import csv
from PyQt5.QtWidgets import QMainWindow
from templates.rules import Ui_Form


class Rules(QMainWindow, Ui_Form):
    def __init__(self, menu_callback):
        super().__init__()
        self.setupUi(self)
        self.menu_callback = menu_callback

        self.return_btn.clicked.connect(self.return_to_menu)

    def return_to_menu(self):
        self.menu_callback()
