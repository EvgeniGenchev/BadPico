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
    
    if cmd.startswith("STRING"):
        return [cmd.split(" ")[0]], " ".join(cmd.split(" ")[1:])

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
    
    if "CAPS_LOCK" == cmd or "CAPSLOCK" == cmd:
        keyboard.press(Keycode.CAPS_LOCK)
        keyboard.release(Keycode.CAPS_LOCK)
        
    for cm in cmd:
        if "F1" == cmd:
            keyboard.press(Keyboard.F1)

        if "F2" == cmd:
            keyboard.press(Keyboard.F2)
        
        if "F3" == cmd:
            keyboard.press(Keyboard.F3)
        
        if "F4" == cmd:
            keyboard.press(Keyboard.F4)
        
        if "F5" == cmd:
            keyboard.press(Keyboard.F5)
        
        if "F6" == cmd:
            keyboard.press(Keyboard.F6)
        
        if "F7" == cmd:
            keyboard.press(Keyboard.F7)
        
        if "F8" == cmd:
            keyboard.press(Keyboard.F8)
        
        if "F9" == cmd:
            keyboard.press(Keyboard.F9)
        
        if "F10" == cmd:
            keyboard.press(Keyboard.F10)
        
        if "F11" == cmd:
            keyboard.press(Keyboard.F11)
        
        if "F12" == cmd:
            keyboard.press(Keyboard.F12)

        if "BREAK" == cmd or "PAUSE" == cmd:
            keyboard.press(Keyboard.PAUSE)

        if "DELETE" == cmd or "DEL" == cmd:
            keyboard.press(Keyboard.DELETE)
        
        if "END" == cmd: 
            keyboard.press(Keyboard.END)

        if "HOME" == cm:
            keyboard.press(Keycode.HOME)
        
        if "NUMLOCK" == cm:
            keyboard.press(Keycode.KEYPAD_NUMLOCK)

        if "PAGEUP" == cm:
            keyboard.press(Keycode.PAGE_UP)
        
        if "PAGEDOWN" == cm:
            keyboard.press(Keycode.PAGE_DOWN)

        if "PRINTSCREEN" == cm:
            keyboard.press(Keycode.PRINT_SCREEN)

        if "SCROLLOCK" == cm:
            keyboard.press(Keycode.SCROLL_LOCK)

        if "SPACE" == cm or "SPC" == cm:
            keyboard.press(Keycode.SPACEBAR)

        if "TAB" == cm:
            keyboard.press(Keycode.TAB)

        if "GUI" == cm or "WINDOWS" == cm:
            keyboard.press(Keycode.GUI)
            write(args)
            
        if "ALT" == cm or "OPTION" == cm:
            keyboard.press(Keycode.ALT)
            write(args)
        
        if "INSERT" == cm or "INS" == cm:
            keyboard.press(Keycode.INSERT)
            write(args)
            
        if "ESC" == cm or "ESCAPE" == cm:
            keyboard.press(Keycode.ESCAPE)
        
        if "CTRL" == cm or "CONTROL" == cm:
            keyboard.press(Keycode.CONTROL)
            write(args)
        
        if "SHIFT" == cm:
            keyboard.press(Keycode.SHIFT)
            write(args)
        
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
