import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from lab1_ui import Ui_MainWindow
import matplotlib
import time
import serial as ser
import statistics
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")
arduino = ser.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)


class MplWidget(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvasQTAgg(Figure())

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
        x_axis = []
        for i in range(1, 16):
            # Read data from the arduinoS
            data = arduino.readline().decode('ascii').split(',')
            x, y, z = data

            # Convert each data from string to float
            x = float(x)
            y = float(y)
            z = float(z.replace("\r\n", ""))

            # Append each data to the list
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
            x_axis.append(i)

            # Plot the graph on MplWidget
            self.ui.MplWidget.canvas.axes.clear()
            self.ui.MplWidget.canvas.axes.set_xlabel("Time in second (s)")
            self.ui.MplWidget.canvas.axes.set_ylabel("Gravitional forces in g")
            self.ui.MplWidget.canvas.axes.plot(x_axis, x_list, color='green',
                                               marker='o', linestyle='solid',
                                               linewidth=2, markersize=12,
                                               label='force in x direction')
            self.ui.MplWidget.canvas.axes.plot(x_axis, y_list, color='red',
                                               marker='o', linestyle='solid',
                                               linewidth=2, markersize=12,
                                               label='force in y direction')
            self.ui.MplWidget.canvas.axes.plot(x_axis, z_list, color='blue',
                                               marker='o', linestyle='solid',
                                               linewidth=2, markersize=12,
                                               label='force in z direction')
            self.ui.MplWidget.canvas.axes.legend(loc='lower right')
            self.ui.MplWidget.canvas.draw()
            self.ui.MplWidget.canvas.flush_events()

            # Sleep for one second
            time.sleep(1)

        # Print the mean on the first left box
        self.print_mean(x_list, y_list, z_list)

        # Print the standard diviation of the second left box
        self.print_stdev(x_list, y_list, z_list)

    # Function that find the mean of the gravitational force in each directions
    def print_mean(self, x, y, z):
        self.ui.mean.clear()
        mean_x = round(statistics.mean(x), 2)
        mean_y = round(statistics.mean(y), 2)
        mean_z = round(statistics.mean(z), 2)
        text = ("Mean of gravitational forces in:\nx-direction: " + str(mean_x)
                + "\ny-direction: " + str(mean_y) + "\nz-direction: "
                + str(mean_z))
        self.ui.mean.append(text)

    # Function that find the standard diviation of the gravitational force in
    # each directions
    def print_stdev(self, x, y, z):
        self.ui.std.clear()
        stdev_x = round(statistics.stdev(x), 2)
        stdev_y = round(statistics.stdev(y), 2)
        stdev_z = round(statistics.stdev(z), 2)
        text = ("Standard diviation of gravitational forces in:\nx-direction: "
                + str(stdev_x) + "\ny-direction: " + str(stdev_y) +
                "\nz-direction: " + str(stdev_z))
        self.ui.std.append(text)


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
