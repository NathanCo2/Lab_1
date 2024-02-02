"""!
@file led.py
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

import pyb

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin: Pin for enabling the motor driver
        @param in1pin: Pin for controlling direction 1
        @param in2pin: Pin for controlling direction 2
        @param timer: Timer object for generating PWM signals
        """
        print ("Creating a motor driver")
        self.en_pin = en_pin
        self.timer = timer
        self.IN1A = timer.channel(1, pyb.Timer.PWM, in1pin) #sets up ch 1 for PWM mode on in1pin
        self.IN2A = timer.channel(2, pyb.Timer.PWM, in2pin) #sets up ch 2 for PWM mode on in2pin
        self.en_pin.high()
        self.IN1A.low()
        self.IN2A.pulse_width_percent(50)
        

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
    # set up timer 3
    TIM3 = pyb.Timer(3, freq=1000) # Timer 3, frequency 1000Hz
    # Define pin assignments
    ENA = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    IN1A = pyb.Pin(pyb.Pin.board.PB4)
    IN2A = pyb.Pin(pyb.Pin.board.PB)
    
    # Create motor drivers
    moe = MotorDriver(ENA, IN1A, IN2A, TIM3)
    moe.set_duty_cycle(-42)