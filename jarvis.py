__author__ = 'Vale Tolpegin & Matthew Nguyen'

# NOTE: Currently, only CLI will be implemented so STT engines and other class initialization will not be required

# Throughout the code in the main program, the following needs to be accomplished:
# 1: Initialize brain and other classes. This will allow JARVIS to interpret commands and access STT associated functions
# 2: In an infinite loop:
#   a: Get user input
#   b: Parse that user input for set commands such as shutdown, restart, etc
#   c: Compare that input to previous input/database of phrases and words and apply learning logic (see logic_basic_learning.txt)

import sys
import subprocess
import os

from brain import Brain


class jarvis:
    """ This is the main class for JARVIS """

    global jarvis_brain


    def __init__( self, *args, **kwargs ):
        global jarvis_brain

        jarvis_brain = Brain()


    def run( self ):
        """ This method will handle getting input and relaying that input to JARVIS' brain """

        global jarvis_brain

        while True:
            command = raw_input( "COMMAND: " )

            jarvis_brain.test_incoming_command( command )


if __name__ == '__main__':
    jarvis_main = jarvis()

    jarvis_main.run()