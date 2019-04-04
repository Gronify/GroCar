import time
import random
import datetime
import telepot
import commands
import serial
time.sleep(10)
operation = "v4l2-ctl --set-ctrl saturation=100"
result = commands.getoutput(operation)
print result
operation = "v4l2-ctl --set-ctrl hue=0"
result = commands.getoutput(operation)
print result
operation = "v4l2-ctl --set-ctrl brightness=120"
result = commands.getoutput(operation)
print result
operation = "v4l2-ctl --set-ctrl contrast=15"
result = commands.getoutput(operation)
print result


