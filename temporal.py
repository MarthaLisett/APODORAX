from memory import Memory

class Temporal(Memory):

	"""
	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		Memory.__init__(self, integers, floats, booleans, strings, characters)
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters
	"""

	def __init__(self):
		self.l_limit = None