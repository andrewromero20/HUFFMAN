from collections import Counter
from xmlrpc.client import Binary

from encoders import load_from_disk
from nodo import Nodo
import heapq
from imprimir_arbol import imprimir_arbol_texto
from generar_codigos import generar_codigos
import encoders

INPUT_FILE_PATH = "libro.txt"
OUTPUT_FILE_PATH = "./compressed.pae"
UNCOMPRESSED = "decompressed.txt"

frecuencias = Counter()
#Abrir el archivo en modo lectura
with open('libro.txt', 'r', encoding='utf-8') as f:
    #Contar las frecuencias linea por linea
    for linea in f:
        frecuencias.update(linea)

print("Conteo finalizado.")
# Imprime los 5 caracteres más comunes
print(frecuencias.most_common(5))

cola_prioridad = []
for char, freq in frecuencias.items():
    nodo = Nodo(char, freq)
    cola_prioridad.append(nodo)

# Convertir la lista en una min-heap
heapq.heapify(cola_prioridad)

#Bucle principal del algoritmo de Huffman
while len(cola_prioridad) > 1:
    nodo_izq = heapq.heappop(cola_prioridad)
    nodo_der = heapq.heappop(cola_prioridad)

    freq_suma = nodo_izq.freq + nodo_der.freq
    nodo_padre = Nodo(None, freq_suma, nodo_izq, nodo_der)

    heapq.heappush(cola_prioridad, nodo_padre)

# El único elemento que queda es la raíz
raiz_huffman = cola_prioridad[0]

print("--- Árbol de Huffman construido ---")
print(f"Raíz final: {raiz_huffman}")
print(f"Total de nodos (caracteres únicos): {len(frecuencias)}")

print("\n--- Representación del árbol en texto ---")
imprimir_arbol_texto(raiz_huffman)

print("\n--- Tabla de Códigos de Huffman ---")

#Diccionario para guardar los codigos
tabla_huffman = {}
#Llenar la tabla con los codigos generados
generar_codigos(raiz_huffman, tabla_huffman)

print("Comprimiendo con algoritmo Huffman")
binary_string = encoders.huffman_encode(INPUT_FILE_PATH, tabla_huffman)
encoders.write_to_disk(OUTPUT_FILE_PATH, binary_string)

uncompressed_binary_string = encoders.load_from_disk(OUTPUT_FILE_PATH)
uncompressed_text = encoders.decode_huffman_string(uncompressed_binary_string, raiz_huffman)

