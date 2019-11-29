class NodoCola:
    def __init__(self,valor,siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

    def setSiguiente(self,siguiente):
        self.siguiente = siguiente

    def getValor(self):
        return self.valor

    def getSiguiente(self):
        return self.siguiente

class Cola:
    def __init__(self):
        self.size = 0
        self.inicio = None
        self.final = None

    def getSize(self):
        return self.size

    def encolar(self,valor):
        nuevo = NodoCola(valor)
        if(self.size == 0):
            self.inicio = nuevo
            self.final = nuevo
        else:
            if(self.size == 1):
                self.inicio.setSiguiente(nuevo)
            else:
                self.final.setSiguiente(nuevo)
            self.final = nuevo
        self.size = self.size + 1


    def desencolar(self):
        retu = None
        if(self.size > 0):
            retu = self.inicio.getValor()
            if(self.size == 1):
                self.inicio = None
                self.final = None
            else:
                self.inicio = self.inicio.getSiguiente()
            self.size = self.size - 1
        return retu

cola = Cola()
string = ""

print("se ingresan 12 valores")
for a in range(0,12):
    cola.encolar(a)

print(cola.getSize())

print("se sacan 12 valores")
for a in range(0,12):
    print(cola.desencolar())

print(cola.getSize())
