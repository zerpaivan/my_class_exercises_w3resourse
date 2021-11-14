# Write a Python class to convert an integer to a roman numeral

class Convert():
    def __init__(self, num):
        self.num = num

    def int_to_roman(self):
        dict_int_roman = {1: 'I', 4: "IV", 5: 'V', 9: 'IX', 10: 'X',
                          40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                          500: 'D', 900: 'CM', 1000: 'M'}
        roman_num = ""
        while self.num > 0:
            if self.num in dict_int_roman:
                roman_num = roman_num + dict_int_roman[self.num]
                self.num = 0
            else:
                temp_num = 1
                for key_int in dict_int_roman:
                    if key_int < self.num:
                        temp_num = key_int
                    else:
                        roman_num = roman_num + dict_int_roman[temp_num]
                        self.num = self.num - temp_num
                        break

        print(roman_num)


roman1 = Convert(105)
roman1.int_to_roman()
