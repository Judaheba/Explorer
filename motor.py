#Motor juan
#import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#GPIO.setup(7, GPIO.OUT)
gpio -g mode 7 out

pwm1 = GPIO.PWM(23, 70)
pwm2 = GPIO.PWM(24, 70)


while(True):
#for i in range(100000):
	adelante= raw_input("w adelante,s atras,d derecha,a izquierda,f parar:")

	if adelante == 'l':
		#GPIO.output(7,True)
		gpio -g write 7 1
	if adelante == 'k':
		#GPIO.output(7,False)
		gpio -g write 7 0
#		GPIO.output(6,False)
#Atras
	if adelante == 's':
		GPIO.output(4,True)
		GPIO.output(27,True)
		GPIO.output(17,False)
		GPIO.output(22,False)
		pwm1.start(70)
		pwm2.start(70)
		#for i in range(100,-1,-1):
		        #pwm1.ChangeDutyCycle(100 - i)
		        #time.sleep(0.02) 
#Adelante
	if adelante == 'w':
		GPIO.output(4,False)
		GPIO.output(27,False)
		GPIO.output(17,True)
		GPIO.output(22,True)
		pwm1.start(100)
		pwm2.start(100)
	
#derecha
	if adelante == 'd':
		GPIO.output(4,True)
		GPIO.output(27,False)
		GPIO.output(17,False)
		GPIO.output(22,True)
		pwm1.start(80)
		pwm2.start(80)
#izquierda
	if adelante == 'a':
		GPIO.output(4,False)
		GPIO.output(27,True)
		GPIO.output(17,True)
		GPIO.output(22,False)
		pwm1.start(80)
		pwm2.start(80)
#parar
	if adelante == 'f':
		GPIO.output(4,False)
		GPIO.output(27,False)
		GPIO.output(17,False)
		GPIO.output(22,False) 
GPIO.cleanup()

