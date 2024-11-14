# utils.py

def get_population():
    """
    Devuelve una lista de países y sus poblaciones.
    """
    keys = ['Colombia', 'Bolivia']
    values = [500, 300]
    return keys, values

def population_by_country(data, country):
    """
    Busca la población de un país específico en la lista de datos.
    
    :param data: Lista de diccionarios con datos de países.
    :param country: Nombre del país a buscar.
    :return: Población del país si se encuentra, None si no.
    """
    for entry in data:
        if entry['Country'].lower() == country.lower():
            return entry['Population']
    return None
