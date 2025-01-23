n1=int(input("Introduce el primer número "))
n2=int(input("Introduce el primer número "))
n3=int(input("Introduce el primer número "))
if n1 > n2 and n1 > n3:
    print("El número", n1, "es el mayor")
elif n2 > n1 and n2 > n3:
    print("El número", n2, "es el mayor")
elif n3 > n1 and n3 > n2:
    print("El número", n3, "es el mayor")
elif n1 == n2 and n1 == n3:
    print("El número", n1, "es igual que")
elif n2 == n1 and n2 == n3:
    print("El número", n2, "es igual que")
elif n3 == n1 and n3 == n2:
    print("El número", n3, "es igual que")

