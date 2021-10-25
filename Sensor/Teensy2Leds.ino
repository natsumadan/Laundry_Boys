const int red = 10;
const int gre = 9;
const int yel = 6;
String cmd;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(yel, OUTPUT);
  pinMode(gre, OUTPUT);
  Serial1.begin(9600);
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:
  cmd = Serial1.readStringUntil('\n');
  cmd.trim();
  ledsControl();
  
}

void ledsControl(){
    if(cmd.equals("RedLed_ON")){
    digitalWrite(red, HIGH);
  }
  else if(cmd.equals("RedLed_OFF")){
    digitalWrite(red, LOW);
  }
  else if(cmd.equals("YellowLed_ON")){
    digitalWrite(yel, HIGH);
  }
  else if(cmd.equals("YellowLed_OFF")){
    digitalWrite(yel, LOW);
  }
  else if(cmd.equals("GreenLed_ON")){
    digitalWrite(gre, HIGH);
  }
  else if(cmd.equals("GreenLed_OFF")){
    digitalWrite(gre, LOW);
  }
}
