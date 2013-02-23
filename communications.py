import time
import serial

def init(port):
  inited=1;
  chalk=serial.Serial(port);
  chalk.open();

def SprayChalk():
  if(inited):
    print "Chalk on";
    chalk.write('H');
    time.sleep(.01);
    print "Chalk Off";
    chalk.write('L');
  else:
    print "No port opened";
