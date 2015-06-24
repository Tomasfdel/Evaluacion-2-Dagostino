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
    
	def check_padre_izq(self):
		if(self.estaLlena()):
			if(self.padre_izq.estaLlena()):
				if(self.padre_izq.hijo_izq.estaLlena() == False):
					self.padre_izq.hijo_izq.set_valor(self.padre_izq.valor-self.valor)
					self.padre_izq.hijo_izq.check_celda()
			
			else:
				if(self.padre_izq.hijo_izq.estaLlena()):
					self.padre_izq.set_valor(self.padre_izq.hijo_izq.valor+self.valor)
					self.padre_izq.check_celda()
				

	def check_padre_der(self):
		if(self.estaLlena()):
			if(self.padre_der.estaLlena()):
				if(self.padre_der.hijo_der.estaLlena() == False):
					self.padre_der.hijo_der.set_valor(self.padre_der.valor-self.valor)
					self.padre_der.hijo_der.check_celda()
			
			else:
				if(self.padre_der.hijo_der.estaLlena()):
					self.padre_der.set_valor(self.padre_der.hijo_der.valor+self.valor)
					self.padre_der.check_celda()
						
						
	def check_hijos(self):
		if(self.estaLlena()):
			if(self.hijo_der.estaLlena()):
				if(self.hijo_izq.estaLlena() == False):
					self.hijo_izq.set_valor(self.valor-self.hijo_der.valor)
					self.hijo_izq.check_celda()
			else:
				if(self.hijo_izq.estaLlena()):
					self.hijo_der.set_valor(self.valor-self.hijo_izq.valor)
					self.hijo_der.check_celda()				
	
	def corregir_celda(self):
		if(self.estaLlena()):
			if(self.hijo_izq.estaLlena() and self.hijo_der.estaLlena()):
				if(self.valor == self.hijo_izq.valor + self.hijo_der.valor ):
					return 1
					
		return 0
		
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
  		
	def corregir_celda(self):
		if(self.estaLlena()):
			return 1
		else:
			return 0
		
		
  		
class Celda_Abajo_Izq (Celda):
	def set_parientes(self, padred):
  		self.padre_der=padred
  
	def check_celda (self):
  		self.check_padre_der()
  		
	def corregir_celda(self):
		if(self.estaLlena()):
			return 1
		else:
			return 0
			
  		
class Celda_Abajo_Der (Celda):
	def set_parientes(self, padrei):
  		self.padre_izq=padrei
  

	def check_celda (self):
  		self.check_padre_izq()

	def corregir_celda(self):
		if(self.estaLlena()):
			return 1
		else:
			return 0
			
			
			
			
			
			
class Piramide:
	def __init__(self):
		self.checksum = 0
		self.celda00 = Celda_Sup()
		self.celda10 = Celda_Izq()
		self.celda11 = Celda_Der()
		self.celda20 = Celda_Izq()
		self.celda21 = Celda()
		self.celda22 = Celda_Der()
		self.celda30 = Celda_Izq()
		self.celda31 = Celda()
		self.celda32 = Celda()
		self.celda33 = Celda_Der()
		self.celda40 = Celda_Izq()
		self.celda41 = Celda()
		self.celda42 = Celda()
		self.celda43 = Celda()
		self.celda44 = Celda_Der()
		self.celda50 = Celda_Abajo_Izq()
		self.celda51 = Celda_Abajo()
		self.celda52 = Celda_Abajo()
		self.celda53 = Celda_Abajo()
		self.celda54 = Celda_Abajo()
		self.celda55 = Celda_Abajo_Der()

		self.celda00.set_parientes(self.celda10, self.celda11)
		self.celda10.set_parientes(self.celda00, self.celda20, self.celda21)
		self.celda11.set_parientes(self.celda00, self.celda21, self.celda22)
		self.celda20.set_parientes(self.celda10, self.celda30, self.celda31)
		self.celda21.set_parientes(self.celda10, self.celda11, self.celda31, self.celda32)
		self.celda22.set_parientes(self.celda11, self.celda32, self.celda33)
		self.celda30.set_parientes(self.celda20, self.celda40, self.celda41)
		self.celda31.set_parientes(self.celda20, self.celda21, self.celda41, self.celda42)
		self.celda32.set_parientes(self.celda21, self.celda22, self.celda42, self.celda43)
		self.celda33.set_parientes(self.celda22, self.celda43, self.celda44)
		self.celda40.set_parientes(self.celda30, self.celda50, self.celda51)
		self.celda41.set_parientes(self.celda30, self.celda31, self.celda51, self.celda52)
		self.celda42.set_parientes(self.celda31, self.celda32, self.celda52, self.celda53)
		self.celda43.set_parientes(self.celda32, self.celda33, self.celda53, self.celda54)
		self.celda44.set_parientes(self.celda33, self.celda54, self.celda55)
		self.celda50.set_parientes(self.celda40)
		self.celda51.set_parientes(self.celda40, self.celda41)
		self.celda52.set_parientes(self.celda41, self.celda42)
		self.celda53.set_parientes(self.celda42, self.celda43)
		self.celda54.set_parientes(self.celda43, self.celda44)
		self.celda55.set_parientes(self.celda44)

	def controlar (self):
		self.celda00.check_celda()
		self.celda10.check_celda()
		self.celda11.check_celda()
		self.celda20.check_celda()
		self.celda21.check_celda()
		self.celda22.check_celda()
		self.celda30.check_celda()
		self.celda31.check_celda()
		self.celda32.check_celda()
		self.celda33.check_celda()
		self.celda40.check_celda()
		self.celda41.check_celda()
		self.celda42.check_celda()
		self.celda43.check_celda()
		self.celda44.check_celda()
		self.celda50.check_celda()
		self.celda51.check_celda()
		self.celda52.check_celda()
		self.celda53.check_celda()
		self.celda54.check_celda()
		self.celda55.check_celda()

	def corregir (self):
		self.checksum= self.checksum + self.celda00.corregir_celda()
		self.checksum= self.checksum + self.celda10.corregir_celda()
		self.checksum= self.checksum + self.celda11.corregir_celda()
		self.checksum= self.checksum + self.celda20.corregir_celda()
		self.checksum= self.checksum + self.celda21.corregir_celda()
		self.checksum= self.checksum + self.celda22.corregir_celda()
		self.checksum= self.checksum + self.celda30.corregir_celda()
		self.checksum= self.checksum + self.celda31.corregir_celda()
		self.checksum= self.checksum + self.celda32.corregir_celda()
		self.checksum= self.checksum + self.celda33.corregir_celda()
		self.checksum= self.checksum + self.celda40.corregir_celda()
		self.checksum= self.checksum + self.celda41.corregir_celda()
		self.checksum= self.checksum + self.celda42.corregir_celda()
		self.checksum= self.checksum + self.celda43.corregir_celda()
		self.checksum= self.checksum + self.celda44.corregir_celda()
		self.checksum= self.checksum + self.celda50.corregir_celda()
		self.checksum= self.checksum + self.celda51.corregir_celda()
		self.checksum= self.checksum + self.celda52.corregir_celda()
		self.checksum= self.checksum + self.celda53.corregir_celda()
		self.checksum= self.checksum + self.celda54.corregir_celda()
		self.checksum= self.checksum + self.celda55.corregir_celda()
		
		if(self.checksum == 21):
			return True
		else:
			return False 
			
			
	def set_valores(self):
		#self.celda00.set_valor(0)
		#self.celda10.set_valor(0)
		#self.celda11.set_valor(0)
		#self.celda20.set_valor(0)
		#self.celda21.set_valor(0)
		#self.celda22.set_valor(0)
		#self.celda30.set_valor(0)
		#self.celda31.set_valor(0)
		#self.celda32.set_valor(0)
		#self.celda33.set_valor(0)
		#self.celda40.set_valor(0)
		#self.celda41.set_valor(0)
		#self.celda42.set_valor(0)
		#self.celda43.set_valor(0)
		#self.celda44.set_valor(0)
		#self.celda50.set_valor(0)
		#self.celda51.set_valor(0)
		#self.celda52.set_valor(0)
		#self.celda53.set_valor(0)
		#self.celda54.set_valor(0)
		#self.celda55.set_valor(0)
			
	
			
			
class Juego:
	def __init__(self):
		self.Pyramid = Piramide()
		self.Pyramid.set_valores()
        
	def jugar(self):
		self.Pyramid.controlar()
		if(self.Pyramid.corregir() ):
			print ("Anduvo :D")
		else:
			print ("No anduvo D:")
            
            
            
            
GameManager = Juego()
GameManager.jugar()
