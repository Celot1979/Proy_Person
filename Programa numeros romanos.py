print("********* P R O G R A M A   C O N V E R S O R *********")
print("-------------------------------------------------------")
print("** N U M E R O S   R O M A N O S   A   E N T E R O S **")
print("-------------------------------------------------------")
print("************************** Y **************************")
print("-------------------------------------------------------")
print("** N U M E R O S   E N T E R O S   A   R O M A N O S **")
print("-------------------------------------------------------")
print("**************  ¿ Qué deseas convertir ? ************** ")
p = input("************* números (ROMANOS) a enteros ************* \n************************** o "
          "************************** \n ************  (ENTEROS) a números romanos ************ \n ************ "
          "Si desea irse escriba (SALIR)************\n ****************** Escriba AQUI => : ")
while True:
    if p == "Enteros" or p == "enteros":
        entero = int(input ("¿Que numero entero desea convertir a numero romano?: "))
        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numeral = ""
        i = 0
        while entero > 0:
            for _ in range(entero // numeros[i]):
                numeral += romanos[i]
                entero -= numeros[i]
            i += 1

        print("EL NUMERO ENTERO QUE ACABA DE ESCRIBIR SERIA EN NUMEROS ROMANOS: ", numeral)

        p = input(" ¿Qué deseas convertir) \n números (ROMANOS) a enteros o (ENTEROS) a números romanos \n Si desea (Salir): ")
    elif p == "ROMANOS" or p == "romanos":
        entero = str(input("Recuerde que tiene que escribir  en letras mayusculas\n ¿ Que numero romano desa convertir a numero entero  ?:"))
        t = str(entero)
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ente = 0
        for i in range(len(t)):
            if i > 0 and rom[t[i]] > rom[t[i - 1]]:
                ente += rom[t[i]] - 2 * rom[t[i - 1]]
            else:
                ente += rom[t[i]]

            print("EL NUMERO ROMANO QUE ACABA DE ESCRIBIR SERÍA EN NUMEROS ENTEROS: ", ente)
        p = input(" ¿Qué deseas convertir) \n números (ROMANOS) a enteros o (ENTEROS) a números romanos \n Si desea (Salir): ")
    elif p == "SALIR" or p == "salir":
        exit()
    else:
        print("Revise los datos introduccidos, vuelva a escribirlos... Espero ....")
        p = input(" ¿Qué deseas convertir) \n números (ROMANOS) a enteros o (ENTEROS) a números romanos \n Si desea (Salir): ")










