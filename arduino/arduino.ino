String instruction = "";
String const turn_off_bulb = "bulb off";
String const turn_on_bulb = "bulb on";
String const turn_off_board_led = "led off";
String const turn_on_board_on = "led on";
String const board_status = "status";
int const pin_ampolleta = 8;


void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pin_ampolleta, OUTPUT);
}

void loop() {
  if (Serial.available()>0) {
    instruction = Serial.readStringUntil('\n');

    /* LED */
    if (instruction.equals(turn_on_board_on)) {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(LED_BUILTIN, HIGH);
    } 

    if(instruction.equals(turn_off_board_led)) {
      // turn the LED off by making the voltage LOW
      digitalWrite(LED_BUILTIN, LOW);
    }

    /* BULB */
    if (instruction.equals(turn_on_board_on)) {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(pin_ampolleta, HIGH);
    } 

    if(instruction.equals(turn_on_bulb)) {
      // turn the LED off by making the voltage LOW
      digitalWrite(pin_ampolleta, LOW);
    }


    if(instruction.equals(board_status)) {
      // turn the LED off by making the voltage LOW
      if (digitalRead(LED_BUILTIN)) {
        Serial.write("El led esta encendido");
      } else {
        Serial.write("El led esta apagado");
      }     
      if (digitalRead(pin_ampolleta)) {
        Serial.write("El led esta encendido");
      } else {
        Serial.write("El led esta apagado");
      }  
    }
  }
}