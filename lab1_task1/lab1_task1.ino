// -------------------------------------------
//
//  Poject: Lab1_task1
//  Group: 76
//  Students: Adam Dong, Hugo Groene
//  Date: juni 5 2023
//  ------------------------------------------

#define OFF 0
#define ON 1

int val;
String On = "On";
String Off = "Off";
String status = "status";

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
}

// put your main code here
void loop() {
  String str = Serial.readString();  //read until timeout
  str.trim();                        // remove any \r \n whitespace at the end of the String

  if (str == On) {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Led on");

  } else if (str == Off) {
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Led off");

  } else if (str == status) {
    val = digitalRead(LED_BUILTIN);
    if (val == ON) {
      Serial.println("Led is on");
    } else {
      Serial.println("Led is off");
    }

  } else if (str.length() !=  0) {
    Serial.println("unknown command");
  }
}
