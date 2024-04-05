import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from challenge import Challenge
from training import Training
from templates.main_menu import Ui_Form
from result import Result
from rules import Rules


class MenuWidget(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_menu = MenuWidget()
        self.stacked_widget.addWidget(self.main_menu)

        self.main_menu.training_btn.clicked.connect(self.switch_to_training)
        self.main_menu.challenge_btn.clicked.connect(self.switch_to_challenge)
        self.main_menu.info_btn.clicked.connect(self.switch_to_rules)
        self.main_menu.exit_btn.clicked.connect(self.quit)

    def switch_to_rules(self):
        self.rules_widget = Rules(self.switch_to_menu)
        self.stacked_widget.addWidget(self.rules_widget)
        self.stacked_widget.setCurrentWidget(self.rules_widget)

    def switch_to_training(self):
        self.training_widget = Training(self.switch_to_menu)
        self.stacked_widget.addWidget(self.training_widget)
        self.stacked_widget.setCurrentWidget(self.training_widget)

    def switch_to_challenge(self):
        self.challenge_widget = Challenge(self.switch_to_result)
        self.stacked_widget.addWidget(self.challenge_widget)
        self.stacked_widget.setCurrentWidget(self.challenge_widget)

    def switch_to_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def switch_to_result(self):
        self.result_widget = Result(self.switch_to_menu)
        self.stacked_widget.addWidget(self.result_widget)
        self.stacked_widget.setCurrentWidget(self.result_widget)

    def quit(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
