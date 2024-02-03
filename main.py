import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QTimer

class MemoryGame(QWidget):
    def __init__(self):
        super().__init__()

        self.sequence = []
        self.user_input = ''
        self.sequence_str = ''
        self.level = 1
        self.max_level = 15
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.remember_time)

    def initUI(self):
        self.setWindowTitle('Memory Game')
        self.setGeometry(100, 100, 400, 200)

        self.info_label = QLabel('Press "Start" to begin', self)
        self.error_label = QLabel('', self)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_game)

        self.user_input_field = QLineEdit(self)
        self.user_input_field.setPlaceholderText('Enter the sequence')
        self.user_input_field.setReadOnly(False)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.check_sequence)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        layout.addWidget(self.error_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.user_input_field)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def start_game(self):
        self.sequence = []
        self.user_input = []
        self.level = 1
        self.error_label.clear()
        self.info_label.setText(f'Level {self.level}')
        self.generate_sequence()
        self.display_sequence()

    def generate_sequence(self):
        self.sequence = [random.randint(1, 9) for _ in range(self.level)]
        self.sequence_str = ' '.join(map(str, self.sequence))

    def display_sequence(self):
        self.info_label.setText(self.sequence_str)
        self.user_input_field.clear()
        self.user_input_field.setFocus()
        self.user_input_field.setReadOnly(True)
        self.timer.start(5000 + self.level * 2000)


    def remember_time(self):
        self.user_input_field.setReadOnly(False)
        self.user_input_field.setFocus()
        self.info_label.setText(f'Level {self.level}')
        self.error_label.clear()
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
            self.error_label.clear()
        else:
            self.error_label.setText('Incorrect sequence. Try again.')
            self.user_input_field.clear()
            self.user_input_field.setFocus()
            self.level = 1

    def game_over(self, message):
        QMessageBox.information(self, 'Game Over', message)
        self.info_label.setText('Press "Start" to play again')
        self.submit_button.setEnabled(False)
        self.user_input_field.setReadOnly(True)
        self.user_input_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MemoryGame()
    game.show()
    sys.exit(app.exec_())
