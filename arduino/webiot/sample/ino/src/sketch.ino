#include <Servo.h>
// サーボのピン番号
const int SERVO_PIN = 9;
// サーボのインスタンス
Servo servo;
// INITがtrueの時は、モーターの位置を0にするだけ
const bool INIT = true;

void setup(){
    servo.attach(SERVO_PIN);
    servo.write(0);
}

void loop(){
  if (INIT) return;
  servo.write(0);
  delay(2000);
  servo.write(180);
  delay(2000);
  servo.write(90);
  delay(2000);
  servo.writeMicroseconds(1000);
  delay(2000);
  servo.writeMicroseconds(2000);
  delay(2000);
  servo.writeMicroseconds(1500);
  delay(4000);
}
