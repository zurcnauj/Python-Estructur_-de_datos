class Objeto:
	def __init__(self, num):
		self.numero = num

	def getNumero(self):
		return self.numero


objeto = Objeto(12)
print(objeto.getNumero())