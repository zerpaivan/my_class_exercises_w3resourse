# Write a Python class to convert a roman numeral to an integer

class Convert():

    def __init__(self, roman_num):
        self.roman_num = roman_num

    def roman_to_int(self):
        dict_int_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                          'M': 1000}
        int_num = 0

        for n in range(len(self.roman_num) - 1):

            if dict_int_roman[self.roman_num[n]] >= dict_int_roman[self.roman_num[n + 1]]:
                int_num = int_num + dict_int_roman[self.roman_num[n]]
            else:
                int_num = int_num - dict_int_roman[self.roman_num[n]]

        int_num = int_num + dict_int_roman[self.roman_num[-1]]
        print(int_num)


int_num1 = Convert("IX")
int_num1.roman_to_int()
