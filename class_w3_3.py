# Write a Python class to find validity of a string of parentheses,
# '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct
# order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
# are invalid

from verificador import verificador


class Test():

    def comprobar(self, str_input):
        verificador(str_input)


result = Test()
result.comprobar("([]][")
