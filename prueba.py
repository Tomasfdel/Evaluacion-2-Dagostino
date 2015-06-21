# Evaluacion-FdeLuco-Moline 

class Celda:
	def __init__ (self):
		self.llena = False
		self.valor = -1

	def set_padre_izq (self, padrei):
		self.padre_izq = padrei
	def set_padre_der (self, padred):
		self.padre_der = padred
	def set_hijo_izq (self, hijoi):
		self.hijo_izq = hijoi
	def set_hijo_der (self, hijod):
		self.hijo_der = hijod

	def set_valor (self, n):
		self.valor = n
		self.llena = True

	def estaVacia (self):
		return self.llena


celdaNula = Celda()
celdaNula.set_padre_izq(celdaNula)
celdaNula.set_padre_der(celdaNula)
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda00 = Celda()
celdaNula.set_padre_izq(celdaNula)
celdaNula.set_padre_der(celdaNula)

celda10 = Celda()
celdaNula.set_padre_izq(celdaNula)

celda11 = Celda()
celdaNula.set_padre_der(celdaNula)

celda20 = Celda()
celdaNula.set_padre_izq(celdaNula)

celda21 = Celda()

celda22 = Celda()
celdaNula.set_padre_der(celdaNula)

celda30 = Celda()
celdaNula.set_padre_izq(celdaNula)

celda31 = Celda()

celda32 = Celda()

celda33 = Celda()
celdaNula.set_padre_der(celdaNula)

celda40 = Celda()
celdaNula.set_padre_izq(celdaNula)

celda41 = Celda()

celda42 = Celda()

celda43 = Celda()

celda44 = Celda()
celdaNula.set_padre_der(celdaNula)

celda50 = Celda()
celdaNula.set_padre_izq(celdaNula)
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda51 = Celda()
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda52 = Celda()
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda53 = Celda()
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda54 = Celda()
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)

celda55 = Celda()
celdaNula.set_padre_der(celdaNula)
celdaNula.set_hijo_izq(celdaNula)
celdaNula.set_hijo_der(celdaNula)






      
      
      
