"""!
@file step_response.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-01-30 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""
import time
import pyb
import micropython

# Initialize pins/ADC Objects (aka initialize pins)
    # Configure Pin A0 for output
pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
    # Configure PWM3/2 for timer (Timer 3 and Channel 2)
pin32 = pyb.Pin(pyb.Pin.board.D4, pyb.Pin.OUT_PP)

def led_setup(): 
    """!
    Sets up LED
    """
    tim_num = pyb.Timer.PWM_INVERTED(2) #Creates a timer 
    tim_num.init(freq=1000) #Starts the timer
    #ch.pulse_width_percent(50)
    

def led_brightness(): 
    """!
    Doxygen style docstring for interrupt callback function
    """
    while True:
        time.sleep(0.5)
        pinA0.low()
        time.sleep(0.5)
        pinA0.high()

    
# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":
    led_brightness(led_setup)
    
    #pinA0 = led_setup()

