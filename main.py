from machine import Pin
import time

int_blue_led = Pin(2, Pin.OUT)
print(int_blue_led.value())

while True:
    int_blue_led.value(1)
    time.sleep(2)
    int_blue_led.value(0)
    time.sleep(2)