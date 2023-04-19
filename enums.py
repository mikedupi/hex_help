from enum import Enum

class Endianness(Enum):
    LITTLE = 0
    BIG = 1

class Word_size(Enum):
    _8_BITS = [8,'02']
    _16_BITS = [16,'04']
    _24_BITS = [24,'06']
    _32_BITS = [32,'08']
    _64_BITS = [64,'16']

class Base(Enum):
    _2 = ['0b',2 ,'b']
    _8 = ['0o',8 , 'o']
    _10 = ['',10 , 'd']
    _16 = ['0x',16 , 'X']