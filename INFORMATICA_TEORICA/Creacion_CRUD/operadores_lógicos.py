# Operadores lógicos

# Pedimos al usuario que ingrese dos valores booleanos
print("Ingrese dos valores booleanos (Verdadero o Falso):")
a = input("Valor para A: ").strip().capitalize() == "Verdadero"
b = input("Valor para B: ").strip().capitalize() == "Verdadero"

# Se muestra el resultado de cada operador lógico
print("\nResultados de operadores lógicos:")
print(f"A and B: {a and b}")  # AND lógico: Verdadero solo si ambos valores son Verdadero
print(f"A or B: {a or b}")    # OR lógico: Verdadero si al menos uno de los valores es Verdadero
print(f"not A: {not a}")      # NOT lógico: Invierte el valor de A
print(f"not B: {not b}")      # NOT lógico: Invierte el valor de B

# Operaciones combinadas
print("\nResultados de combinaciones de operadores:")
print(f"(A and B) or (not A): {(a and b) or (not a)}")
print(f"not (A and B): {not (a and b)}")
print(f"(A or B) and not (A and B): {(a or b) and not (a and b)}")
