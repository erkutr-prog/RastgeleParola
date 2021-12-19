import random
import string
import sys

from PyQt5.QtWidgets import QMessageBox
from pwdgen import password
from  qtpy import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.options = ["Weak", "Average", "Strong"]


        
        self.input = QtWidgets.QSpinBox()
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(self.options)
        self.check_box = QtWidgets.QCheckBox()
        self.button = QtWidgets.QPushButton("Generate")
        self.password_text = QtWidgets.QLabel()
        
        self.label1 = QtWidgets.QLabel("Length: ")
        self.label2 = QtWidgets.QLabel("Difficulty: ")
        self.label3 = QtWidgets.QLabel("Number: ")


        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addRow(self.label1, self.input)
        self.layout.addRow(self.label2, self.combo)
        self.layout.addRow(self.label3, self.check_box)
        self.layout.addRow(self.button)
        self.layout.addRow(self.password_text)

        self.button.clicked.connect(self.generate_pwd)

    @QtCore.Slot()
    def generate_pwd (self):
        generated_pwd = password(self.input.value(), self.check_box.isChecked(), self.combo.currentText().lower())
        print(generated_pwd)
        self.password_text.setText("Your password: {}".format(generated_pwd))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(500, 100)
    widget.setWindowTitle("Password Generator")
    widget.show()

    sys.exit(app.exec())




