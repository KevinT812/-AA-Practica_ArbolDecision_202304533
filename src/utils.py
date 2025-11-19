"""
Módulo de utilidades para manejo de archivos y lectura de datos.
"""

import os
import random
from pathlib import Path


def verificar_o_generar_archivo(ruta_archivo: str) -> None:
    """
    Verifica si el archivo existe; si no existe, genera números aleatorios.

    Args:
        ruta_archivo (str): Ruta del archivo a verificar o generar.

    Los números generados estarán en el rango 1–100, uno por línea.
    Se imprime la semilla utilizada en caso de generar el archivo.
    """
    ruta = Path(ruta_archivo)

    # Crear carpeta si no existe
    if not ruta.parent.exists():
        ruta.parent.mkdir(parents=True, exist_ok=True)

    # Si el archivo ya existe no se genera nada
    if ruta.exists():
        return

    # Generar archivo porque no existe
    semilla = random.randint(1, 999999)
    random.seed(semilla)

    print(f"Archivo no encontrado. Generando numeros_1000.txt con semilla: {semilla}")

    with open(ruta, "w") as f:
        for _ in range(1000):
            numero = random.randint(1, 100)
            f.write(f"{numero}\n")


def leer_numeros(ruta_archivo: str) -> list:
    """
    Lee números enteros desde un archivo de texto.

    Args:
        ruta_archivo (str): Ruta del archivo a leer.

    Returns:
        list: Lista de enteros obtenidos del archivo.
    """
    numeros = []
    with open(ruta_archivo, "r") as f:
        for linea in f:
            numero = int(linea.strip())
            numeros.append(numero)
    return numeros
