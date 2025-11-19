"""
Módulo que implementa un árbol de decisión de un solo nodo (umbral).
"""


def clasificar(numero: int, umbral: int = 50) -> str:
    """
    Clasifica un número como 'Alto' o 'Bajo' basado en un umbral.

    Args:
        numero (int): Número a clasificar.
        umbral (int, optional): Umbral de decisión. Default 50.

    Returns:
        str: "Alto" si numero >= umbral; "Bajo" en caso contrario.
    """
    if numero >= umbral:
        return "Alto"
    else:
        return "Bajo"
