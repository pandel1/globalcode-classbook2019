from gpiozero import Buzzer

bz = Buzzer(17)
bz.on()
bz.beep(on_time=1,off_time=1, n=None,background=True)
