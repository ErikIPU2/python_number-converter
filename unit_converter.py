symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


# convert any decimal number to any base, only works with base-2 up to base-36 (all alphabetical letters)
# if you add more symbols in the symbols tuple, more available bases are added too
def integer_decimal_to_any_base(number, base):
    result = ""
    while not number == 0:
        result = result + symbols[number % base]
        number = number // base
    # reverse the result to be correct
    result = result[::-1]
    return result
