# BadPico 👹

Ducky script emulator running on Raspberry Pi Pico.
Written in Circuit Python 🐍
  
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![CircuitPython](https://img.shields.io/badge/CircuitPython-6.3-9cf)](https://circuitpython.org/board/raspberry_pi_pico/)

## Requirements 

[CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) <br>
[Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)

## Setup

1. Install CicuitPython like [so](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

2. Install the Adafruit_CircuitPython_HID libraries.(You can use [minipip](https://github.com/aivarannamaa/minipip) or install by IDE like Thonny)

3. clone this repository and upload the code

- on Windows (ampy)
```bash
$ pip install adafruit-ampy 
$ git clone https://github.com/EvgeniGenchev/BadPico
$ cd BadPico 
$ rename main.py code.py
$ ampy --port COM<device_number> put code.py
```

- on Linux (ampy)
```bash
$ sudo pip3 install adafruit-ampy 
$ git clone https://github.com/EvgeniGenchev/BadPico
$ cd BadPico 
$ mv main.py code.py
$ sudo ampy --port /dev/<device_name> put code.py
```

 ## Usage
 Create a file `script.txt` with your ducky script on it and upload it to the RaspberryPi Pico
 ```bash
 # Linux
 $ sudo ampy --port /dev/<device_name> put script.txt
 # Windows
 $ ampy --port COM<device_number> put script.txt
 ```
 
 ## Supported commands
 - DEFAULT_DELAY \ DEFAULTDELAY
 - DELAY
 - STRING 
 - CAPS_LOCK \ CAPSLOCK
 - BREAK \ PAUSE
 - F1, F2 ..., F12
 - DELETE \ DEL
 - END
 - HOME
 - NUMLOCK
 - PAGEUP, PAGEDOWN, PRINTSCREEN
 - SCROLLOCK
 - SPACE \ SPC
 - TAB
 - GUI \ WINDOWS
 - ALT \ OPTION
 - INSERT \ INS
 - ESCAPR \ ESC
 - CTRL \ CONTROL
 - SHIFT 
 - MENU \ APP
 - ENTER
 
 ## What to expect
 - Support for loops
 
 
 
