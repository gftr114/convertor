import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QComboBox

from convert import ConverterLogic

class CurrencyConver(QWidget):
    def __init__(self):
        super().__init__()

        self.logic = ConverterLogic()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Конвертер валют")
        self.resize(400, 150)

        currencies = ['USD', 'EUR', "UAH", "GBR"]

        self.amount_label = QLabel("Сума: ")
        self.amount_input = QLineEdit()

        self.from_currency_label = QLabel("З валюти")
        self.from_currency_combo = QComboBox()
        self.from_currency_combo.addItems(currencies)

        self.to_currency_label = QLabel("У валюту")
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(currencies)

        self.result_label = QLabel("Результат: ")
        self.result_display = QLabel("0.00")

        self.convert_button = QPushButton("Конвертувати")
        self.convert_button.clicked.connect(self.convert_currency)

        layout = QVBoxLayout()
        
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(self.amount_label)
        amount_layout.addWidget(self.amount_input)

        from_currency_layout = QHBoxLayout()
        from_currency_layout.addWidget(self.from_currency_label)
        from_currency_layout.addWidget(self.from_currency_combo)

        to_currency_layout = QHBoxLayout()
        to_currency_layout.addWidget(self.to_currency_label)
        to_currency_layout.addWidget(self.to_currency_combo)

        result_layout = QHBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.result_display)

        layout.addLayout(amount_layout)
        layout.addLayout(from_currency_layout)
        layout.addLayout(to_currency_layout)
        layout.addLayout(result_layout)

        layout.addWidget(self.convert_button)
        self.setLayout(layout)

        self.show()
    
    def create_hbox_layout(self, label, widget):
        hbox = QHBoxLayout()

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_combo.currentText()
            to_currency = self.to_currency_combo.currentText()

            convert_amount = self.logic.convert(amount, from_currency, to_currency)

            self.result_display.setText(f'{convert_amount:2f}')

        except ValueError:
            self.result_display.setText('Bad Input')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CurrencyConver()
    sys.exit(app.exec_())