# Faysal_SSD1306 (under development)

A lightweight MicroPython driver for **SSD1306 OLED displays** (128x32 and 128x64, I2C interface).  
Author: **Faysal Mahmud**  
GitHub: [FaysalMahmudSajan](https://github.com/FaysalMahmudSajan/)

---

##  Features
- Compatible with **SSD1306 OLED 128x32 and 128x64** modules
- Supports **I2C communication**
- Core display functions:
  - `fill(color)` → Fill entire screen with black/white
  - `pixel(x, y, color)` → Draw individual pixels
  - `text(string, x, y, color)` → Draw text
  - `show()` → Update display with buffer contents
- Extra features:
  - `invert()` → Invert display colors
  - `poweron()` / `poweroff()` → Control display power
  - `contrast(value)` → Adjust brightness
  - `scroll(start, stop)` → Enable horizontal scrolling
  - `stop_scroll()` → Stop scrolling

---

##  Requirements
- MicroPython board (ESP8266, ESP32, Raspberry Pi Pico, etc.)
- SSD1306 OLED display (I2C, address default `0x3C`)
- `framebuf` module (built-in with MicroPython)

---

##  Usage Example

```python
from machine import Pin, I2C
from Faysal_SSD1306 import Faysal_SSD1306

# Initialize I2C (adjust pins for your board)
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Initialize OLED (128x64)
oled = Faysal_SSD1306(128, 64, i2c)

# Draw text
oled.text("Hello Faysal!", 0, 0)
oled.show()

# Draw pixel
oled.pixel(10, 10, 1)
oled.show()

# Invert display
oled.invert(True)
