import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from training_design import Ui_Form


class Training(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sequence = []
        self.user_input = ''
        self.level = 1
        self.max_level = 15
        self.remaining_time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.error_count = 0

        self.start_button.clicked.connect(self.start_game)
        self.user_input_field.returnPressed.connect(self.check_sequence)  # Обработка нажатия Enter

    def start_game(self):
        self.sequence = []
        self.user_input = []
        self.level = 1
        self.timer_label.setText("Осталось")
        self.start_button.hide()

        self.generate_sequence()
        self.display_sequence()
        self.start_button.hide()

    def get_lvl(self):
        if not self.lvl_edit.text() == "":
            try:
                if int(self.lvl_edit.text()) <= 15:
                    self.level = int(self.lvl_edit.text())
            except:
                print('Введенное значени не является числом')
    def generate_sequence(self):
        self.get_lvl()
        self.sequence = [random.randint(1, 9) for _ in range(self.level)]

    def display_sequence(self):
        self.lvl_edit.setText("")
        self.info_label.setText("Запомните последовательность")
        sequence_str = ' '.join(map(str, self.sequence))
        self.seq_label.setText(sequence_str)
        self.user_input_field.clear()
        self.user_input_field.setReadOnly(True)
        self.user_input_field.hide()
        self.timer_label_2.show()
        self.lvl_edit.setPlaceholderText(str(self.level))
        self.error_label.setText(str(self.error_count))
        self.remaining_time = 5 + self.level * 2  # Устанавливаем начальное время
        self.update_timer()  # Обновляем значение таймера
        self.timer.start(1000)  # Запускаем таймер

    def update_timer(self):
        self.remaining_time -= 1
        self.timer_label_2.setText(f'{self.remaining_time} сек')
        if self.remaining_time == 0:
            self.timer.stop()  # Останавливаем таймер, когда время истекло
            self.remember_time()

    def remember_time(self):
        self.user_input_field.setReadOnly(False)
        self.user_input_field.show()
        self.user_input_field.setFocus()
        self.info_label.setText('Введите последовательность')
        self.seq_label.setText("")
        self.timer_label_2.hide()
        self.user_input_field.clear()

    def check_sequence(self):
        user_input = self.user_input_field.text()
        correct_sequence = ''.join(map(str, self.sequence))

        if user_input == correct_sequence:
            self.generate_sequence()
            self.display_sequence()
        else:
            self.error_count += 1




if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Training()
    game.show()
    sys.exit(app.exec_())
