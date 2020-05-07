# ls8-emulator

The LS8 is a ficticious 8-bit microcomputer with 8-bit addressing, allowing for 256 bytes of RAM.

See the instruction set [specifications](LS8-spec.md) to get a better idea as to what this microcomputer can do.

## Notable features

-   Hardware stack using a stack pointer register. SP starts at 0xF3 and grows downward

-   Support for hardware interrupts (max of 8 interrupts) via dedicated interrupt status register, an interrupt mask register (to enable / disable servicing), and an IVT located in memory between the addresses of 0xF8 - 0xFF.

-   Dedicated 1 second timer interrupt built-in

-   Support for additional devices (through direct memory acces). Included in the python-app is a simplistic "keyboard" device. Reads terminal (non-blocking) and writes single chars to memory at address 0xF4

### Memory map:

```
      top of RAM
+-----------------------+
| FF  I7 vector         |    Interrupt vector table
| FE  I6 vector         |
| FD  I5 vector         |
| FC  I4 vector         |
| FB  I3 vector         |
| FA  I2 vector         |
| F9  I1 vector         |
| F8  I0 vector         |
| F7  Reserved          |
| F6  Reserved          |
| F5  Reserved          |
| F4  Key pressed       |    Holds the most recent key pressed on the keyboard
| F3  Start of Stack    |
| F2  [more stack]      |    Stack grows down
| ...                   |
| 01  [more program]    |
| 00  Program entry     |    Program loaded upward in memory starting at 0
+-----------------------+
    bottom of RAM
```
