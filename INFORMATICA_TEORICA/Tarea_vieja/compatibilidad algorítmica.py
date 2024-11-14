#compatibilidad algorítmica

def calcular_compatibilidad(respuestas_1, respuestas_2):
    """
    Calcula la compatibilidad entre dos perfiles comparando sus respuestas a una serie de preguntas.

    :param respuestas_1: Lista de respuestas del primer perfil (e.g., persona 1)
    :param respuestas_2: Lista de respuestas del segundo perfil (e.g., persona 2)
    :return: Porcentaje de compatibilidad entre los dos perfiles
    """
    # Verificar que ambas listas de respuestas tengan el mismo tamaño
    if len(respuestas_1) != len(respuestas_2):
        raise ValueError("Las listas de respuestas deben tener el mismo tamaño.")
    
    # Contador para las respuestas que coinciden
    coincidencias = 0

    # Comparar las respuestas
    for r1, r2 in zip(respuestas_1, respuestas_2):
        if r1 == r2:
            coincidencias += 1
    
    # Calcular el porcentaje de coincidencia
    compatibilidad = (coincidencias / len(respuestas_1)) * 100
    
    return compatibilidad


# Ejemplo de uso
if __name__ == "__main__":
    # Respuestas de dos personas a una serie de preguntas (0: No, 1: Sí)
    #8 preguntas exactamente para cada persona
    respuestas_persona_1 = [1, 1, 1, 1, 1, 1, 1, 1]
    respuestas_persona_2 = [1, 1, 1, 1, 1, 1, 1, 1]

    # Calcular la compatibilidad
    compatibilidad = calcular_compatibilidad(respuestas_persona_1, respuestas_persona_2)

    print(f"La compatibilidad entre los dos perfiles es: {compatibilidad:.2f}%")
