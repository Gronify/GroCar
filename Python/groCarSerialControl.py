# from __future__ import print_function
import time
import serial
import json
import os
import copy
import threading

def thread_function():
  while 1:
    a = input()
    f = open('jsonSend.json', 'w')
    f.write(a)
    f.close()
    
if __name__ == "__main__":
  x = threading.Thread(target=thread_function)
  print('Write port:')
  serialPort = '/dev/ttyUSB'
  serialPort = serialPort + str(input())
  x.start()
  serialArduino = serial.Serial(
    port=serialPort,
    baudrate=115200, 
  )
  serialArduino.isOpen()
  time.sleep(5)
  while serialArduino.inWaiting() > 0:
    serialArduino.read(1)
  
  with open('jsonSend.json') as json_file:
    jsonToSendBuff = json.load(json_file)

  #statinfo = os.stat('jsonSend.json')
  jsonToSend = copy.deepcopy(jsonToSendBuff) 
  while 1:
    #Send json to Serial
    if jsonToSend:
      print(jsonToSend)
      serialArduino.write(str.encode(str(jsonToSend)))
      serialArduino.write(str.encode('\n'))
    #############################################
    oldJsonToSend = copy.deepcopy(jsonToSendBuff) 

    with open('jsonSend.json') as json_file:
      jsonToSendBuff = json.load(json_file)
    jsonToSend = copy.deepcopy(jsonToSendBuff) 
    for external_key in list(jsonToSend):
      if jsonToSend[external_key] == oldJsonToSend[external_key]:
        jsonToSend.pop(external_key)
    for external_key in list(jsonToSend):
      for internal_key in list(jsonToSend[external_key]):
        if jsonToSend[external_key][internal_key] == oldJsonToSend[external_key][internal_key]:
          jsonToSend[external_key].pop(internal_key)
    
    time.sleep(0.5)
    #Read json from Serial
    
    while serialArduino.inWaiting() > 0:
      jsonFromSerial = serialArduino.readline()
      print(jsonFromSerial.decode('utf-8'))
      f = open('jsonSerial.json', 'w')
      f.write(str(jsonFromSerial))
      f.close()
    

