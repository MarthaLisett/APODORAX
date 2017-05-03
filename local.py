""" Clase Local
Hereda los metodos de distribucion de memoria
de la clase Memory y cuenta con los limites
de memoria para cada tipo de dato junto con
sus propios diccionario.
José González Ayerdi - A01036121
Martha Benavides - A01280115
10/03/2017
"""
from memory import Memory

class Local(Memory):
	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters
		
		# limites del segmento de locales
		self.l_limit = 5000
		self.u_limit = 9999
		self.dir_counter = 5000

		# limites para enteros
		self.int_l_limit = 5000
		self.int_u_limit = 5999
		self.int_counter = 5000

		# limites para flotantes
		self.float_l_limit = 6000
		self.float_u_limit = 6999
		self.float_counter = 6000

		# limites para booleanos
		self.bool_l_limit = 7000
		self.bool_u_limit = 7999
		self.bool_counter = 7000

		# limites para cadenas
		self.str_l_limit = 8000
		self.str_u_limit = 8999
		self.str_counter = 8000
		
		# limites para caracteres
		self.char_l_limit = 9000
		self.char_u_limit = 9999
		self.char_counter = 9000

		"""
		locales:  5,000  - 9,999
			enteros:    5,000 - 5,999
			flotantes:  6,000 - 6,999
			booleanos:  7,000 - 7,999
			strings:    8,000 - 8,999
			caracteres: 9,000 - 9,999
		"""
