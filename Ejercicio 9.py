import random
numero = random.randint(1, 50)

for __ in range(4):
    adivina=int(input("Adivina el número (del 1 al 50): "))
    if adivina == numero:
            print("¡Adivinaste el número!")
    elif adivina > numero:
            print("El número es menor")
    elif adivina < numero:
            print("El número es mayor")
