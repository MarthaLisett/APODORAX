from memory import Memory

class Constant(Memory):
	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

		self.l_limit = 15000
		self.u_limit = 19999
		self.dir_counter = 15000

		self.int_l_limit = 15000
		self.int_u_limit = 15999
		self.int_counter = 15000

		self.float_l_limit = 16000
		self.float_u_limit = 16999
		self.float_counter = 16000

		self.bool_l_limit = 17000
		self.bool_u_limit = 17999
		self.bool_counter = 17000

		self.str_l_limit = 18000
		self.str_u_limit = 18999
		self.str_counter = 18000

		self.char_l_limit = 19000
		self.char_u_limit = 19999
		self.char_counter = 19000

		"""
		ctes:     15,000 - 19,999
			enteros:    15,000 - 15,999
			flotantes:  16,000 - 16,999
			booleanos:  17,000 - 17,999
			strings:    18,000 - 18,999
			caracteres: 19,000 - 19,999
		"""

