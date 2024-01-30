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
        
        self.timer = timer  # Timer 2, frequency 1000Hz
        self.en_pin = 

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