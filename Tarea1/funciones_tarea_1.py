def num_to_str(num):
    '#Verifica si el parametro es un integer'
    if type(num) != int:
        print(101)
    else:
        '#se crea un diccionario para las posibles'
        '#combinaciones para la salida'
        d = {0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco',
                6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez',
                11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce',
                15: 'quince', 16: 'dieciseis', 17: 'diecisiete',
                18: 'dieciocho', 19: 'diecinueve', 20: 'veinte',
                30: 'treinta', 40: 'cuarenta', 50: 'cincuenta',
                60: 'sesenta', 70: 'setenta', 80: 'ochenta',
                90: 'noventa'}

        '#Verifica si el parametro es negativo'
        if(0 > num):
            print(102)
        else:
            '#Verifica si el parametro es menor a 20 para'
            '#utilizar el nombre completo'
            if (num < 20):
                return d[num]

            '#Verifica si el parametro es menor a 100 para'
            '#separar el numero y mostrar los nombres de'
            'las centenas y decenas'
            if (num < 100):
                '#Verifica si el parametro es un multiplo'
                '#de 10 para mostrar su nombre'
                if num % 10 == 0:
                    return d[num]
                else:
                    '#se retorna el número en centenas'
                    '# y decenas'
                    return d[num // 10 * 10] + '_'+'y'+'_' + d[num % 10]
            '#Verifica si el parametro es mayor a 99'
            if (num > 99):
                print(103)


def string_work(num):
    '#Verifica si el parametro es un string'
    if type(num) == str:
        newstring = ''
        for a in num:
            '#Verifica si el caracter es un letra mayúscula'
            if (a.isupper()) is True:
                newstring += (a.lower())
                '#Covierte el caracter a letra minúscula'

            elif (a.islower()) is True:
                '#Verifica si el caracter es un letra minúscula'

                newstring += (a.upper())
                '#Covierte el caracter a letra mayúscula'

            elif (a.islower()) is False and (a.isupper()) is False:
                '#Verifica si el parametro contiene algún número o símbolo en'
                '#el string'
                newstring = ''
                print(506)
                break
        print(newstring)
    else:
        print(505)


'#Errores'
'#101: El párametro no es un integer'
'#102: El párametro es un número decimal o negativo'
'#103: El párametro es un número mayor a 99'
'#505: El párametro no es un string'
'#506: El string contiene un número o símbolo'
