# Importing Libraries
import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

def write_read(x):

    # send command
    arduino.write(x.encode())

    # stime for arduino to respond
    time.sleep(0.9)

    # recieve data and convert to ascii
    data = arduino.readline().decode('ascii')

    return data

while True:

    # taking input from user
    command = input("command > ")

    # send command and receive response
    response = write_read(command)

    # printing the value
    print(response)