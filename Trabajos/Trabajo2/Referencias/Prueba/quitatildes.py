from unidecode import unidecode


def quitar_tildes(palabra):
    return unidecode(palabra)


# Ejemplo de uso
with open("wordlist.txt", "r", encoding="utf-8") as archivo_entrada:
    lineas = archivo_entrada.readlines()

nuevas_lineas = []

for linea in lineas:
    # Dividir la línea en palabras
    palabras = linea.split()

    # Quitar tildes de cada palabra y agregar a la nueva línea
    nuevas_palabras = [quitar_tildes(palabra) + "\n" for palabra in palabras]

    # Unir las palabras y agregar la nueva línea
    nueva_linea = "".join(nuevas_palabras)

    nuevas_lineas.append(nueva_linea)

# Escribir las nuevas líneas en un nuevo archivo
with open("wordlist.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.writelines(nuevas_lineas)
