class Memory(object):

	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

	def insert_integer(self, val):
		pass

	def insert_float(self, val):
		pass
	
	def insert_boolean(self, val):
		pass
	
	def insert_string(self, val):
		pass
	
	def insert_characters(self, val):
		pass
	
	def get_new_dir(self, var_type):
		pass

	def insert_integer(self, val):
		if self.int_counter <= self.u_limit and self.int_counter >= self.l_limit:
			if self.int_counter <= self.int_u_limit and self.int_counter >= self.int_l_limit:
				self.integers[self.int_counter] = val
				self.int_counter += 1
				return self.int_counter - 1
			else:
				pass
				# ERROR: ya no hay espacio
		else:
			pass
			# ERROR: ya no hay espacio

	def insert_float(self, val):
		if self.float_counter <= self.u_limit and self.float_counter >= self.l_limit:
			if self.float_counter <= self.float_u_limit and self.float_counter >= self.float_l_limit:
				self.floats[self.float_counter] = val
				self.float_counter += 1
				return self.float_counter - 1
			else:
				pass
				# ERROR: ya no hay espacio
		else:
			pass
			# ERROR: ya no hay espacio

	def insert_boolean(self, val):
		if self.bool_counter <= self.u_limit and self.bool_counter >= self.l_limit:
			if self.bool_counter <= self.bool_u_limit and self.bool_counter >= self.bool_l_limit:
				self.booleans[self.bool_counter] = val
				self.bool_counter += 1
				return self.bool_counter - 1
			else:
				pass
				# ERROR: ya no hay espacio
		else:
			pass
			# ERROR: ya no hay espacio


	def insert_string(self, val):
		if self.str_counter <= self.u_limit and self.str_counter >= self.l_limit:
			if self.str_counter <= self.str_u_limit and self.str_counter >= self.str_l_limit:
				self.strings[self.str_counter] = val
				self.str_counter += 1
				return self.str_counter - 1
			else:
				pass
				# ERROR: ya no hay espacio
		else:
			pass
			# ERROR: ya no hay espacio


	def insert_character(self, val):
		if self.char_counter <= self.u_limit and self.char_counter >= self.l_limit:
			if self.char_counter <= self.char_u_limit and self.char_counter >= self.char_l_limit:
				self.characters[self.char_counter] = val
				self.char_counter += 1
				return self.char_counter - 1
			else:
				pass
				# ERROR: ya no hay espacio
		else:
			pass
			# ERROR: ya no hay espacio

	def set_val(self, var_dir, val, var_type):
		if var_type == "entero":
			if var_dir <= self.int_u_limit and var_dir >= self.int_l_limit:
				self.integers[var_dir] = val
			else:
				pass
				# No se encontro la direccion
		elif var_type == "flotante":
			if var_dir <= self.float_u_limit and float_dir >= self.float_l_limit:
				self.floats[var_dir] = val
			else:
				pass
				# No se encontro la direccion
		elif var_type == "booleano":
			if var_dir <= self.bool_u_limit and var_dir >= self.bool_l_limit:
				self.booleans[var_dir] = val
			else:
				pass
				# No se encontro la direccion
		elif var_type == "cadena":
			if var_dir <= self.str_u_limit and var_dir >= self.str_l_limit:
				self.strings[var_dir] = val
			else:
				pass
				# No se encontro la direccion
		elif var_type == "caracter":
			if var_dir <= self.char_u_limit and var_dir >= self.char_l_limit:
				self.characters[var_dir] = val
			else:
				pass
				# No se encontro la direccion

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

















