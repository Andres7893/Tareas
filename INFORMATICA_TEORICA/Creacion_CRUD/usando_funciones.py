clients = 'Andres, Abram, '

def crear_cliente(nombre_cliente):
    global clients

    clients += nombre_cliente
    _add_comma()


def lista_clientes():
    global clients

    print(clients)

def _add_comma():
    global clients

    clients += ','

    
if __name__ == '__main__':

    lista_clientes()

    crear_cliente('Aaron')

    lista_clientes()

    print(clients)