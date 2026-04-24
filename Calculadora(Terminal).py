import os

while True:
    a = input ("Digite um número: ")
    b = input ("Digite outro número: ")
    operador = input ("Digite um operador (+-/*): ")
    numeros_validos = None

    try:
        a_float = float(a)
        b_float = float(b)
        numeros_validos = True

        operadores_validos = "+-/*"

        if len(operador) > 1:
            print("Por favor, insira apenas um operador.")
            continue
        
        if operador not in operadores_validos:
            print ('Operador inválido.')
            continue
        
        print (" ")
        print (" ")
        print ("Realizando sua conta, confira o resultado abaixo:")
        print (" ")
        print (" ")
        print (" ")
        print (" ")


        
        if operador == "+":
            print (f'{a_float} + {b_float} = {a_float+b_float}')
        if operador == "-":
            print (f'{a_float} - {b_float} = {a_float-b_float}')
        if operador == "/":
            print (f'{a_float}/{b_float} = {a_float/b_float}')
        if operador == "*":
            print (f'{a_float} x {b_float} = {a_float*b_float}')

        sair = input ("Deseja sair[s]? ").lower().startswith("s")
        
        if sair == False:
            os.system("cls" if os.name == "nt" else "clear")
            continue
        

        if sair == True:
            os.system("cls" if os.name == "nt" else "clear")
            print ('Você saiu, até mais!')
            break
            
            
        
    except:
        numeros_validos = None
        print ("Você inseriu um ou mais números inválidos.")

        sair = input ("Deseja sair[s]? ").lower().startswith("s")
        
        if sair == False:
            os.system("cls" if os.name == "nt" else "clear")
            continue
        

        if sair == True:
            os.system("cls" if os.name == "nt" else "clear")
            print ('Você saiu, até mais!')
            break

    

    