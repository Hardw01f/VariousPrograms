#define LED_PIN 13
#include<stdlib.h>

    void setup() {
        pinMode(LED_PIN, OUTPUT);
        Serial.begin(9600);
    }
    void loop() {
		for(int i=0;i<=5;i++){
			Serial.println("Yhea!!!!!!");
				if(i==5){
				Serial.println("Hello Arduino");
				digitalWrite(LED_PIN, HIGH); delay(100);
				digitalWrite(LED_PIN, LOW);  delay(900);
				system("zsh test.sh");
				}
    }
}
