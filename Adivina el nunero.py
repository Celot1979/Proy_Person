import random
intentosRealizados = 0
print("Hola! ¿ Cómo te llamas? ")
miNombre= input()
numero = random.randint(1,20)
print(" Bueno " + miNombre + " estoy pensando un numero entre 1 y 20 ")
print(" Escribe el número que piensas... ")
while intentosRealizados < 6:
	print(" Intenta adivinar ")
	estimacion = input()
	estimacion = int(estimacion)
	intentosRealizados = intentosRealizados + 1
	if estimacion < numero:
		print(" Tu estimacion es muy baja. ")
	elif estimacion > numero:
		print(" Tu estimacion es muy alta ")
	elif estimacion == numero:
		break
	
if estimacion == numero:
	intentosRealizados = str(intentosRealizados)
	print(" Buen trabajo " + miNombre + " has adivinado mi numero en " + intentosRealizados + " intentos ")
if estimacion != numero:
	numero = str(numero)
	print(" Pues no. El numero que estaba pensado era " + numero)
