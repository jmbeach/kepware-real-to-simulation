"""Normal register module"""
import register

class RegularRegister(register.Register):
    """Represents a normal register
    Between R0000 - R9999.
    Each address is a byte on an 8-bit device and a word on a 16-bit
    device.
    To get a bit, you specify RXXXX.Y on an 8-bit device
    and RXXXX.YY on a 16-bit device.
    Can be data type Word, Short, BCD,
    DWord, Long, LBCD, Float, LLong, QWord,
    Double, Date, Boolean"""

    def __init__(self, is_16bit):
        register.Register.__init__(self, is_16bit, "R0000")