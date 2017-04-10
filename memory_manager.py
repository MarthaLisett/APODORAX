from memory        import Memory
from temporal      import Temporal
from globs         import Globs
from local         import Local
from constant      import Constant

class memory_manager():

	def __init__(self):
		self.tmp   = Temporal()
		self.glob  = Globs()
		self.loc   = Local()
		self.const = Constant()

	"""insert_variable funcion exclusiva para agregar variables locales/globales"""
	def insert_variable(self, var_type, var_id, var_scope, var_val):

		segment = self.check_variable_functionality(var_scope)
		
		if var_type ==  "entero":
			return segment.insert_integer(var_val)
		elif var_type == "flotante":
			return segment.insert_float(var_val)
		elif var_type == "booleano":
			return segment.insert_boolean(var_val)
		elif var_type == "caracter":
			return segment.insert_carater(var_val)
		elif var_type == "cadena":
			return segment.insert_string(var_val)

	def check_variable_functionality(self, var_scope):
		if var_scope == "global":
			return self.glob
		else:
			return self.loc
