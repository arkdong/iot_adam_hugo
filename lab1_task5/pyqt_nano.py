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

arduino = ser.Serial(port='COM5', baudrate=115200, timeout=.1)


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
        self.x = [0,1,1,1,2,3]
        self.y = [0,1,1,1,2,3]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('arduino_sensors')
        self.ui.pushButton.clicked.connect(self.scheduler)



    def measurement(self, scheduler,interval, total):
        if total <= 0:
            return
        data = arduino.readline().split(',')
        self.ui.MplWidget.canvas.axes.plot(data[0], data[1])
        self.ui.MplWidget.canvas.draw()
        total -= 1
        scheduler.enter(interval, 1, self.measurement, (scheduler,interval, total))
        # # recieve data and convert to ascii


        # return data

    def scheduler(self):
        self.ui.MplWidget.canvas.axes.clear()
        my_scheduler = sched.scheduler(time.time, time.sleep)
        my_scheduler.enter(0,1,self.measurement, (my_scheduler,1,15))
        my_scheduler.run

if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())