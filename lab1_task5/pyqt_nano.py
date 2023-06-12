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
        x_list = []
        y_list = []
        z_list = []
        for i in range(1,16):
            data = arduino.readline().decode('ascii').split(',')
            x,y,z = data
            x = float(x)
            y = float(y)
            z = float(z.replace("\r\n",""))
            self.ui.MplWidget.canvas.axes.plot(x, i)
            self.ui.MplWidget.canvas.axes.plot(y, i)
            self.ui.MplWidget.canvas.axes.plot(z, i)
            self.ui.MplWidget.canvas.draw()
            print(x,y,z)
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
            time.sleep(1)

        print(x_list)
        print(y_list)
        print(z_list)
        x_axis = list(range(1,16))
        # self.ui.MplWidget.canvas.axes.plot(data[0], data[1])
        # self.ui.MplWidget.canvas.draw()


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())