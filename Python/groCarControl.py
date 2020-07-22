import pygame
import time
import json
import copy

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
global jsonToSend
#read json data from arduino
def fileReadJson():
  with open('jsonSerial.json') as json_file_serial:
    jsonFromSerialBuff = json.load(json_file_serial)
  global jsonFromSerial
  jsonFromSerial = copy.deepcopy(jsonFromSerialBuff)
    
#read json data from rpi
def fileReadJsonRPI():
  with open('jsonSend.json') as json_file:
      jsonToSendBuff = json.load(json_file)
  global jsonToSend
  jsonToSend = copy.deepcopy(jsonToSendBuff) 
   

def fileWriteJsonRPI(data):
  with open('jsonSend.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

def draw_background(screen):
  screen.fill(white)
  screen.fill((255, 255, 255))
  fileReadJsonRPI()
 
  f1 = pygame.font.Font(None, 36)
  temp = f1.render("Temperature:" + jsonFromSerial["data"]["t"], 1, (0, 0, 0))
  humd = f1.render("Humidity:" + jsonFromSerial["data"]["h"], 1, (0, 0, 0))
  dist = f1.render("Distance:" + jsonFromSerial["data"]["d"], 1, (0, 0, 0))
  lcam = f1.render("Light Cam:" + jsonFromSerial["data"]["lcam"], 1, (0, 0, 0))
  lcar = f1.render("Light Car:" + jsonFromSerial["data"]["lcar"], 1, (0, 0, 0))
  sped = f1.render("Speed:" + jsonFromSerial["data"]["sm"], 1, (0, 0, 0))
  spedr = f1.render("Speed Of Rotation:" + jsonFromSerial["data"]["sr"], 1, (0, 0, 0))
  drs = f1.render("Rotation Of Cam:" + jsonFromSerial["data"]["drs"], 1, (0, 0, 0))
 
  screen.blit(temp, (10, 50))
  screen.blit(humd, (10, 100))
  screen.blit(dist, (10, 150))
  screen.blit(lcam, (10, 200))
  screen.blit(lcar, (10, 250))
  screen.blit(sped, (10, 300))
  screen.blit(spedr, (10, 350))
  screen.blit(drs, (10, 400))


fileReadJsonRPI()

pygame.init()

screen = pygame.display.set_mode([300, 500])


clock = pygame.time.Clock()

done=False
gron = 0
while done == False:
 for event in pygame.event.get():   
  if event.type == pygame.QUIT:
    done = True
       
  if event.type == pygame.KEYDOWN:
    fileReadJsonRPI()
    if event.key == pygame.K_w:
      jsonToSend["req"]["dm"] = 0
    if event.key == pygame.K_s:
      jsonToSend["req"]["dm"] = 1
    if event.key == pygame.K_a:
      jsonToSend["req"]["dr"] = 0
    if event.key == pygame.K_d:
      jsonToSend["req"]["dr"] = 1
    fileWriteJsonRPI(jsonToSend)
    
    while pygame.key.get_pressed()[pygame.K_r]:
      fileReadJsonRPI()
      time.sleep(0.07)
      pygame.event.get()
      sm = jsonToSend["set"]["sm"] + 1
      if sm < 256:
        jsonToSend["set"]["sm"] = sm
        fileWriteJsonRPI(jsonToSend)

    while pygame.key.get_pressed()[pygame.K_f]:
      fileReadJsonRPI()
      time.sleep(0.07)
      pygame.event.get()
      sm = jsonToSend["set"]["sm"] - 1
      if sm > 0:
        jsonToSend["set"]["sm"] = sm
        fileWriteJsonRPI(jsonToSend)    

    while pygame.key.get_pressed()[pygame.K_q]:
      fileReadJsonRPI()
      time.sleep(0.07)
      pygame.event.get()
      drs = jsonToSend["req"]["drs"] + 1
      if drs < 181:
        jsonToSend["req"]["drs"] = drs
        fileWriteJsonRPI(jsonToSend)  

    while pygame.key.get_pressed()[pygame.K_e]:
      fileReadJsonRPI()
      time.sleep(0.07)
      pygame.event.get()
      drs = jsonToSend["req"]["drs"] - 1
      if drs >= 0:
        jsonToSend["req"]["drs"] = drs
        fileWriteJsonRPI(jsonToSend)     
                      
    if event.key == pygame.K_c:
      jsonToSend["req"]["drs"] = 90
      fileWriteJsonRPI(jsonToSend)

    if event.key == pygame.K_z:
      if jsonToSend["set"]["lcam"] == 0:
        jsonToSend["set"]["lcam"] = 1
      elif jsonToSend["set"]["lcam"] == 1:
        jsonToSend["set"]["lcam"] = 0

    if event.key == pygame.K_x:
      if jsonToSend["set"]["lcar"] == 0:
        jsonToSend["set"]["lcar"] = 1
      elif jsonToSend["set"]["lcar"] == 1:
        jsonToSend["set"]["lcar"] = 0

    if event.key == pygame.K_t:
      if jsonToSend["set"]["t"] == 0:
        jsonToSend["set"]["t"] = 1
      elif jsonToSend["set"]["t"] == 1:
        jsonToSend["set"]["t"] = 0

    if event.key == pygame.K_h:
      if jsonToSend["set"]["h"] == 0:
        jsonToSend["set"]["h"] = 1
      elif jsonToSend["set"]["h"] == 1:
        jsonToSend["set"]["h"] = 0

    if event.key == pygame.K_g:
      if jsonToSend["set"]["d"] == 0:
        jsonToSend["set"]["d"] = 1
      elif jsonToSend["set"]["d"] == 1:
        jsonToSend["set"]["d"] = 0
    fileWriteJsonRPI(jsonToSend)

      # Если кнопка была отпущена, то и движение надо прекратить
  if event.type == pygame.KEYUP:
    fileReadJsonRPI()
    if event.key == pygame.K_w:
      jsonToSend["req"]["dm"] = 2
    if event.key == pygame.K_s:
      jsonToSend["req"]["dm"] = 2
    if event.key == pygame.K_a:
      jsonToSend["req"]["dr"] = 2
    if event.key == pygame.K_d:
      jsonToSend["req"]["dr"] = 2
    fileWriteJsonRPI(jsonToSend)
   
#  freadd() 
 draw_background(screen) 
 pygame.display.flip()
 clock.tick(60)
pygame.quit()
