import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from challenge import Challenge
from training import Training
from templates.main_ui import Ui_Form
from result import Result
from rules import Rules


class MenuWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Тренажер для памяти')
        self.resize(800, 600)  # Установка начального размера окна

        # Создание главного виджета и установка его как центрального
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Создание вертикального макета
        self.layout = QVBoxLayout(main_widget)

        # Создание QStackedWidget и добавление его в основной макет
        self.stacked_widget = QStackedWidget()
        self.layout.addWidget(self.stacked_widget)

        # Инициализация основного меню
        self.main_menu = MenuWidget()
        self.stacked_widget.addWidget(self.main_menu)

        # Подключение кнопок основного меню к соответствующим методам
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
