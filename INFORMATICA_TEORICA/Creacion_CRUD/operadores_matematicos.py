# Operaciones matemáticas
def operaciones_matematicas(a, b):
    print(f"Números: {a} y {b}")
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b)  # División normal
    print("División entera:", a // b)  # División entera
    print("Residuo:", a % b)  # Módulo (residuo de la división)
    print("Potencia:", a ** b)  # Potencia

# Solicitar dos números al usuario
try:
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    operaciones_matematicas(num1, num2)
except ValueError:
    print("Por favor, ingresa numeros validos.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero en la division o el residuo.")
