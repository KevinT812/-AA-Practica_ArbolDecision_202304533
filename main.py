"""
Programa principal que ejecuta la clasificación de números usando un árbol simple.
"""

import time
import argparse
from src.utils import verificar_o_generar_archivo, leer_numeros
from src.arbol import clasificar


def main():
    """Función principal del programa."""

    print("\na) Iniciando cronómetro...")
    inicio = time.time()

    # Configurar argumentos
    parser = argparse.ArgumentParser(description="Clasificación simple con árbol de decisión.")
    parser.add_argument("--umbral", type=int, default=50, help="Umbral de clasificación (default = 50)")
    args = parser.parse_args()

    UMBRAL = args.umbral

    print("b) Verificando o generando archivo data/numeros_1000.txt...")
    ruta_archivo = "data/numeros_1000.txt"
    verificar_o_generar_archivo(ruta_archivo)

    print("c) Leyendo números del archivo...")
    numeros = leer_numeros(ruta_archivo)

    print("d) Clasificando números usando el árbol de decisión...")
    resultados = [clasificar(n, UMBRAL) for n in numeros]

    print("e) Imprimiendo resultados y conteos...")

    # Mostrar primeros 10 resultados
    print("\nPrimeros 10 resultados:")
    for i in range(10):
        print(f"{numeros[i]} → {resultados[i]}")

    # Conteos
    total_altos = resultados.count("Alto")
    total_bajos = resultados.count("Bajo")

    print("Conteos finales:")
    print(f"Alto: {total_altos}")
    print(f"Bajo: {total_bajos}")

    print("f) Deteniendo cronómetro y mostrando tiempo total...")
    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos\n")


if __name__ == "__main__":
    main()
