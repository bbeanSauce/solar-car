import board
import digitalio
import time

#define relays
main_relay = digitalio.DigitalInOut(board.GP6)
precharge_relay = digitalio.DigitalInOut(board.GP7)
gnd_relay = digitalio.DigitalInOut(board.GP8)

#set relays as outputs
main_relay.direction = digitalio.Direction.OUTPUT
precharge_relay.direction = digitalio.Direction.OUTPUT
gnd_relay.direction = digitalio.Direction.OUTPUT

#input data pins
charge_enable = digitalio.DigitalInOut(board.GP0)
discharge_enable = digitalio.DigitalInOut(board.GP1)

#set input as input
charge_enable.switch_to_input( pull=digitalio.Pull.UP)
discharge_enable.switch_to_input( pull=digitalio.Pull.UP)

#idk russell did it
charge_enable.pull = digitalio.Pull.UP
discharge_enable.pull = digitalio.Pull.UP


car_started = False

#turn everything off
main_relay.value = False
precharge_relay.value = False
gnd_relay.value = False


print("charge enable value:{}, discharge enable value: {}".format(charge_enable.value, discharge_enable.value))


#run the car
while not car_started:
    
    if not charge_enable.value and not discharge_enable.value and not car_started:
        
        gnd_relay.value = True
        print("ground relay on")
        precharge_relay.value = True
        print("precharge relay on")
                
        time.sleep(5)
        
        main_relay.value = True
        print("main relay on")
        
        time.sleep(1)
        
        precharge_relay.value = False
        print("precharge relay off")
        
        car_started = True
        
        time.sleep(1)
        

while car_started:
    
    if charge_enable.value or discharge_enable.value:
        
        main_relay.value = False
        gnd_relay.value = False
        precharge_relay.value = False
        print("car off")
    
