from math import sqrt

def CalcularBhaskara(a, b, c):
    if a != 0:
        delta = (b ** 2) - 4 * a * c
        if delta >= 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            print(delta)
            print(f"({x1:.2f}, {x2:.2f})")
        else:
            print("Impossivel realizar o calculo pois delta é negativo.")
    else:
        print("Impossivel realizar o calculo pois a é 0.")
