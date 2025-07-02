# Trabajo Práctico Integrador
# Análisis de Algoritmos en Python
# Título: La eficacia de los algoritmos y su impacto en el rendimiento de sistemas
# Alumno: Marisabel Viviana Aramayo
# Profesor: —
# Fecha de entrega: 4 de julio de 2025

import time

# Enfoque 1: Método básico (con listas)
def conteo_con_listas(texto):
    palabras = texto.split()
    resultado = []
    for palabra in palabras:
        contador = 0
        for p in palabras:
            if p == palabra:
                contador += 1
        if (palabra, contador) not in resultado:
            resultado.append((palabra, contador))
    return resultado

# Enfoque 2: Método optimizado (con diccionario)
def conteo_con_diccionario(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

# Programa para medir tiempo
def medir_tiempo(funcion, datos):
    inicio = time.time()
    resultado = funcion(datos)
    fin = time.time()
    return resultado, fin - inicio

# Análisis de rendimiento
texto_corto = "la casa es grande y la casa es blanca "
texto_largo = "la casa es grande y la casa es blanca " * 1000

conteo_con_listas_corto = medir_tiempo(conteo_con_listas, texto_corto)
conteo_con_listas_largo = medir_tiempo(conteo_con_listas, texto_largo)
conteo_con_diccionario_corto = medir_tiempo(conteo_con_diccionario, texto_corto)
conteo_con_diccionario_largo = medir_tiempo(conteo_con_diccionario, texto_largo)

print("Análisis de rendimiento: \n")
print("Pruebas con texto corto: \n")
print(f"El conteo con listas contó {conteo_con_listas_corto[0]}")
print(f"El conteo con diccionario contó {conteo_con_diccionario_corto[0]}")
print(f"El conteo con listas tardó {conteo_con_listas_corto[1]} segundos")
print(f"El conteo con diccionario tardó {conteo_con_diccionario_corto[1]} segundos\n")


print("Pruebas con texto largo: \n")
print(f"El conteo con listas contó {conteo_con_listas_largo[0]}")
print(f"El conteo con diccionario contó {conteo_con_diccionario_largo[0]}")
print(f"El conteo con listas tardó {conteo_con_listas_largo[1]} segundos")
print(f"El conteo con diccionario tardó {conteo_con_diccionario_largo[1]} segundos\n")
