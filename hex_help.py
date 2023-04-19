# File: 
# Author: Michael du Preez
#

# --------- Imports
import enums
import string
import math
from tabulate import tabulate

# --------- Globals / Config
g_word_size_bits = enums.Word_size._32_BITS
g_endianness = enums.Endianness.LITTLE


display_format =""
 
# --------- Functions
def invert_endianness(x):
    return int.from_bytes(x.to_bytes(int(g_word_size_bits.value[0]/8), byteorder='little'), byteorder='big', signed=False)

def set_display_format(format_specifier : str):
    global display_format
    number_of_display_bits = 0

    if(format_specifier == enums.Base._2.value[2]):
        number_of_display_bits = int(g_word_size_bits.value[1]) * 4
    
    else:
        number_of_display_bits = int(g_word_size_bits.value[1])    

    display_format = '{:' + str(number_of_display_bits) + format_specifier +'}'
 
def invert_bits(number :int , include_leading_zeros :bool) -> int:
    # Minimum number of bits required to express number
    number_of_bits = int(math.log2(number)) + 1
    
    if(include_leading_zeros == True):
        if(number_of_bits <= g_word_size_bits.value[0]):
            number_of_bits = g_word_size_bits.value[0]
        else:
            number_of_bits = math.ceil(g_word_size_bits.value[0] / number_of_bits) * g_word_size_bits.value[0]

    # Inverting the bits one by one
    for index in range(number_of_bits):
        number = (number ^ (1 << index))
     
    return number

def get_base_of_input_string(input_string_number:str) -> enums.Base:
    _base = enums.Base._10

    if(len(input_string_number) > 2):
        _prefix = input_string_number[:2]

        if(_prefix[1:] in string.ascii_letters):
            for base_prexif_enum in enums.Base:
                base_prexif = base_prexif_enum.value[0]

                if base_prexif == _prefix.lower():
                    _base = base_prexif_enum
                    break
    return _base

# --------- Program Operations

print("Welcome to Hex Help!")
print("valid prefixe(s):\n\
    0b = binary (Base 2)\n\
    0o = binary (Base 8)\n\
    0x = hexidecimal (Base 16)\n\
    no_prefix = decimal (Base 10)")
user_value = input("Please insert your value for assistance:\n")

try:
    user_value = user_value.replace(" ","")
    decimal_value = eval(user_value)
    input_base = get_base_of_input_string(user_value)
    print("Displaying all results in {}\n".format(str(input_base)))
    if(input_base != enums.Base._10):
        length_of_input = len(user_value) - 2
    else:
        length_of_input = len(user_value)
except Exception as e:
    print("Error interpretting your input: {}".format(str(e)))

set_display_format(input_base.value[2])
# invert_bits(decimal_value, True)

no_leading_zeros_flipped = invert_bits(decimal_value, False)
leading_zeros_flipped = invert_bits(decimal_value, True)
# print("Bit Flip:")

# print("Math Without leading zeros: " + display_format.format(no_leading_zeros_flipped).strip())
# print("Math With leading zeros:" + display_format.format(leading_zeros_flipped).strip())
# print(display_format.format((decimal_value)))
# print(display_format.format(invert_endianness(decimal_value)))

display_array = []
row_array = []

row_array.append("Original")
row_array.append(display_format.format(decimal_value))
row_array.append(display_format.format(no_leading_zeros_flipped).strip())
row_array.append(display_format.format(leading_zeros_flipped).strip())

display_array.append(row_array)

row_array = []
row_array.append("Endian Swap")
row_array.append(display_format.format(invert_endianness(decimal_value)))
row_array.append(display_format.format(invert_endianness(no_leading_zeros_flipped)).strip())
row_array.append(display_format.format(invert_endianness(leading_zeros_flipped)).strip())

display_array.append(row_array)

print (tabulate(display_array, headers=["","Endian", "No-Zeros BitFlip", "Zeros BitFlip"]))
print()