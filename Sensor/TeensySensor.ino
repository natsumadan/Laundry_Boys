#include <Wire.h>
#include "DHT.h"
const int photoResistor = 19 ; // input the pin that the photoresistor connect to here
const int dlt = 1000 ;
const int windSensor = 20; // input the delay time here to control how often it measure data
#define rxPin 7             //receiving serial data
#define txPin 8             //transmitting serial data
#define DHTPIN 21           // define DHT sensor pin
#define DHTTYPE 11
DHT dht(DHTPIN, DHTTYPE);
float windspeed = 0.00;

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(photoResistor, INPUT);
    pinMode(DHTPIN, INPUT);
    dht.begin();
    Serial1.begin(9600);
    delay(1000);
}

void loop()
{
    // put your main code here, to run repeatedly:
    delay(dlt);
    dataRead();
    Serial.println("");
    Serial1.println("");
}

void dataRead()
{

    // Measure humidity and temperature, print in terminal and send via bluetooth
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    float f = dht.readTemperature(true);

    float hif = dht.computeHeatIndex(f, h);
    float hic = dht.computeHeatIndex(t, h, false);

    Serial.print(F(" Humidity: "));
    Serial.print(h);
    Serial.print(F("%  Temperature: "));
    Serial.print(t);
    Serial.print(F("C "));
    Serial.print(f);
    Serial.print(F("F  Heat index: "));
    Serial.print(hic);
    Serial.print(F("C "));
    Serial.print(hif);
    Serial.print(F("F "));

    Serial1.print(F(" Humidity: "));
    Serial1.print(h);
    Serial1.print(F("%  Temperature: "));
    Serial1.print(t);
    Serial1.print(F("C "));
    Serial1.print(f);
    Serial1.print(F("F  Heat index: "));
    Serial1.print(hic);
    Serial1.print(F("C "));
    Serial1.print(hif);
    Serial1.print(F("F "));

    // Measure light intensity, print in terminal and send via bluetooth
    int light = analogRead(photoResistor);
    Serial.print(" Current brightness is ");
    Serial.print(light);
    Serial1.print(" Current brightness is ");
    Serial1.print(light);

    windspeed = ((analogRead(20) * 0.109) - 19.5);
    if(windspeed < 0){
        windspeed = 0;
        Serial.print(" Wind: ");
        Serial.print(windspeed);
        Serial1.print(" Wind ");
        Serial1.print(windspeed);
    }else {
        Serial.print(" Wind: ");
        Serial.print(windspeed);
        Serial1.print(" Wind ");
        Serial1.print(windspeed);
    }
    
}
