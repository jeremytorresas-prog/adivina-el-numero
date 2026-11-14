
import random
secreto = random.randint(1, 100)
intentos = 0

while True:
    numero = int (input("Adivina el número: "))
    intentos += 1

    if numero == secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    elif intentos >= 7:
        print(f"Perdiste, el número secreto era {secreto}.")
        break
    elif numero < secreto:
        print("Muy bajo")
    else:   
        print("Muy alto")