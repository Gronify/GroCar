from __future__ import print_function
import time
import serial
import os


serialArduino = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    
)
se = '';
serialArduino.isOpen();
print ('Go...')
while 1 :
    while serialArduino.inWaiting() > 0:
        serialArduino.read(1)
    command = ''
    while command == '':
        f = open('commandtosend.txt')
        command = f.read()
        f.close()
    os.system('clear')
    print (command)
    serialArduino.write(command + '\n')
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
    f = open('commandtosend.txt', 'w')
    f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
    f.close()
    serialEnd = False
    command = ''
    commanda = ''
    buff = ''
    sm = ''
    drs  = ''
    while serialArduino.inWaiting() < 40:
        time.sleep(0.01)   
    while not serialEnd:    
        if serialArduino.inWaiting() > 0:
            buff = str(serialArduino.read(1))
        command = command + buff
        if command == 'T_':
            while serialArduino.inWaiting() < 5:
                time.sleep(0.01)
            while buff != ';':
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            command = ''
            commanda = commanda + 'T_' + sm + ';'
            sm = ''
        if command == 'H_':
            command = ''
            while buff != ';': 
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'H_' + sm + ';'
            sm = ''
        if command == 'D_':
            command = ''
            while buff != ';':
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'D_' + sm + ';'
            sm = ''
        if command == 'LCam_':
            while serialArduino.inWaiting() < 5:
                time.sleep(0.01)
            command = ''
            while buff != ';': 
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'LCam_' + sm + ';'
            sm = ''
        if command == 'LCar_':
            command = ''
            while buff != ';':
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'LCar_' + sm + ';'
            sm = ''
        if command == 'DM_':
            command = ''
            while buff != ';': 
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'DM_' + sm + ';'
            sm = ''
        if command == 'DR_':
            command = ''
            while buff != ';': 
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'DR_' + sm + ';'
            sm = ''
        if command == 'SM_':
            command = ''
            while buff != ';': 
                buff = serialArduino.read(1)
                if buff != ';':
                    sm = str(sm) + str(buff)
            commanda = commanda + 'SM_' + sm + ';'
            sm = ''
        if command == 'DRS_':
            command = ''
            while buff != ';':
                buff = serialArduino.read(1)
                if buff != ';':     
                    drs = str(drs) + str(buff)
            commanda = commanda + 'DRS_' + drs + ';'
            sm = ''
        if command == 'A_OK!;\r\n':
            commanda = commanda + command
            f = open('commanda.txt', 'w')
            f.write(commanda)
            f.close()
            commanda = ''
            command = ''
            serialEnd = True
        if buff == '\n':
            command = ''
            serialEnd = True
        
        
        
