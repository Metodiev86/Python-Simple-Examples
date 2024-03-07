from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.setGeometry(200, 200, 300, 300)
		self.setWindowTitle("Hello")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Proba")
		self.label.move(20, 50)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Click me")
		self.b1.clicked.connect(self.click_UI)
	def click_UI(self):
		self.label.setText("You press the Button")
		self.update()

	def update(self):
		self.label.adjustSize()


def window():
	app = QApplication(sys.argv)
	win = MyWindow()

	win.show()
	sys.exit(app.exec_())

window()

