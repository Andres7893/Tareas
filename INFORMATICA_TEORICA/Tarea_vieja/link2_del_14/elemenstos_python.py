import random

def main():
    """Ingresa el límite superior e inferior de un rango de números
    y permite al usuario adivinar el número aleatorio hasta que acierte.
    """
    limite_inferior = int(input("Ingresa el número menor del rango: "))
    limite_superior = int(input("Ingresa el número mayor del rango: "))
    numero_secreto = random.randint(limite_inferior, limite_superior)
    intentos = 0

    while True:
        intentos += 1
        numero_usuario = int(input("Ingresa un numero para tratar de adivinar: "))

        if numero_usuario > numero_secreto:
            print("Intenta con un número más alto:")
        elif numero_usuario > numero_secreto:
            print("Intenta con un número más bajo:")
        else:
            print(f"¡Ganaste! Te tomó {intentos} intentos")
            break

if __name__ == "__main__":
    main()