# Práctica: Árbol de Decisión Simple con GitFlow

**Universidad Da Vinci de Guatemala**  
**Curso:** Análisis de Algoritmos  
**Instructor:** Ing. César Sazo  
**Práctica:** Árbol de Decisión y Flujo GitFlow  
**Nombre:** Sergio Agustin
**Carnet:** 202304533  
**Fecha de entrega:** 18/11/2025

## Objetivo General

Construir y ejecutar un árbol de decisión simple en Python (sin librerías externas) para clasificar números como “Alto” o “Bajo” utilizando un umbral configurable, aplicando correctamente el flujo de trabajo Gitflow (ramas, commits, PRs, merges y versionado semántico).

## Objetivos Específicos

- Implementar un árbol de decisión minimalista con un solo nodo (umbral).  
- Generar y/o cargar un archivo con 1000 números enteros aleatorios.  
- Clasificar cada número según el criterio del umbral.  
- Imprimir resultados parciales, conteos y tiempo total en consola.  
- Aplicar Gitflow de manera rigurosa (feature, develop, main, hotfix).  
- Documentar mediante docstrings (PEP-257) y README.md.  
- Generar evidencia de commits, ramas, PRs y ejecución.  

## Descripción del Árbol de Decisión

El árbol utilizado en esta práctica es un árbol de un solo nodo (raíz) con dos posibles salidas:

                 ┌─── "Alto" (n ≥ UMBRAL)
        número ≥ UMBRAL?
                 └─── "Bajo" (n < UMBRAL)

Umbral por defecto: 50
Clasificación:
-Si n ≥ umbral → “Alto”
-Si n < umbral → “Bajo"


## Metodología

### 1. Pasos del Script

1.  Generé una semilla aleatoria.\
2.  Creé una lista de 1000 números entre 0 y 100.\
3.  Clasifiqué cada número como Alto o Bajo usando el umbral.\
4.  Mostré los primeros 10 datos como ejemplo.\
5.  Conté cuántos fueron Altos y cuántos fueron Bajos.\
6.  Medí el tiempo total de ejecución del programa.\
7.  Guardé todos los resultados en un archivo de texto.

### 2. Flujo del promagra(main.py)
* Iniciar cronómetro  
* Verificar o generar data/numeros_1000.txt  
* Leer los 1000 números  
* Clasificar con el árbol de decisión  
* Imprimir:
    - Primeros 10 resultados
    - Conteo de “Alto” y “Bajo”   
* Mostrar el tiempo total

### 3. Flujo Gitflow aplicado
**Ramas creadas:**
- main
- develop
- feature/implementacion_arbol
- hotfix/cambio_nombre

**Commits significativos:**
- [feature] Estructura base del proyecto
- [feature] Generación de numeros_1000.txt
- [feature] Implementación del árbol de decisión y clasificación
- [feature] Impresión de resultados y conteos + tiempo total
- [hotfix] Cambio de nombre temporal por requerimiento del instructor

**Pull Requests realizados:**
- PR: feature/implementacion_arbol → develop
- PR: develop → main

**Versionado:**
- v1.0.0 — Merge estable en rama main
- v1.0.1 — Hotfix aplicado y documentado

## Resultados

Primeros 10 ejemplos:\
65 → Alto  
7 → Bajo  
5 → Bajo  
31 → Bajo  
14 → Bajo  
7 → Bajo  
80 → Alto  
63 → Alto  
83 → Alto  
75 → Alto  

### Conteos finales

-   Altos: 502
-   Bajos: 498

### Tiempo total

0.0313 segundos

## Evidencias

Las evidencias de la práctica se encuentran en:\
`docs/evidencias`

## Conclusiones
- Esta práctica permitió comprender la estructura y funcionamiento básico de un árbol de decisión de un solo nodo.
- Gitflow se consolidó como una metodología profesional para organizar y controlar el ciclo de desarrollo.
- El uso de ramas feature y hotfix ayuda a mantener el proyecto ordenado.
- El versionado semántico (v1.0.0, v1.0.1) facilita identificar entregas estables y correcciones puntuales.
- La práctica combina algoritmos simples con buenas prácticas de ingeniería de software.
