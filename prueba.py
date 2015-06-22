# Evaluacion-FdeLuco-Moline 

class Celda:
	def __init__ (self):
		self.llena = False
		self.valor = -1

	def set_parientes(self, padrei, padred, hijoi, hijod):
  		self.padre_izq=padrei
  		self.padre_der=padred
  		self.hijo_izq=hijoi
  		self.hijo_der=hijod
  
	def check_celda (self):
  		self.check_padre_izq()
  		self.check_padre_der()
  		self.check_hijos()
  

	def set_valor (self, n):
		self.valor = n
		self.llena = True

	def estaLlena (self):
		return self.llena



class Celda_Sup (Celda):
	def set_parientes(self, hijoi, hijod):
  		self.hijo_izq=hijoi
  		self.hijo_der=hijod

	def check_celda (self):
  		self.check_hijos()
	
	
	
class Celda_Izq (Celda):
	def set_parientes(self, padred, hijoi, hijod):
  		self.padre_der=padred
  		self.hijo_izq=hijoi
  		self.hijo_der=hijod
  
	def check_celda (self):
  		self.check_padre_der()
  		self.check_hijos()
  		
  		
  		
class Celda_Der (Celda):
	def set_parientes(self, padrei, hijoi, hijod):
  		self.padre_izq=padrei
  		self.hijo_izq=hijoi
  		self.hijo_der=hijod
  
	def check_celda (self):
  		self.check_padre_izq()
  		self.check_hijos()
  		
  		
  		
class Celda_Abajo (Celda):
	def set_parientes(self, padrei, padred):
  		self.padre_izq=padrei
  		self.padre_der=padred
  
	def check_celda (self):
  		self.check_padre_izq()
  		self.check_padre_der()
  		
  		
  		
class Celda_Abajo_Izq (Celda):
	def set_parientes(self, padred):
  		self.padre_der=padred
  
	def check_celda (self):
  		self.check_padre_der()
  		
  		
  		
class Celda_Abajo_Der (Celda):
	def set_parientes(self, padrei):
  		self.padre_izq=padrei
  

	def check_celda (self):
  		self.check_padre_izq()

  		
celda00 = Celda_Sup()
celda10 = Celda_Izq()
celda11 = Celda_Der()
celda20 = Celda_Izq()
celda21 = Celda()
celda22 = Celda_Der()
celda30 = Celda_Izq()
celda31 = Celda()
celda32 = Celda()
celda33 = Celda_Der()
celda40 = Celda_Izq()
celda41 = Celda()
celda42 = Celda()
celda43 = Celda()
celda44 = Celda_Der()
celda50 = Celda_Abajo_Izq()
celda51 = Celda_Abajo()
celda52 = Celda_Abajo()
celda53 = Celda_Abajo()
celda54 = Celda_Abajo()
celda55 = Celda_Abajo_Der()

celda00.set_parientes(celda10, celda11)
celda10.set_parientes(celda00, celda20, celda21)
celda11.set_parientes(celda00, celda21, celda22)
celda20.set_parientes(celda10, celda30, celda31)
celda21.set_parientes(celda10, celda11, celda31, celda32)
celda22.set_parientes(celda11, celda32, celda33)
celda30.set_parientes(celda20, celda40, celda41)
celda31.set_parientes(celda20, celda21, celda41, celda42)
celda32.set_parientes(celda21, celda22, celda42, celda43)
celda33.set_parientes(celda33, celda43, celda44)
celda40.set_parientes(celda30, celda50, celda51)
celda41.set_parientes(celda30, celda31, celda51, celda52)
celda42.set_parientes(celda31, celda32, celda52, celda53)
celda43.set_parientes(celda32, celda33, celda53, celda54)
celda44.set_parientes(celda33, celda54, celda55)
celda50.set_parientes(celda40)
celda51.set_parientes(celda40, celda41)
celda52.set_parientes(celda41, celda42)
celda53.set_parientes(celda42, celda43)
celda54.set_parientes(celda43, celda44)
celda55.set_parientes(celda44)
