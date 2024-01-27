from CalculatorApp.model.model_calculator import ModelCalculator

from CalculatorApp.view.main_window import Ui_MainWindow
from PyQt5.QtGui import QDoubleValidator


class ControllerMain(Ui_MainWindow):

    def __init__(self, parent_win):
        self.parent_win = parent_win

        super().__init__(self.parent_win)
        self.setupUi(self.parent_win)

        self.connect_event()

    def connect_event(self):
        self.var1_lineedit.setValidator(QDoubleValidator)
        self.var2_lineedit.setValidator(QDoubleValidator)

        self.plus_button.clicked.connect(self.onclick_plus_button)
        self.minus_button.clicked.connect(self.onclick_minus_button)
        self.multiply_button.clicked.connect(self.onclick_multiply_button)
        self.divide_button.clicked.connect(self.onclick_divide_button)
        self.larger_button.clicked.connect(self.onclick_larger_button)
        self.smaller_button.clicked.connect(self.onclick_smaller_button)

    def onclick_plus_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.plus(var1, var2))

        self.result_lineedit.setText(ans)

    def onclick_minus_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.minus(var1, var2))

        self.result_lineedit.setText(ans)

    def onclick_multiply_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.multiply(var1, var2))

        self.result_lineedit.setText(ans)

    def onclick_divide_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.divide(var1, var2))

        self.result_lineedit.setText(ans)

    def onclick_larger_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.larger(var1, var2))

        self.result_lineedit.setText(ans)

    def onclick_smaller_button(self):
        var1 = float(self.var1_lineedit.text())
        var2 = float(self.var2_lineedit.text())
        ans = str(ModelCalculator.smaller(var1, var2))

        self.result_lineedit.setText(ans)
