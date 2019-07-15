from gpiozero import LED, Button
from signal import pause
from gpiozero import Buzzer

led = LED(17)
bz = Buzzer(27)
button = Button(2)

button.when_presse = led.on
button.when_pressed = bz.on
button.when_release = led.off
button.when_released = bz.off

pause()