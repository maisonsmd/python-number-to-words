words_below_21 = {
    1: "one",    2: "two",    3: "three",    4: "four",    5: "five",
    6: "six",    7: "seven",    8: "eight",    9: "nine",    10: "ten",    11: "eleven",
    12: "twelve",    13: "thirteen",    14: "fourteen",    15: "fifteen",    16: "sixteen",
    17: "seventeen",    18: "eighteen",    19: "nineteen"
}

words_multiple = {
    20: "twenty",    30: "thirty",    40: "fourty",    50: "fifty",
    60: "sixty",    70: "seventy",    80: "eighty",    90: "ninety"
}

# https://en.wikipedia.org/wiki/Names_of_large_numbers for morpythe
words_thousands_power = {
    1e0: "",
    1e3: "thousand",    1e6: "million",   1e9: "billion", 
    1e12: "trilion",    1e15: "quadrillion", 1e18: "quintillion",
    1e21: "sextillion", 1e24: "septillion", 1e27: "octillion",
}

def hundreds_to_words(num):
    # eg: num = 345
    hundreds = int(num / 100)       # 3
    tens = int(int(num % 100) / 10) # 4
    unit = int(num % 10)            # 5

    tens_and_unit = num % 100       # 45

    result = ""

    if hundreds > 0:
        result += words_below_20[hundreds] + " hundred"

    if tens == 0:
        if unit > 0:
            result += " " + words_below_20[unit]
    elif tens_and_unit < 20:
        result += " " + words_below_20[tens_and_unit]
    else:
        result += " " + words_multiple[tens * 10]
        if unit > 0:
            result += "-" + words_below_20[unit]

    return result

def num_to_words(num):
    num = int(num)
    result = ""
    is_negative = num < 0
    num = abs(num)
    
    if num == 0:
        return "zero"

    # convert number to list of digits, eg: 1234 => [1,2,3,4]
    digits = list(map(lambda x: int(x), list(str(num))))
    # number of digits of num
    n_digits = len(digits)
    
    # split number into 3-digits chunks
    for i in range(3, 3 + n_digits, 3):
        # what power of 10 the current digit is
        power = (10**(i))
        # get the hundreds number, eg: 123456 => 123, thousand
        hundreds_splited = int((num % power) / (power / 1000))
        result = (hundreds_to_words(hundreds_splited) + " " + words_thousands_power[power / 1000] + " ") + result
        
    if is_negative:
        result = "negative " + result

    return " ".join(result.split())

def test(number):
    print('{:,}: "{}"'.format(number, num_to_words(number)))

def main():
    test(0)
    test(-1)
    test(100001)
    test(12)
    test(123)
    test(1234)
    test(12345)
    test(123456)
    test(1233234567)
    test(12345678)
    test(123456789)
    test(1234567890)
    test(12345678901)
    test(123456789012)
    test(1234567890123)
    test(12345678901234)

if __name__ == "__main__":
    main()
