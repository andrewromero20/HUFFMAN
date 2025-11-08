class Nodo:
    def __init__(self, char, freq, izquierda=None, derecha=None):
        self.char = char  #Caracter o simbolo
        self.freq = freq  #Frecuencia de ese caracter

        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.freq < otro.freq

    def __repr__(self):
        if self.char:
            return f"Nodo('{self.char}', {self.freq})"
        return f"Nodo(Interno, {self.freq})"