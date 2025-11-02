# предварительно pip install PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Современный калькулятор")
        self.setFixedSize(320, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #202020;
                color: white;
                font-size: 20px;
                font-family: Arial;
            }
            QLineEdit {
                background-color: #2d2d2d;
                border: none;
                border-radius: 8px;
                padding: 10px;
                color: #00ff99;
            }
            QPushButton {
                background-color: #3a3a3a;
                border: none;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #00b37e;
            }
        """)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # поле ввода
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        # сеточный макет
        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 1, 4)
        ]

        for text, row, col, *span in buttons:
            btn = QPushButton(text)
            if span:
                grid.addWidget(btn, row, col, *span)
            else:
                grid.addWidget(btn, row, col)
            btn.clicked.connect(self.on_button_click)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                expression = self.display.text()
                result = eval(expression)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Ошибка")
        else:
            self.display.setText(self.display.text() + text)

# запускаем приложение
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

