def string_work(num):
    #Verifica si el parametro es un string
    if type(num) == str:
        newstring = ''
        for a in num:
            '#Verifica si el caracter es un letra mayúscula'
            if (a.isupper()) is True:


                
                newstring += (a.lower())

            elif (a.islower()) is True:

                newstring += (a.upper())

            elif (a.islower()) is False and (a.isupper()) == False:
                newstring = ''
                print(506)
                break
        print(newstring)
    else:
        print(505)