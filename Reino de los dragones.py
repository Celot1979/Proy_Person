import random
import time
def mostrarIntroduccion():
	print(" Estás en un tierra llena de dragones.Frente a ti ")
	time.sleep(3)
	print(" hay 2 cuevas. Es una de ellas, el dragón es generoso y")
	time.sleep(3)
	print(" amigable y compartirá su tesero contigo.El otro dragón")
	time.sleep(3)
	print(" es codiciso y está hambriento, y te devorará inmediatamente")
	time.sleep(3)
	print()
def elegirCueva():
	cueva = ""
	while cueva != "1" and cueva != "2":
		print("A qué cueva quieres entrar? (1 o 2) ")
		cueva = input()
	return cueva
def explorarCueva(cuevaElegida):
	print("Te aproximas a la cueva..")
	time.sleep(3)
	print("Es oscura y espeluznante...")
	time.sleep(3)
	print("Un gran dragón aparece súbitamente frente a ti\n Abre sus fauces y ..")
	print()
	time.sleep(3)
	cuevaAmigable = random.randint(1,2)
	if cuevaElegida == str(cuevaAmigable):
		print(" Te regala un tesoro")
	else:
		print(" Te engulle de un bocado!!!")
jugarDeNuevo = "si" 
while jugarDeNuevo == "si" or jugarDeNuevo == "SI":
	mostrarIntroduccion()
	numeroDeCueva = elegirCueva()
	explorarCueva(numeroDeCueva)
	print("¿ Quieres jugar de nuevo? (Si o No)")
	jugarDeNuevo = input()
