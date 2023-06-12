  // -------------------------------------------
  //
  //  Poject: Lab1_task5
  //  Group: 76
  //  Students: Adam Dong, Hugo Groene
  //  Date: juni 8 2023
  //  ------------------------------------------

  #include <Arduino_LSM6DS3.h>

  float x, y, z;
  char buffer[40];

  // put your setup code here
  void setup() {

    // initialize serial port and wait for port to open:
    Serial.begin(9600);

    // wait for serial port to connect. Needed for native USB port only
    while (!Serial) {}

    if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
    }
  }

  // put your main code here
  void loop() {
    if (IMU.accelerationAvailable()) {
        IMU.readAcceleration(x, y, z);
        // sprintf(buffer, "%d,%d,%d",x,y,z);
        // Serial.println(buffer);
        Serial.print(x);
        Serial.print(',');
        Serial.print(y);
        Serial.print(',');
        Serial.println(z);
    }
  }
