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

def led_setup(): 
    """!
    Doxygen style docstring for interrupt callback function
    """
    val = adcpin.read()
    int_queue.put(val)# Puts an integer into the queue
    
def led_brightness(): 
    """!
    Doxygen style docstring for interrupt callback function
    """
    val = adcpin.read()
    int_queue.put(val)# Puts an integer into the queue


if __name__ == "__main__":
    step_response(timer_int)
