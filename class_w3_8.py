# Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'

class Script_8():

    def reverse(self, s):
        if len(s) == 1:
            return s
        else:
            return s[-1] + self.reverse(s[:-1])


op1 = Script_8()
print(op1.reverse("Murcielago"))
