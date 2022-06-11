from RPi import GPIO as gpio
from time import slee

gpio.setmode(gpio.BOARD)    #Pin Notation will be followed
                            #as of the physical board pin
gpio.setwarnings(False)     #To avoid warnings

'''Setting Up Control Pins Of Relay Module As An Output
   Of Pi'''

gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)

'''Setting UP Control Pins Of IR Module As An Input
   Of Pi'''

gpio.seup(10, gpio.IN)
gpio.setup(12, gpio.IN)
while True:

 irFrontModule = gpio.input(10)
 irBackModule = gpio.input(12)
 print(irFrontModule, irBackModule)
 if irFrontModule == 0 :
  RelayModule1 = gpio.output(7, 1)
  RelayModule1 = gpio.output(7, 0)
  sleep(5)
 elif irBackModele == 1 :
  RelayModule2 = gpio.output(8, 1)
  RelayModule2 = gpio.output(8, 0)
  sleep(5)
