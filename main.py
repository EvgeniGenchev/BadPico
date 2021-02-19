import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


def_delay = 0
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def write(args):
    if args:
        layout.write(args)
    
def get_args(cmd):
    
    cm   = []
    args = []
    
    for s in cmd.split(" "):
        if s.isupper():
            cm.append(s)
        else:
            args.append(s)
            
    return cm, " ".join(args)

def command(cmd):
    global def_delay
    cmd, args = get_args(cmd)
    time.sleep(def_delay)
    cm0 = cmd[0]
    
    if "DEFAULT_DELAY" == cm0 or "DEFAULTDELAY" == cm0:
        def_delay = int(args)
    
    if "DELAY" == cm0:
        time.sleep(int(args) / 1000)
        
    if "STRING" == cm0:
        layout.write(args)
    
    if "CAPS_LOCK" == cmd:
        keyboard.press(Keycode.CAPS_LOCK)
        keyboard.release(Keycode.CAPS_LOCK)
        
    for cm in cmd:
        print(cm)
        if "GUI" == cm or "WINDOWS" == cm:
            keyboard.press(Keycode.GUI)
            write(args)
            
        if "ALT" == cm or "OPTION" == cm:
            keyboard.press(Keycode.ALT)
            write(args)
            
        if "ESC" == cm or "ESCAPE" == cm:
            keyboard.press(Keycode.ESCAPE)
        
        if "CTRL" == cm or "CONTROL" == cm:
            keyboard.press(Keycode.CONTROL)
            write(args)
        
        if "SHIFT" == cm:
            keyboard.press(Keycode.SHIDT)
        
                
        if "MENU" == cm or "APP" == cm:
            keyboard.press(Keycode.APPLICATION)
        
    if "ENTER" in cmd:
            keyboard.press(Keycode.ENTER)
            keyboard.release_all()
        
    keyboard.release_all()
           
try:           
    with open('script.txt', 'r') as file:
        for line in file:
            command(line.rstrip())
except:
    keyboard.release_all()