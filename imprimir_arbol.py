def imprimir_arbol_texto(nodo, prefijo="", es_ultimo=True):
    print(prefijo, end="")
    if es_ultimo:
        print("└── ", end="")
        nuevo_prefijo = prefijo + "    "
    else:
        print("├── ", end="")
        nuevo_prefijo = prefijo + "│   "

    if nodo.char:
        print(f"'{nodo.char}' ({nodo.freq})")
    else:
        print(f"(*) ({nodo.freq})")

    hijos = []
    if nodo.izquierda:
        hijos.append(nodo.izquierda)
    if nodo.derecha:
        hijos.append(nodo.derecha)

    for i, hijo in enumerate(hijos):
        es_ultimo_hijo = (i == len(hijos) - 1)
        imprimir_arbol_texto(hijo, nuevo_prefijo, es_ultimo_hijo)