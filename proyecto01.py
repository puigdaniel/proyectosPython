#Hacer un juego que permita adivinar un numero al azar
import random

intentos = 0

print("Hola: ¿como se llama usted?: ")
nombre = input()

numero = random.randint(1, 300)
print("Bueno:  "+ nombre + " estoy pensando en un numero entre 1 y 300: ")
i = 0
while i < 6:
	print("Atenti intenta adivinar: ")
	estimacion = input()
	estimacion = int(estimacion)
	intentos = intentos + 1
	
	if estimacion < numero:
		print("Tu estimacion es muy baja:")
		
	if estimacion > numero:
		print("Tu estimacion es muy alta")
		
	if estimacion == numero:
		break
	
	if estimacion == numero:
		intentos = str(intentos)
		print("Has ganado: " + nombre + "has adivinado en: " + intentos)
		
	if estimacion != numero:
		numero = str(numero)
		print("Has perdido brother, el numero que estabas pensando era: " + numero)
	break