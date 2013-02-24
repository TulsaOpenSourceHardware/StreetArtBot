import time
import serial

inited=0
chalk=0;
def init(port):
  global inited;
  global chalk
  inited=1;

  chalk=serial.Serial("COM7");
  chalk.close();
  chalk.open();

def Step():
    chalk.write('L');
    time.sleep(.1);
def StopSpraying():
  chalk.write('L')
  chalk.write('L')
  chalk.write('L')
  chalk.write('L')
  chalk.write('L')
  print "Chalk Off";
def SprayChalk():
  global chalk
  global inited
  if(inited==0):
    print "Init first"
    return
  print "Chalk on";
  chalk.write('H');
  chalk.write('H');
  chalk.write('H');
  chalk.write('H');
  chalk.write('H');
  #time.sleep(.1);
  #chalk.write('L');
  #chalk.write('L');
  #chalk.write('L');
  #chalk.write('L');