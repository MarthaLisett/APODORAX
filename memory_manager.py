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

	def set_val(self, var_dir, val, var_type):
		if var_dir >= self.tmp.l_limit and var_dir <= self.tmp.u_limit:
			self.tmp.set_val(var_dir, val, var_type)
		elif var_dir >= self.glob.l_limit and var_dir <= self.glob.u_limit:
			self.glob.set_val(var_dir, val, var_type)
		elif var_dir >= self.loc.l_limit and var_dir <= self.loc.u_limit:
			self.loc.set_val(var_dir, val, var_type)
		elif var_dir >= self.const.l_limit and var_dir <= self.const.u_limit:
			self.const.set_val(var_dir, val, var_type)

	"""insert_variable funcion exclusiva para agregar variables locales/globales"""
	def insert_variable(self, var_type, var_id, var_scope, var_val):

		segment = self.check_variable_functionality(var_scope)
		
		if var_type ==  "entero":
			print("voy a regresar:", segment.insert_integer(var_val))
			return segment.insert_integer(var_val)
		elif var_type == "flotante":
			print("voy a regresar:", segment.insert_integer(var_val))
			return segment.insert_float(var_val)
		elif var_type == "booleano":
			print("voy a regresar:", segment.insert_integer(var_val))
			return segment.insert_boolean(var_val)
		elif var_type == "caracter":
			print("voy a regresar:", segment.insert_integer(var_val))
			return segment.insert_character(var_val)
		elif var_type == "cadena":
			print("voy a regresar:", segment.insert_integer(var_val))
			return segment.insert_string(var_val)

	def check_variable_functionality(self, var_scope):
		if var_scope == "global":
			return self.glob
		else:
			return self.loc
