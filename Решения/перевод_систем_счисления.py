def convert(number, base):
    digits = '0123456789ABCDEFGHIJKLMNOP'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result
