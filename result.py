import csv
from PyQt5.QtWidgets import QMainWindow
from templates.results import Ui_Form


class Result(QMainWindow, Ui_Form):
    def __init__(self, menu_callback):
        super().__init__()
        self.setupUi(self)
        self.level = 0
        self.max_lvl = 0
        self.menu_callback = menu_callback
        self.get_results()

        self.return_btn.clicked.connect(self.return_to_menu)

        self.passed_lvl.setText(str(self.level))
        self.rec_lvl.setText(str(self.max_lvl))

    def return_to_menu(self):
        self.menu_callback()

    def get_results(self):
        filename = 'results.csv'
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            second_field_values = []

            for row in reader:
                if len(row) > 1:
                    second_field_values.append(row[1])
        self.level = second_field_values[-1]
        self.max_lvl = max(second_field_values)
