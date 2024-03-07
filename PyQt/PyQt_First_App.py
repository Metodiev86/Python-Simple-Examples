import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

def window():
	app = QtWidgets.QApplication(sys.argv)
	win = QtWidgets.QMainWindow()
	win.setGeometry(1200, 300, 500, 500)
	win.setWindowTitle("My First App for PyQt5")
	win.setWindowIcon(QIcon("Seven_Tops.png"))
	win.setToolTip("Това е примерна подсказка")

	label_Name = QtWidgets.QLabel(win)
	label_Name.setText("Въведете своето име: ")
	label_Name.move(50, 50)
	label_Name.setGeometry(50, 50, 150, 20)
	
	label_Lastname = QtWidgets.QLabel(win)
	label_Lastname.setText("Въведете своята фамилия: ")
	label_Lastname.move(50, 70)
	label_Lastname.setGeometry(50, 90, 150, 20)

	txt_Name = QtWidgets.QLineEdit(win)
	txt_Name.move(200, 45)

	txt_Lastname = QtWidgets.QLineEdit(win)
	txt_Lastname.move(200, 85)

	def btn_save_Clicked():
		full_name = txt_Name.text() + " " + txt_Lastname.text()
		print(full_name)

	btn_save = QtWidgets.QPushButton(win)
	btn_save.setText("Save")
	btn_save.move(200, 130)
	btn_save.clicked.connect(btn_save_Clicked)

	win.show()
	sys.exit(app.exec_())


window()
