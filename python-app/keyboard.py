"""
Keyboard

1. Has access to CPU instance so it can call an interrupt, access memory (DMA)
2. Runs in its own thread to allow for simultaneous execution of CPU cycle and keyboard polling loop
"""

import sys
import threading
from time import sleep


class Keyboard:
    def __init__(self, ls8):
        # Get access to ls8 as a 'peripheral'
        self.ls8 = ls8
        # Interrupt bit of this device
        self.interrupt_bit = 1
        # Create keyboard polling thread
        self._keyboard_thread = threading.Thread(target=self._poll)
        # Making thread a daemon will allow for auto cleanup on main program exit
        self._keyboard_thread.daemon = True

    def connect(self):
        # Start thread
        self._keyboard_thread.start()

    def _poll(self):
        # Enter keyboard polling loop
        while True:
            char = sys.stdin.read(1)  # Read one byte (char)
            if char:
                # Set char in memory as an int byte
                self.ls8.ram[0xF4] = ord(char)
                # Raise keyboard interrupt
                self.ls8.raise_interrupt(self.interrupt_bit)

            # Sleep 50 ms to keep cpu usage down
            # Technically this makes it poll the keyboard at 20hz
            sleep(0.05)
