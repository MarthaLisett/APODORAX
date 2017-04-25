from memory        import Memory
from temporal      import Temporal
from globs         import Globs
from local         import Local
from constant      import Constant

debug = False
class memory_manager():

	def __init__(self):
		self.tmp   = Temporal()
		self.glob  = Globs()
		self.loc   = Local()
		self.const = Constant()


	def increment_address_pointer(self, var_type, var_dir, offset):
		if var_dir >= self.tmp.l_limit and var_dir <= self.tmp.u_limit:
			self.tmp.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.glob.l_limit and var_dir <= self.glob.u_limit:
			self.glob.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.loc.l_limit and var_dir <= self.loc.u_limit:
			self.loc.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.const.l_limit and var_dir <= self.const.u_limit:
			self.const.increment_address_pointer(var_dir, var_type, offset)

	def set_val(self, var_dir, val, var_type):
		if var_dir >= self.tmp.l_limit and var_dir <= self.tmp.u_limit:
			self.tmp.set_val(var_dir, val, var_type)
		elif var_dir >= self.glob.l_limit and var_dir <= self.glob.u_limit:
			self.glob.set_val(var_dir, val, var_type)
		elif var_dir >= self.loc.l_limit and var_dir <= self.loc.u_limit:
			self.loc.set_val(var_dir, val, var_type)
		elif var_dir >= self.const.l_limit and var_dir <= self.const.u_limit:
			self.const.set_val(var_dir, val, var_type)

	# '_12332' => 12332 -> dir -> val
	def get_val_from_dir(self, address):
		if str(address)[len(str(address)) - 1] == '_':
			return int(address[:len(str(address)) - 1])
		if str(address)[0] == '_':
			meta_address = self.get_val_from_dir(int(address[1:]))
			return self.get_val_from_dir(meta_address)
		if address >= self.tmp.l_limit and address <= self.tmp.u_limit:
			return self.tmp.get_val_from_dir(address)
		elif address >= self.glob.l_limit and address <= self.glob.u_limit:
			return self.glob.get_val_from_dir(address)
		elif address >= self.loc.l_limit and address <= self.loc.u_limit:
			return self.loc.get_val_from_dir(address)
		elif address >= self.const.l_limit and address <= self.const.u_limit:
			return self.const.get_val_from_dir(address)

	# '_12332' => 12332 -> dir -> val
	def set_val_from_dir(self, address, val):
		if str(address)[0] == '_':
			address = self.get_val_from_dir(int(address[1:]))
		if address >= self.tmp.l_limit and address <= self.tmp.u_limit:
			self.tmp.set_val_from_dir(address, val)
		elif address >= self.glob.l_limit and address <= self.glob.u_limit:
			self.glob.set_val_from_dir(address, val)
		elif address >= self.loc.l_limit and address <= self.loc.u_limit:
			self.loc.set_val_from_dir(address, val)
		elif address >= self.const.l_limit and address <= self.const.u_limit:
			self.const.set_val_from_dir(address, val)

	"""
	globales:       0     - 4,999
		enteros:    0     - 999
		flotantes:  1,000 - 1,999
		booleanos:  2,000 - 2,999
		strings:    3,000 - 3,999
		caracteres: 4,000 - 4,999
	locales:  5,000  - 9,999
		enteros:    5,000 - 5,999
		flotantes:  6,000 - 6,999
		booleanos:  7,000 - 7,999
		strings:    8,000 - 8,999
		caracteres: 9,000 - 9,999
	temps:    10,000 - 14,999
		enteros:    10,000 - 10,999
		flotantes:  11,000 - 11,999
		booleanos:  12,000 - 12,999
		strings:    13,000 - 13,999
		caracteres: 14,000 - 14,999
	ctes:     15,000 - 19,999
		enteros:    15,000 - 15,999
		flotantes:  16,000 - 16,999
		booleanos:  17,000 - 17,999
		strings:    18,000 - 18,999
		caracteres: 19,000 - 19,999
	"""

	"""insert_variable funcion exclusiva para agregar variables locales/globales"""
	def insert_variable(self, var_type, var_id, var_scope, var_val):
		global debug
		segment = self.check_variable_functionality(var_scope, var_id)
		if debug : print("llego la variable", var_id, "de tipo", var_type, "para el segmento de", segment)

		if var_type ==  "entero":
			return segment.insert_integer(var_val)
		elif var_type == "flotante":
			return segment.insert_float(var_val, var_id)
		elif var_type == "bool":
			return segment.insert_boolean(var_val)
		elif var_type == "caracter":
			return segment.insert_character(var_val)
		elif var_type == "cadena":
			return segment.insert_string(var_val)

	def check_variable_functionality(self, var_scope, var_id):
		if var_id == "const":
			return self.const
		elif var_id[0:2] == "t_":
			return self.tmp
		elif var_scope == "global":
			return self.glob
		else:
			return self.loc





