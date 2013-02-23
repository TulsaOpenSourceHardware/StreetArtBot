import time
import serial

inited=0
chalk=0;
def init(port):
  global inited;
  global chalk
  inited=1;
  chalk=serial.Serial(port);
  chalk.open();

def SprayChalk():
  global chalk
  global inited
  if(inited==0):
    print "Init first"
    return
  print "Chalk on";
  chalk.write('H');
  time.sleep(.01);
  print "Chalk Off";
  chalk.write('L');
