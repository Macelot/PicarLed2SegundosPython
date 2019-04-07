#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Desenvolver um circuito e programar para que pisque      # 
#  (o mínimo possível) um LED a cada dois segundos.         #
#                                                           # 
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 12
try:
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    while(1):
        GPIO.output(pin_to_circuit,1)
        print("***LIGADO***")
        time.sleep(.010)
        GPIO.output(pin_to_circuit,0)
        print("---DESLIGADO---")
        time.sleep(1.990)
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()
