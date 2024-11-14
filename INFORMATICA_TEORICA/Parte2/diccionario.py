numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Andres",
               "Apellido": "Espinoza",
               "Altura": 1.75,
               "Edad": 22}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Andres": {"Apellido": "Espinoza",
               "Altura": 1.75,
               "Edad": 22},
                "Isacc": {"Apellido": "Espinoza",
               "Altura": 1.89,
               "Edad": 16}}
print(contacts["Andres"])