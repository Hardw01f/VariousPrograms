void setup() {
  Serial.begin(9600);
  pinMode(8,OUTPUT);
}
 
void loop() {
  Serial.println("HIGH");
  digitalWrite(8,HIGH);
  delay(1000);
  
  Serial.println("LOW");
  digitalWrite(8,LOW);
  delay(1000);
}
