from PyQt5.QtWidgets import QWidget
from templates.rules_ui import Ui_Form


class Rules(QWidget, Ui_Form):
    def __init__(self, menu_callback):
        super().__init__()
        self.setupUi(self)
        self.menu_callback = menu_callback

        self.return_btn.clicked.connect(self.return_to_menu)

    def return_to_menu(self):
        self.menu_callback()
