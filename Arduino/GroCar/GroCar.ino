#include <Ultrasonic.h>
#include <Servo.h>
#include <DHT.h>
#include <ArduinoJson.h>

#define NULL (void)0
Servo webcamservo;
Ultrasonic ultrasonic(4, 3); //4 trig //3 echo
#define DHTPIN A3
DHT dht(DHTPIN, DHT11);

int pwm1m = 10;
int pwm2m = 5;
int pinOfMotorRotation1 = 9;
int pinOfMotorRotation2 = 8;
int pinOfMotorMove1 = 7;
int pinOfMotorMove2 = 6;
int pinOfLedCam = 2;
int pinOfLedCar = 11;

int temperatureAir;
int HumidityAir;
int distance;
boolean temperatureChange;
boolean HumidityChange;
boolean distanceChange;
char inCharFromSerialPort;
String inStringFromSerialPort;
String responseToSerialString;
boolean needTemperature;
boolean needHumidity;
boolean needDistance;
boolean lightCam;
boolean lightCar;
int directionOfMovement = 2;
int directionOfRotationWheels = 2;
int speedOfMovement;
int speedOfRotationWheels;
int directionOfRotationWebCamServo = 90;

int temp;
boolean serialEnd;
StaticJsonDocument<256> requestFromSerial;
StaticJsonDocument<256> responseToSerial;
void setup()
{
  pinMode(pwm1m, OUTPUT);
  pinMode(pwm2m, OUTPUT);
  pinMode(pinOfMotorRotation1, OUTPUT);
  pinMode(pinOfMotorRotation2, OUTPUT);
  pinMode(pinOfMotorMove1, OUTPUT);
  pinMode(pinOfMotorMove2, OUTPUT);
  pinMode(pinOfLedCam, OUTPUT);
  pinMode(pinOfLedCar, OUTPUT);
  // Serial.begin(9600);
  Serial.begin(115200);
  dht.begin();
  webcamservo.attach(12);
}

void loop()
{
  if (Serial.available() > 0)
  {
    readSerial();
    writeSerial();
  }
  if ((temperatureChange && needTemperature) || (HumidityChange && needHumidity) || (distanceChange && needDistance))
  {
    writeSerial();
  }
  !needTemperature ? NULL : temperatureSensor();
  !needHumidity ? NULL : humiditySensor();
  !needDistance ? NULL : DistanceSensor();
}

void readSerial()
{
  serialEnd = false;
  while (!serialEnd)
  {
    if (Serial.available() > 0)
    {
      inCharFromSerialPort = Serial.read();
      inStringFromSerialPort += (char)inCharFromSerialPort;
      serialEnd = (inCharFromSerialPort == '\n') ? true : false;
    }
  }

  deserializeJson(requestFromSerial, inStringFromSerialPort);
  JsonObject object = requestFromSerial.as<JsonObject>();

  if (requestFromSerial.containsKey("set"))
  {
    if (requestFromSerial["set"].containsKey("t"))
    {
      needTemperature = (bool)requestFromSerial["set"]["t"];
    }
    if (requestFromSerial["set"].containsKey("h"))
    {
      needHumidity = (bool)requestFromSerial["set"]["h"];
    }
    if (requestFromSerial["set"].containsKey("d"))
    {
      needDistance = (bool)requestFromSerial["set"]["d"];
    }
    if (requestFromSerial["set"].containsKey("lcam"))
    {
      lightCam = (bool)requestFromSerial["set"]["lcam"];
      lightCamFun();
    }
    if (requestFromSerial["set"].containsKey("lcar"))
    {
      lightCar = (bool)requestFromSerial["set"]["lcar"];
      lightCarFun();
    }
    if (requestFromSerial["set"].containsKey("sm"))
    {
      speedOfMovement = requestFromSerial["set"]["sm"];
    }
    if (requestFromSerial["set"].containsKey("sr"))
    {
      speedOfRotationWheels = requestFromSerial["set"]["sr"];
    }
  }
  else if (requestFromSerial.containsKey("req"))
  {
    if (requestFromSerial["req"].containsKey("dm"))
    {
      directionOfMovement = requestFromSerial["req"]["dm"];
      switch (directionOfMovement)
      {
      case 0:
        MotorMoveForward();
        break;
      case 1:
        MotorMoveBackward();
        break;
      default:
        MotorMoveStop();
        break;
      }
    }
    if (requestFromSerial["req"].containsKey("dr"))
    {
      directionOfRotationWheels = requestFromSerial["req"]["dr"];
      switch (directionOfRotationWheels)
      {
      case 0:
        RotationWheelsLeft();
        break;
      case 1:
        RotationWheelsRight();
        break;
      default:
        RotationWheelsStop();
        break;
      }
    }
    if (requestFromSerial["req"].containsKey("drs"))
    {
      directionOfRotationWebCamServo = requestFromSerial["req"]["drs"];
      WebCamServo();
    }
  }
  inStringFromSerialPort = "";
}

void temperatureSensor()
{
  temp = dht.readTemperature();
  if (temperatureAir != temp)
  {
    temperatureAir = temp;
    temperatureChange = true;
  }
}
void humiditySensor()
{
  temp = dht.readHumidity();
  if (HumidityAir != temp)
  {
    HumidityAir = temp;
    HumidityChange = true;
  }
}
void DistanceSensor()
{
  temp = ultrasonic.Ranging(true);
  if (distance != temp)
  {
    distance = temp;
    distanceChange = true;
  }
}
void lightCamFun()
{
  lightCam ? digitalWrite(pinOfLedCam, HIGH) : digitalWrite(pinOfLedCam, LOW);
}
void lightCarFun()
{
  lightCar ? digitalWrite(pinOfLedCar, HIGH) : digitalWrite(pinOfLedCar, LOW);
}

void RotationWheelsLeft()
{
  digitalWrite(pinOfMotorRotation1, HIGH);
  digitalWrite(pinOfMotorRotation2, LOW);
  analogWrite(pwm1m, speedOfRotationWheels);
}

void RotationWheelsRight()
{
  digitalWrite(pinOfMotorRotation1, LOW);
  digitalWrite(pinOfMotorRotation2, HIGH);
  analogWrite(pwm1m, speedOfRotationWheels);
}

void RotationWheelsStop()
{
  digitalWrite(pinOfMotorRotation1, LOW);
  digitalWrite(pinOfMotorRotation2, LOW);
  analogWrite(pwm1m, 0);
}

void MotorMoveForward()
{
  digitalWrite(pinOfMotorMove1, HIGH);
  digitalWrite(pinOfMotorMove2, LOW);
  analogWrite(pwm2m, speedOfMovement);
}

void MotorMoveBackward()
{
  digitalWrite(pinOfMotorMove1, LOW);
  digitalWrite(pinOfMotorMove2, HIGH);
  analogWrite(pwm2m, speedOfMovement);
}

void MotorMoveStop()
{
  digitalWrite(pinOfMotorMove1, LOW);
  digitalWrite(pinOfMotorMove2, LOW);
  analogWrite(pwm2m, 0);
}

void WebCamServo()
{
  webcamservo.write(directionOfRotationWebCamServo);
}
void writeSerial()
{
  responseToSerialString = "{ ";
  if (temperatureChange && needTemperature)
  {
    temperatureChange = false;
    responseToSerialString += String("\"t\":") + temperatureAir + ",";
  }
  if (HumidityChange && needHumidity)
  {
    HumidityChange = false;
    responseToSerialString += String("\"h\":") + HumidityAir + ",";
  }
  if (distanceChange && needDistance)
  {
    distanceChange = false;
    responseToSerialString += String("\"d\":") + distance + ",";
  }

  if (responseToSerialString[responseToSerialString.length() - 1] == ',')
  {
    responseToSerialString = responseToSerialString.substring(0, responseToSerialString.length() - 1);
  }

  responseToSerialString += "}";
  responseToSerial.clear();

  responseToSerial["data"] = serialized(responseToSerialString);
  serializeJson(responseToSerial, Serial);
  Serial.println();
}

