import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):

	def loaddata(self):
		produkts = [{"name" : "Д-Р ФРЕШ  OV-пудра ЛИМОН син", "cena" : 0.5, "count" : 4},
		            {"name" : "Д-Р ФРЕШ  Антимухъл ПИСТ. 0.5", "cena" : 1.5, "count" : 2},
		            {"name" : "МАДЕЛ ЗА ПЕТНА SMACCHIOTUTTO Concentrato 400 ml", "cena" : 2, "count" : 1}]
		row = 0
		total = 0
		self.tableWidget.setRowCount(len(produkts))
		for produkt in produkts:
			self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(produkt["name"]))
			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(produkt["cena"])))
			self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(produkt["count"])))
			self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(float((produkt["cena"]) * (produkt["count"])))))
			row = row + 1
			total = total + (float(produkt["cena"]) * float(produkt["count"]))
			self.textBoxTotal.setText(str(total))


	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("form–table.ui", self)
		self.tableWidget.setColumnWidth(0, 180)
		self.tableWidget.setColumnWidth(1, 70)
		self.tableWidget.setColumnWidth(2, 70)
		self.tableWidget.setColumnWidth(3, 70)
		self.loaddata()



app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(741)
widget.setFixedWidth(390)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exit")