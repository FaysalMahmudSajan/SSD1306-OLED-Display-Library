from machine import Pin, I2C
from  Faysal_SSD1306 import Faysal_SSD1306
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = Faysal_SSD1306(128, 64, i2c)  

oled.fill(0)
oled.text("Hello Faisal!", 0, 0)
oled.text("OLED Ready", 0, 16)
oled.show()

time.sleep(2)
oled.invert(True)
time.sleep(1)
oled.invert(False)

oled.scroll()
time.sleep(3)
oled.stop_scroll()

