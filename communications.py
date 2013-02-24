import time
import serial
import threading


class Spray(object):
	spraying = False

	def __init__(self, port):
		super(Spray, self).__init__()
		# self.arg = arg
		self.serial = serial.Serial(port)
		self.serial.close()
		self.serial.open()
		
	def on(self):
		print 'spray on'
		self.serial.write('H');
		self.spraying = True
	
	def off(self):
		print 'spray off'
		self.serial.write('L')
		self.spraying = False
	
	def pulse(self, delay=0.18):
		print 'pulse'
		self.on()
		threading.Thread(target=self.pulse_off, args=(delay,)).start()
	
	def pulse_off(self, delay):
		time.sleep(delay)
		self.off()
		print 'plused'