def generar_codigos(nodo, tabla_codigos, codigo_actual=""):
    if nodo.char is not None: #Se ha llegado a un nodo hoja
        if not codigo_actual: #Si el codigo actual es: "" le asignamos un 0
            tabla_codigos[nodo.char] = '0'
        else:#  De lo contrario ponemos el codigo actual
            tabla_codigos[nodo.char] = codigo_actual
        return

    #Ir a la izquierda y poner agregar un 0
    if nodo.izquierda:
        generar_codigos(nodo.izquierda, tabla_codigos, codigo_actual + '0')

    #Ir a la derecha y poner agregar un 1 al codigo actual
    if nodo.derecha:
        generar_codigos(nodo.derecha, tabla_codigos, codigo_actual + '1')
