frase = input("Escribe una frase: ")

# Convertir la frase a mayúsculas
frase_mayus = frase.upper()
print("Frase en mayúsculas:", frase_mayus)

# Convertir la frase a minúsculas
frase_minus = frase.lower()
print("Frase en minúsculas:", frase_minus)

# Contar el número de palabras en la frase
palabras = frase.split()
num_palabras = len(palabras)
print("Número de palabras en la frase:", num_palabras)

# Mostrar las palabras en orden inverso
palabras_inversas = ' '.join(palabras[::-1])
print("Palabras en orden inverso:", palabras_inversas)