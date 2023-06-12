import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from lab1_ui import *
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import sched, time
import serial as ser

arduino = ser.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)


class MplWidget(QWidget):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('arduino_sensors')
        self.ui.pushButton.clicked.connect(self.getdata)


    def getdata(self):
        for i in range(15):
            data = arduino.readline().split(',')
            # self.ui.MplWidget.canvas.axes.plot(data[0], data[1])
            # self.ui.MplWidget.canvas.draw()


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())