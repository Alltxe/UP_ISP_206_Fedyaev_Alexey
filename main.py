import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer

from design import Ui_Form

class MemoryGame(QMainWindow, Ui_Form):
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

    def generate_sequence(self):
        self.sequence = [random.randint(1, 9) for _ in range(self.level)]

    def display_sequence(self):
        self.info_label.setText("Запомните последовательность")
        sequence_str = ' '.join(map(str, self.sequence))
        self.seq_label.setText(sequence_str)
        self.user_input_field.clear()
        self.user_input_field.setReadOnly(True)
        self.user_input_field.hide()
        self.timer_label_2.show()
        self.lvl_label.setText(f'Уровень {self.level}  ')
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
        self.info_label.setText('Введите последовательность')
        self.seq_label.setText("")
        self.timer_label_2.hide()
        self.user_input_field.clear()
    def check_sequence(self):
        user_input = self.user_input_field.text()
        correct_sequence = ''.join(map(str, self.sequence))

        if user_input == correct_sequence:
            self.level += 1
            if self.level > self.max_level:
                self.game_over('Congratulations! You completed all levels!')
            else:
                self.generate_sequence()
                self.display_sequence()
        else:
            self.game_over('Incorrect sequence. Try again.')

    def game_over(self, message):
        QMessageBox.information(self, 'Game Over', message)
        self.info_label.setText('Press "start" to play again')
        self.user_input_field.setReadOnly(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MemoryGame()
    game.show()
    sys.exit(app.exec_())
