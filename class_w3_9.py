class Script_9():
    def __init__(self):
        self.xstring = None

    def get_String(self):
        self.xstring = input("Intro a string: ")

    def print_string(self):

        if self.xstring is not None:
            print(self.xstring.upper())
        else:
            print("")


op1 = Script_9()
op1.get_String()
op1.print_string()
