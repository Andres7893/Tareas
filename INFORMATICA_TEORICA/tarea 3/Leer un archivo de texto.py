file = open("tarea 3./caperucita.txt")
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
  print(line)
file.close

with open("tarea 3./caperucita.txt") as file:
  for line in file:
    print(line)