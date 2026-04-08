from gpiozero import LED, Button
from time import sleep


leds = {
        "1": LED(27),
        "2": LED(22),
        "3": LED(23),
        "4": LED(24)
    }


btn = Button(25)

speed = 0.1

def toggle():
    if leds['1'].is_lit:
        for _, led in leds.items():
            led.off()
    elif not leds['1'].is_lit:
        for _, led in leds.items():
            led.on()

def LtR():
    for _, led in leds.items():
        led.on()
        sleep(speed)
        led.off()

def RtL():
    for _, led in reversed(leds.items()):
        led.on()
        sleep(speed)
        led.off()


def Clights():
    for _, led in reversed(leds.items()):
        led.on()
    sleep(speed)
    for _, led in reversed(leds.items()):
        led.off()
    sleep(speed)

cur = 1

def patterns():
    global cur
    if btn.is_pressed:
       cur += 1
    elif cur > 3:
       cur = 1

    if cur == 1:
        LtR()
    elif cur == 2:
        RtL()
    elif cur == 3:
        Clights()

    print(cur)
    


while True:   
    patterns()

