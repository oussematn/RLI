# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("RLI")

		# setting geometry
		self.setGeometry(100, 100, 700, 400)

		# calling method
		self.UiComponents(100,50,30,200,150, 100, 300, 80)
		self.UiComponents(300,50,30,200,350,100,300,80)
		self.UiComponents(500,50,30,200,550,100,300,80)

		# showing all the widgets
		self.show()



	# method for components
	def UiComponents(self,a,b,c,d,e,f,g,h):

		scroll = QScrollBar(self)

		# setting geometry of the scroll bar
		scroll.setGeometry(a, b, c, d)

		# setting range of scroll bar
		scroll.setRange(0, 99)

		# making its background color to green
		scroll.setStyleSheet("background : lightgrey;")

		# creating a label
		label = QLabel("Capteur", self)

		# setting geometry to the label
		label.setGeometry(e,f,g,h)

		# making label multi line
		label.setWordWrap(True)

		# getting value changed signal
		scroll.valueChanged.connect(lambda: do_action())

		# method called when signal is emitted
		def do_action():

			# getting current value
			value = scroll.value()

			# setting text to the label
			label.setText("Current Value : " + str(value))





# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
