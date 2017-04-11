from memory import Memory

class Globs(Memory):

	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

		self.l_limit = 0
		self.u_limit = 4999
		self.dir_counter = 0 # checar que hacer con esto

		self.int_l_limit = 0
		self.int_u_limit = 999
		self.int_counter = 0

		self.float_l_limit = 1000
		self.float_u_limit = 1999
		self.float_counter = 0

		self.bool_l_limit = 2000
		self.bool_u_limit = 2999
		self.bool_counter = 0

		self.str_l_limit = 3000
		self.str_u_limit = 3999
		self.str_counter = 0

		self.char_l_limit = 4000
		self.char_u_limit = 4999
		self.char_counter = 0

	"""
	globales:       0     - 4,999
		enteros:    0     - 999
		flotantes:  1,000 - 1,999
		booleanos:  2,000 - 2,999
		strings:    3,000 - 3,999
		caracteres: 4,000 - 4,999
	"""




