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
        self.setWindowTitle('Тренажер для памяти')

        self.setFixedSize(800, 600)

        self.main_menu = MenuWidget()
        self.stacked_widget.addWidget(self.main_menu)

        self.main_menu.training_btn.clicked.connect(lambda: self.switch_widget('training'))
        self.main_menu.challenge_btn.clicked.connect(lambda: self.switch_widget('challenge'))
        self.main_menu.info_btn.clicked.connect(lambda: self.switch_widget('rules'))
        self.main_menu.exit_btn.clicked.connect(self.quit)

    def switch_widget(self, widget_type):
        if widget_type == 'rules':
            self.widget = Rules(self.switch_to_menu)
        elif widget_type == 'training':
            self.widget = Training(self.switch_to_menu)
        elif widget_type == 'challenge':
            self.widget = Challenge(lambda: self.switch_widget('result'))
        else:
            self.widget = Result(self.switch_to_menu)

        self.stacked_widget.addWidget(self.widget)
        self.stacked_widget.setCurrentWidget(self.widget)

    def switch_to_menu(self):
        self.stacked_widget.setCurrentWidget(self.main_menu)

    def quit(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
