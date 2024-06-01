import random
import csv
import os
import datetime
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from templates.challenge import Ui_Form


class Challenge(QWidget, Ui_Form):
    def __init__(self, menu_callback):
        super().__init__()
        self.setupUi(self)
        self.menu_callback = menu_callback
        self.return_btn.clicked.connect(self.save_results)

        self.sequence = []
        self.user_input = ''
        self.level = 1
        self.max_level = 15
        self.remaining_time = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.game_started = False
        self.check_file('results.csv')

        self.start_button.clicked.connect(self.start_game)
        self.user_input_field.returnPressed.connect(self.check_sequence)  # Обработка нажатия Enter

    def check_file(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w', newline='', encoding='utf-8'):
                pass

    def return_to_menu(self):
        if self.game_started:
            self.save_results()
        else:
            self.menu_callback()

    def start_game(self):
        self.game_started = True
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
                self.save_results()
            else:
                self.generate_sequence()
                self.display_sequence()
        else:
            self.save_results()

    def save_results(self):
        current_date = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        filename = 'results.csv'  # Имя файла для сохранения результатов

        # Запись количества пройденных уровней в CSV файл
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            csv.field_size_limit(100)
            writer.writerow([current_date, self.level - 1])

        self.menu_callback()
