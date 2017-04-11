from memory import Memory

class Temporal(Memory):
	
	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

		self.l_limit = 10000
		self.u_limit = 14999
		self.dir_counter = 10000

		self.int_l_limit = 10000
		self.int_u_limit = 10999
		self.int_counter = 10000

		self.float_l_limit = 11000
		self.float_u_limit = 11999
		self.float_counter = 11000

		self.bool_l_limit = 12000
		self.bool_u_limit = 12999
		self.bool_counter = 12000

		self.str_l_limit = 13000
		self.str_u_limit = 13999
		self.str_counter = 13000

		self.char_l_limit = 14000
		self.char_u_limit = 14999
		self.char_counter = 14000

"""
	temps:    10,000 - 14,999
		enteros:    10,000 - 10,999
		flotantes:  11,000 - 11,999
		booleanos:  12,000 - 12,999
		strings:    13,000 - 13,999
		caracteres: 14,000 - 14,999
"""



