#include <Ultrasonic.h>
#include <Servo.h>
#include <DHT.h>

Servo webcamservo;
Ultrasonic ultrasonic( 4, 3 );//4 trig //3 echo
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
int inCharFromSerialPort;
String inStringFromSerialPort;
boolean needTemperature;
boolean needHumidity;
boolean needDistance;
boolean lightCam;
boolean lightCar;
int directionOfMovement =  2;
int directionOfRotationWheels = 2;
int speedOfMovement;
int directionOfRotationWebCamServo;

boolean serialEnd;
void setup() {
  pinMode (pwm1m, OUTPUT);
  pinMode (pwm2m, OUTPUT);
  pinMode (pinOfMotorRotation1, OUTPUT);
  pinMode (pinOfMotorRotation2, OUTPUT);
  pinMode (pinOfMotorMove1, OUTPUT);
  pinMode (pinOfMotorMove2, OUTPUT);
  pinMode (pinOfLedCam, OUTPUT);
  pinMode (pinOfLedCar, OUTPUT);
  // Serial.begin(9600);
  Serial.begin(115200);
  dht.begin();
  webcamservo.attach(12);

}

void loop() {
  controlSerial();
}

void controlSerial() {

  if (Serial.available() > 0) {
    serialEnd = false;

    while (!serialEnd) {

      if (Serial.available() > 0) {
        inCharFromSerialPort = Serial.read();
        /*if ((char)inCharFromSerialPort == "!"){
          inStringFromSerialPort = "";
          Serial.read();
          Serial.read();
          serialEnd = true;
          controlSerialSend();
          }*/
        inStringFromSerialPort += (char)inCharFromSerialPort;
      }
      delay(2);

      if (inStringFromSerialPort == "NT_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        needTemperature = (bool)inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }

      if (inStringFromSerialPort == "NH_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        needHumidity = (bool)inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "ND_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        needDistance = (bool)inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "LCam_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        lightCam = (bool)inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "LCar_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        lightCar = (bool)inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "DM_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        directionOfMovement = inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "DR_") {
        inStringFromSerialPort = "";
        inCharFromSerialPort = Serial.read();
        inStringFromSerialPort += (char)inCharFromSerialPort;
        directionOfRotationWheels = inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
        Serial.read();
      }
      if (inStringFromSerialPort == "SM_") {
        inStringFromSerialPort = "";
        while ((char)inCharFromSerialPort != ';') {
          inCharFromSerialPort = Serial.read();
          inStringFromSerialPort += (char)inCharFromSerialPort;
        }
        speedOfMovement = inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
      }
      if (inStringFromSerialPort == "DRS_") {

        inStringFromSerialPort = "";
        while ((char)inCharFromSerialPort != ';') {
          inCharFromSerialPort = Serial.read();
          inStringFromSerialPort += (char)inCharFromSerialPort;
        }
        directionOfRotationWebCamServo = inStringFromSerialPort.toInt();
        inStringFromSerialPort = "";
      }
      if (inStringFromSerialPort == "R_OK!;\n") {
        inStringFromSerialPort = "";
        serialEnd = true;
        controlSerialSend();
      }

    }


  }
  if (needTemperature) {
    temperatureSensor();
  }
  if (needHumidity) {
    humiditySensor();
  }
  if (needDistance) {
    DistanceSensor();
  }
  if (directionOfRotationWheels == 0) {
    RotationWheelsLeft();
  } else if (directionOfRotationWheels == 1) {
    RotationWheelsRight();
  } else {
    RotationWheelsStop();
  }
  if (directionOfMovement == 0) {
    MotorMoveForward();
  } else if (directionOfMovement == 1) {
    MotorMoveBackward();
  } else {
    MotorMoveStop();
  }
  lightCamFun();
  lightCarFun();
  WebCamServo();
}

void temperatureSensor() {
  temperatureAir = dht.readTemperature();
}
void humiditySensor() {
  HumidityAir = dht.readHumidity();
}
void DistanceSensor() {
  distance = ultrasonic.Ranging(true);

}
void lightCamFun() {
  if (lightCam) {
    digitalWrite (pinOfLedCam, HIGH);
  }
  else {
    digitalWrite (pinOfLedCam, LOW);
  }
}
void lightCarFun() {
  if (lightCar) {
    digitalWrite (pinOfLedCar, HIGH);
  }
  else {
    digitalWrite (pinOfLedCar, LOW);

  }
}


void RotationWheelsLeft() {

  digitalWrite (pinOfMotorRotation1, HIGH);
  digitalWrite (pinOfMotorRotation2, LOW);
  analogWrite(pwm1m, 255);

}

void RotationWheelsRight() {

  digitalWrite (pinOfMotorRotation1, LOW);
  digitalWrite (pinOfMotorRotation2, HIGH);
  analogWrite(pwm1m, 255);

}

void RotationWheelsStop() {

  digitalWrite (pinOfMotorRotation1, LOW);
  digitalWrite (pinOfMotorRotation2, LOW);
  analogWrite(pwm1m, 0);

}


void MotorMoveForward() {

  digitalWrite (pinOfMotorMove1, HIGH);
  digitalWrite (pinOfMotorMove2, LOW);
  analogWrite(pwm2m, speedOfMovement);

}

void MotorMoveBackward() {

  digitalWrite (pinOfMotorMove1, LOW);
  digitalWrite (pinOfMotorMove2, HIGH);
  analogWrite(pwm2m, speedOfMovement);

}
void MotorMoveStop() {

  digitalWrite (pinOfMotorMove1, LOW);
  digitalWrite (pinOfMotorMove2, LOW);
  analogWrite(pwm2m, 0);

}

void WebCamServo() {

  webcamservo.write(directionOfRotationWebCamServo);

}
void controlSerialSend() {
  Serial.print("T_");
  if (needTemperature) {
    Serial.print(temperatureAir);
  } else {
    Serial.print("Off");
  }
  Serial.print(";");

  Serial.print("H_");
  if (needHumidity) {
    Serial.print(HumidityAir);
  } else {
    Serial.print("Off");
  }
  Serial.print(";");

  Serial.print("D_");
  if (needDistance) {
    Serial.print(distance);
  } else {
    Serial.print("Off");
  }
  Serial.print(";");

  Serial.print("LCam_");
  if (lightCam) {
    Serial.print("1");
  } else {
    Serial.print("0");
  }
  Serial.print(";");

  Serial.print("LCar_");
  if (lightCar) {
    Serial.print("1");
  } else {
    Serial.print("0");
  }
  Serial.print(";");

  Serial.print("DM_");
  Serial.print(directionOfMovement);
  Serial.print(";");

  Serial.print("DR_");
  Serial.print(directionOfRotationWheels);
  Serial.print(";");

  Serial.print("SM_");
  Serial.print(speedOfMovement);
  Serial.print(";");

  Serial.print("DRS_");
  Serial.print(directionOfRotationWebCamServo);
  Serial.print(";");

  Serial.println("A_OK!;");

}





