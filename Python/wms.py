from __future__ import print_function
import time
import serial
import os

t = 0.1
r = 1
print ('Go...')
while 1 :
    time.sleep(t)
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
                nt = f.read(1)
                f.read(1)
            if command == 'NH_':
                command = ''
                nh = f.read(1)
                f.read(1)
            if command == 'ND_':
                command = ''
                nd = f.read(1)
                f.read(1)
            if command == 'LCam_':
                command = ''
                lcam = f.read(1)
                f.read(1)
            if command == 'LCar_':
                command = ''
                lcar = f.read(1)
                f.read(1)
            if command == 'DM_':
                command = ''
                dm = f.read(1)
                f.read(1)
            if command == 'DR_':
                command = ''
                dr = f.read(1)
                f.read(1)
            if command == 'SM_':
                command = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        sm = str(sm) + str(buff)    
                sm = int(sm) 
            if command == 'DRS_':
                command = ''
                while buff != ';':
                    buff = f.read(1)
                    if buff != ';':
                        drs = str(drs) + str(buff)  
                drs = int(drs)
            if command == 'R_OK!;':
                command = ''
                f.close()
                serialEnd = True
    if r == 1:
        drs = drs + 1
        if drs > 140:
            r = 0
    if r == 0:
        drs = drs - 1
        if drs < 40:
            r = 1

    f = open('commandtosend.txt', 'w')
    f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
    f.close()

