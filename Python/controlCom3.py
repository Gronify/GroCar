import pygame
import time

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)


def freadd():
    global t
    global h
    global d
    global lce
    global lcr
    global speed
    global drss
    t = ""
    h = ""
    d = ""
    lce = ""
    lcr = ""
    speed = ""
    drss = ""
    f = open('commanda.txt')
    serialEnd = False
    commanda = ''
    command = ''
    buff = ''
    sm = ''
    drs  = ''
    while not serialEnd:
            buff = f.read(1)
            command = command + buff
            if command == 'T_':
                t = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        t = str(t) + str(buff)
                command = ''
            if command == 'H_':
                h = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        h = str(h) + str(buff)
                command = ''
            if command == 'D_':
                d = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        d = str(d) + str(buff)
                command = ''
            if command == 'LCam_':
                lce = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        lce = str(lce) + str(buff)
                        if lce == '0':
                            lce = 'Off'
                        if lce == '1':
                              lce = 'On'
                command = ''  
            if command == 'LCar_':
                lcr = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        lcr = str(lcr) + str(buff)
                        if lcr == '0':
                            lcr = 'Off'
                        if lcr == '1':
                              lcr = 'On'
                command = '' 
            if command == 'DM_':
                gh = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        gh = str(gh) + str(buff)
                command = '' 
            if command == 'DR_':
                dr = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        dr = str(dr) + str(buff)
                command = ''
            if command == 'SM_':
                speed = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        speed = str(speed) + str(buff)
                command = ''
                speed = float(speed)
                speed = speed / 2.55
                speed = int(speed) 
            if command == 'DRS_':
                drss = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        drss = str(drss) + str(buff)
                command = ''
            if command == 'A_OK!;':
                command = ''
                f.close()
                serialEnd = True


def draw_background(screen):
 screen.fill(white)
 screen.fill((255, 255, 255))
 
 f1 = pygame.font.Font(None, 36)
 temp = f1.render("Temperature:" + str(t), 1, (0, 0, 0))
 humd = f1.render("Humidity:" + str(h), 1, (0, 0, 0))
 dist = f1.render("Distance:" + str(d), 1, (0, 0, 0))
 lcam = f1.render("Light Cam:" + str(lce), 1, (0, 0, 0))
 lcar = f1.render("Light Car:" + str(lcr), 1, (0, 0, 0))
 sped = f1.render("Speed:" + str(speed), 1, (0, 0, 0))
 drs = f1.render("Rotation Of Cam:" + str(drss), 1, (0, 0, 0))
 
 screen.blit(temp, (10, 50))
 screen.blit(humd, (10, 100))
 screen.blit(dist, (10, 150))
 screen.blit(lcam, (10, 200))
 screen.blit(lcar, (10, 250))
 screen.blit(sped, (10, 300))
 screen.blit(drs, (10, 350))

def fread():
    f = open('commandtosend.txt')
    serialEnd = False
    command = ''
    buff = ''
    sm = ''
    drs  = ''
    while not serialEnd:
        buff = f.read(1)
        command = command + buff
        if command == 'NT_':
            command = ''
            global nt 
            nt = f.read(1)
            f.read(1)
        if command == 'NH_':
            command = ''
            global nh 
            nh = f.read(1)
            f.read(1)
        if command == 'ND_':
            command = ''
            global nd
            nd = f.read(1)
            f.read(1)
        if command == 'LCam_':
            command = ''
            global lcam
            lcam = f.read(1)
            f.read(1)
        if command == 'LCar_':
            command = ''
            global lcar
            lcar = f.read(1)
            f.read(1)
        if command == 'DM_':
            command = ''
            global dm
            dm = f.read(1)
            f.read(1)
        if command == 'DR_':
            command = ''
            global dr
            dr = f.read(1)
            f.read(1)
        if command == 'SM_':
            command = ''
            global sm
            while buff != ';':
                buff = f.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)    
            sm = int(sm)
        if command == 'DRS_':
            command = ''
            global drs
            while buff != ';':
                buff = f.read(1)
                if buff != ';':
                    drs = str(drs) + str(buff)  
            drs = int(drs)
        if command == 'R_OK!;':
            command = ''
            f.close()
            serialEnd = True

 
fread() 
freadd()
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
       fread()
       if event.key == pygame.K_w:
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(0) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_s:
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(1) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_a:
        fread()
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(0) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_d:
        fread()
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(1) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       while pygame.key.get_pressed()[pygame.K_r]:
           fread()
           time.sleep(0.07)
           pygame.event.get()
           
           sm = sm + 1
           if sm < 256:
                f = open('commandtosend.txt', 'w')
                f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
                f.close()
           
                   
       while pygame.key.get_pressed()[pygame.K_f]:
           fread()
           time.sleep(0.07)
           pygame.event.get()
                
           sm = sm - 1
           if sm > 0:
             f = open('commandtosend.txt', 'w')
             f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
             f.close()
           
                   
       while pygame.key.get_pressed()[pygame.K_q]:
           fread()
           time.sleep(0.07)
           pygame.event.get()
           drs = drs + 1
           if drs < 181:
                f = open('commandtosend.txt', 'w')
                f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
                f.close()
                       
       while pygame.key.get_pressed()[pygame.K_e]:
           fread()
           time.sleep(0.07)
           pygame.event.get()
           drs = drs - 1
           if drs >= 0:
                f = open('commandtosend.txt', 'w')
                f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
                f.close()
                       
       if event.key == pygame.K_c:
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(90) +  ';R_OK!;')
           f.close()
       if event.key == pygame.K_z:
           if lcam == '0':
                    lcam = '1'
           elif lcam == '1':
                    lcam = '0'
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
           f.close()
       if event.key == pygame.K_x:
           if lcar == '0':
                    lcar = '1'
           elif lcar == '1':
                    lcar = '0'
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
           f.close()
       if event.key == pygame.K_t:
           if nt == '0':
                    nt = '1'
           elif nt == '1':
                    nt = '0'
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
           f.close()
       if event.key == pygame.K_h:
           if nh == '0':
                    nh = '1'
           elif nh == '1':
                    nh = '0'
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
           f.close()
       if event.key == pygame.K_g:
           if nd == '0':
                    nd = '1'
           elif nd == '1':
                    nd = '0'
           f = open('commandtosend.txt', 'w')
           f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
           f.close()
        
       
        
      # Если кнопка была отпущена, то и движение надо прекратить
  if event.type == pygame.KEYUP:
       fread()
       if event.key == pygame.K_w:
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(2) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_s:
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(2) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_a:
        fread()
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(2) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
       if event.key == pygame.K_d:
        fread()
        f = open('commandtosend.txt', 'w')
        f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(2) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
        f.close()
   
 freadd() 
 draw_background(screen) 
 pygame.display.flip()
 clock.tick(60)
pygame.quit()
