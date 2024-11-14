clients = 'Andres, Abram, '

def crear_cliente(nombre_cliente):
    global clients

    if nombre_cliente not in clients:
        clients += nombre_cliente
        _add_comma()
    else:
        print('Cliente ya esta en la lista de clientes')

def lista_clientes():
    global clients

    print(clients)

def _add_comma():
    global clients

    clients += ','

    
def _print_bienvenido():
    print('BIENVENIDO A TECNOLIGY VENTAS')
    print('*'*50)
    print('¿Que te gustaria hacer hoy?')
    print('[C]rear cliente')
    print('[B]orrar cliente')


if __name__ == '__main__':
    _print_bienvenido()

    command = input()

    if command == 'C':
        nombre_cliente = input('Cual es el cliente: ')
        crear_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'B':
        pass
    else:
        print('comndo imvalido')