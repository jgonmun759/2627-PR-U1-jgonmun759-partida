VALORACION_PARTIDA = ("Sigue practicando", "Buen resultado", "Excelente")

PUNT_ACIERTO = 3
PUNT_ERROR = 1

def calcular_resultados(aciertos: int, errores: int) -> tuple[int, int]:
    """
    Calcula los resultados de una partida dependiendo de los aciertos y errores.

    :param aciertos: el número de aciertos
    :param errores: el número de errores

    :return: una tupla con el número total de preguntas respondidas y la puntuación, respectivamente.
    """
    return (aciertos + errores), (aciertos * PUNT_ACIERTO) - (errores * PUNT_ERROR)


def valorar_partida(puntuacion: int) -> int:
    """
    Indica la posición del mensaje que se debe mostrar de VALORACION_PARTIDA.

    :param puntuacion: la puntuación a valorar
    :return: la posición que se debe mostrar
    """
    valor = 0

    if 10 <= puntuacion <= 19:
        valor = 1
    elif puntuacion > 20:
        valor = 2

    return valor

def main():
    aciertos = int(input())
    errores = int(input())

    if (aciertos >= 0) and (errores >= 0):
        total_preguntas, puntuacion = calcular_resultados(aciertos, errores)
        pos_valoracion = valorar_partida(puntuacion)

        print(f"\nPreguntas respondidas: {total_preguntas} \nPuntuación: {puntuacion} \nValoración: {VALORACION_PARTIDA[pos_valoracion]}")
    else:
        print("\nERROR - valores incorrectos")


if __name__ == "__main__":
    main()