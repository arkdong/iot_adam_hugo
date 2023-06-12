import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtWidgets import *
from lab1_ui import *

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('arduino_sensors')

        self.ui.pushButton.clicked.connect(self.mybuttonfunction)

        self.x = list(range(0, 100))
        self.y = [0.1, 0.6, 0.8, 0.3, 0.1, 0.1, 0.6, 0.8, 0.3, 0.1, 0.1, 0.6, 0.8, 0.3, 0.1, 0.1, 0.6, 0.8, 0.3, 0.1, 0.1, 0.6, 0.8, 0.3, 0.1, 0.1, 0.6, 0.8, 0.3, 0.1]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_event)
        self.active = False
        self.counter = 0
        self.max_x_value = 5


    def mybuttonfunction(self):

        if (self.active):
            self.timer.stop()
            self.active = False
        else:
            self.timer.start(1000)
            self.active = True

    def timer_event(self):
        self.counter += 1

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(self.x[0 : self.counter], self.y[0 : self.counter], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.draw()

        interval_box = self.ui.spinBox.valueChanged()
        max_x_box = self.ui.spinBox_2.valueChanged()
        if interval_box:
            self.timer.setInterval(interval_box)

        if max_x_box:
            self.max_x_value = max_x_box


if __name__ == "__main__":

    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())