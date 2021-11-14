# Write a Python class to find validity of a string of parentheses,
# '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct
# order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
# are invalid

class Test():

    def parenthese(self, str_input):
        container = []
        pchar = {"(": ")", "[": "]", "{": "}"}

        for character in str_input:
            if character in pchar:
                container.append(character)
            elif len(container) == 0 or pchar[container.pop()] != character:
                return False

        return len(container) == 0


print(Test().parenthese('([{}])'))
