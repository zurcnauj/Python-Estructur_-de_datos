class ColaConPrioridad:
    def __init__(self,funcion):
        self.size = 0
        self.funcion = funcion
        self.arreglo = []
        self.arreglo.append(None)

    def agregar(self,valor):
        self.arreglo.append(valor)
        self.size = self.size + 1
        self._acomodarA(self.size)

    def _acomodarA(self, num):
        if(num  > 1):
            ref = num // 2
            if(self.funcion(self.arreglo[num],self.arreglo[ref])):
                auxiliar = self.arreglo[num]
                self.arreglo[num] = self.arreglo[ref]
                self.arreglo[ref] = auxiliar
                self._acomodarA(ref)

    def quitar(self):
        if( self.size == 0):
            return None
        else:
            retu = self.arreglo[1]
            self.arreglo[1] = self.arreglo[self.size]
            self.arreglo[1] == self.arreglo.pop()
            self.size = self.size - 1
            self._acomodarQ(1)
            return retu

    def _acomodarQ(self,num):
        ref = num * 2
        if(ref <= self.size):
            acambiar = self._masRele(ref)
            if(self.funcion(self.arreglo[acambiar],self.arreglo[num])):
                auxiliar = self.arreglo[num]
                self.arreglo[num] = self.arreglo[acambiar]
                self.arreglo[acambiar] = auxiliar
                self._acomodarQ(acambiar)

    def _masRele(self,num):
        if((num + 1 <= self.size) and (self.funcion(self.arreglo[num], self.arreglo[num + 1]))):
            return num + 1
        else:
            return num

def mayor(valor1, valor2):
    return valor1 > valor2

ccp = ColaConPrioridad(mayor)

for num in range(0,30):
    ccp.agregar(num)

for num in range(0,3):
    print(ccp.quitar())
