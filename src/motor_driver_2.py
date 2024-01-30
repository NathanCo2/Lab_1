"""!
<<<<<<< HEAD
@file motor_driver.py
=======
@file led.py
>>>>>>> 0bcf3ef0e6e15c3dcf0d1b9b12be0b45344a8963
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
<<<<<<< HEAD
=======

>>>>>>> 0bcf3ef0e6e15c3dcf0d1b9b12be0b45344a8963
import time
import pyb
import micropython

<<<<<<< HEAD
# Configure Pin A0 for output and timer (PWM2/1: Timer 2 and Channel 1)
pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
# Configure Pin PA10 (D2) for output to enable motor
en_pin = pyb.Pin(pyb.Pin.board.D2, pyb.Pin.OUT_PP)
# Configure Pin PB4 (D5) for output 
in1pin = pyb.Pin(pyb.Pin.board.D5, pyb.Pin.OUT_PP)
# Configure Pin PB5 (D4) for output 
in2pin = pyb.Pin(pyb.Pin.board.D4, pyb.Pin.OUT_PP)

=======
>>>>>>> 0bcf3ef0e6e15c3dcf0d1b9b12be0b45344a8963
class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    
    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        print ("Creating a motor driver")
<<<<<<< HEAD
        
        
        self.timer = timer  # Timer 2, frequency 1000Hz
        
=======
        en_pin = 
        self.timer = timer  # Timer 2, frequency 1000Hz
        self.en_pin = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
>>>>>>> 0bcf3ef0e6e15c3dcf0d1b9b12be0b45344a8963

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")
        # The microcontroller controls pins ENA, IN1A, and IN2A. A common way of using these pins is to set ENA high
        # to enable the motor, set IN1A low, and send a PWM signal to IN2A to power the motor in one direction
        # reverse the signals to IN1A and IN2A to power the motor in the other direction. 
        
        
 
# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program       
if __name__ == "__main__":
    moe = MotorDriver (a_pin, another_pin, a_timer)
    moe.set_duty_cycle (-42)