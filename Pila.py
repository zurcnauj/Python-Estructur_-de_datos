class NodoPila :
    def __init__(self,valor ,anterior=None):
        self.valor = valor
        self.anterior = anterior

    def getValor(self):
        return self.valor

    def getAnterior(self):
        return self.anterior

class Pila :
    def __init__(self):
        self.size = 0
        self.nodo = None

    def getSize(self):
        return self.size

    def push(self,valor):
        nuevo = NodoPila(valor, self.nodo)
        self.nodo = nuevo
        self.size = self.size + 1

    def top(self):
        if(nodo != None):
            return nodo.getValor()
        else:
            return None

    def pop(self):
        if(self.nodo != None):
            retu = self.nodo.getValor()
            self.nodo = self.nodo.getAnterior()
            self.size = self.size -1
            return retu
        else:
            return None

objeto = NodoPila(12)
#print(objeto.getValor())

pila = Pila()

print("se ingresan 12 valores")
for a in range(0,12):
    pila.push(a)

print(pila.getSize())

print("se sacan 12 valores")
for a in range(0,12):
    print(pila.pop())

print(pila.getSize())
