# script que verifica si un string comformado por [],{} y () cierra
# apropiadamente

def verificador(str_input):
    i = 0
    contenedor = ""
    result = True
    while len(str_input) != 0 or i == len(str_input):
        print(str_input)

        if len(str_input)== 1:
            result= False
            break

        if len(str_input) == 2:
            if contenedor == "":
                if str_input not in ('()', '[]', '{}'):
                    result = False
                    break
                else:
                    str_input = contenedor + str_input
                    contenedor = ""
                    i = 0

        if (str_input[0] + str_input[1]) in ('()', '[]', '{}'):
            str_input = contenedor + str_input[2:]
            contenedor = ''
            i = i + 1
        else:
            contenedor = contenedor + str_input[0]
            str_input = str_input[1:]
            i = 0

    print(result)

if __name__ == "__main__":
    verificador('(({))')
