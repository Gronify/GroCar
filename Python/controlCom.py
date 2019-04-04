from pynput import keyboard
import time


def on_press(key):
    try:
      #  print('alphanumeric key {0} pressed'.format(
       #     key.char))
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
        if format(key.char) == 'w':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(0) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 's':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(1) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'e':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(0) + ';DR_' + str(1) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'q':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(0) + ';DR_' + str(0) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'a':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(1) + ';DR_' + str(0) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'd':
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(1) + ';DR_' + str(1) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'r':
            sm = sm + 1
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        if format(key.char) == 'f':
            sm = sm - 1
            f = open('commandtosend.txt', 'w')
            f.write('NT_' + str(nt) + ';NH_' + str(nh) + ';ND_' + str(nd) + ';LCam_' + str(lcam) + ';LCar_' + str(lcar) + ';DM_'+ str(dm) + ';DR_' + str(dr) + ';SM_' + str(sm) + ';DRS_' + str(drs) +  ';R_OK!;')
            f.close()
        
    except AttributeError:
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
                dn = f.read(1)
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
                serialEnd = True

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:listener.join()

    
