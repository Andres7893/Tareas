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


def cliente_actualizado(nombre_cliente, actualizar_nombre_cliente):
    global clients

    if nombre_cliente in clients:
        clients = clients.replace(nombre_cliente + ',', actualizar_nombre_cliente + ',')
    else:
        print('El cliente no esta en la lista de clientes')

def borrar_cliente(nombre_cliente):
    global clients
    if nombre_cliente in clients:
        clients = clients.replace(nombre_cliente + ',','')
        pass
    else:
        print('El cliente no esta en la lista de cliente')
def _add_comma():
    global clients

    clients += ','

    
def _print_bienvenido():
    print('BIENVENIDO A TECNOLIGY VENTAS')
    print('*'*50)
    print('¿Que te gustaria hacer hoy?')
    print('[C]rear cliente')
    print('[A]ctualizar cliente')
    print('[B]orrar cliente')

def _get_nombre_cliente():
    return input('Cual es el nombre del cliente: ')

if __name__ == '__main__':
    _print_bienvenido()

    command = input()
    command = command.upper()

    if command == 'C':
        nombre_cliente = _get_nombre_cliente()
        crear_cliente(nombre_cliente)
        lista_clientes()
    elif command == 'B':
        nombre_cliente = _get_nombre_cliente()
        borrar_cliente(nombre_cliente)
        lista_clientes()
        pass
    elif command == 'A':
        nombre_cliente = _get_nombre_cliente()
        actualizar_nombre_cliente = input('Cual es el nombre actualizado del cliente: ')
        cliente_actualizado(nombre_cliente, actualizar_nombre_cliente)
        lista_clientes()
    else:
        print('comando invalido')