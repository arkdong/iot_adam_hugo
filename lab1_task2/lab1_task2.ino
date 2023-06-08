  // -------------------------------------------
  //
  //  Poject: Lab1_task2
  //  Group: 76
  //  Students: Adam Dong, Hugo Groene
  //  Date: juni 5 2023
  //  ------------------------------------------

  #define OFF 0
  #define ON 1
  #include <RTCZero.h>


  RTCZero rtc;

  /* Change these values to set the current initial time */

  const byte seconds = 0;
  const byte minutes = 0;
  const byte hours = 0;
  const byte day = 0;
  const byte month = 0;
  const byte year = 0;
  
  int val;
  String On = "on";
  String Off = "off";
  String status = "status";
  String Blink = "blink";
  String str, lastCommand;

  // put your setup code here
  void setup() {

    // initialize digital pin LED_BUILTIN as an output.
    pinMode(LED_BUILTIN, OUTPUT);

    // initialize serial port and wait for port to open:
    Serial.begin(9600);

    // wait for serial port to connect. Needed for native USB port only
    while (!Serial) {}

    // init digital IO pins
    digitalWrite(LED_BUILTIN, LOW);

    rtc.begin();

    // Set the time
    rtc.setHours(hours);
    rtc.setMinutes(minutes);
    rtc.setSeconds(seconds);

    // Set the date
    rtc.setDay(day);
    rtc.setMonth(month);
    rtc.setYear(year);
  }


  // put your main code here
  void loop() {
    str = Serial.readString();  //read until timeout
    str.trim();                 // remove any \r \n whitespace at the end of the String

    if (str == On) {
      lastCommand = On;
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED on");

    } else if (str == Off) {
      lastCommand = Off;
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED off");

    } else if (str == status) {
      if (lastCommand != Blink) {
        lastCommand = status;
        val = digitalRead(LED_BUILTIN);
        if (val == ON) {
          Serial.println("LED on");
        } else {
          Serial.println("LED off");
        }
      } else {
        Serial.println("LED blink");
      }

    } else if (str == Blink || lastCommand == Blink) {
      int x = rtc.getSeconds() % 2;
      if (x == 0) {
        digitalWrite(LED_BUILTIN, LOW);
      } else {
        digitalWrite(LED_BUILTIN, HIGH);
      }
      if (str == Blink) {
        Serial.println("LED blink");
      }
      lastCommand =   Blink;
  
    } else if(str.length() != 0){
      Serial.println("unknown command");
    }
  }
