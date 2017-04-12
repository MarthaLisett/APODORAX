class Memory(object):

	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

	def insert_integer(self, val):
		if self.int_counter <= self.u_limit and self.int_counter >= self.l_limit:
			if self.int_counter <= self.int_u_limit and self.int_counter >= self.int_l_limit:
				self.integers[self.int_counter] = val
				self.int_counter += 1
				return self.int_counter - 1
			else:
				raise MemoryError("ERROR: ya no hay espacio para enteros.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para enteros.")

	def insert_float(self, val, var_id):
		print("en memoria con", var_id)
		if self.float_counter <= self.u_limit and self.float_counter >= self.l_limit:
			if self.float_counter <= self.float_u_limit and self.float_counter >= self.float_l_limit:
				self.floats[self.float_counter] = val
				self.float_counter += 1
				return self.float_counter - 1
			else:
				raise MemoryError("ERROR: ya no hay espacio para flotantes.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para flotantes.")

	def insert_boolean(self, val):
		print("el contador de booleanos esta en:", self.bool_counter)
		if self.bool_counter <= self.u_limit and self.bool_counter >= self.l_limit:
			if self.bool_counter <= self.bool_u_limit and self.bool_counter >= self.bool_l_limit:
				self.booleans[self.bool_counter] = val
				self.bool_counter += 1

				return self.bool_counter - 1
			else:
				raise MemoryError("ERROR: ya no hay espacio para booleanos.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para booleanos.")


	def insert_string(self, val):
		if self.str_counter <= self.u_limit and self.str_counter >= self.l_limit:
			if self.str_counter <= self.str_u_limit and self.str_counter >= self.str_l_limit:
				self.strings[self.str_counter] = val
				self.str_counter += 1
				return self.str_counter - 1
			else:
				raise MemoryError("ERROR: ya no hay espacio para cadenas.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para cadenas.")


	def insert_character(self, val):
		if self.char_counter <= self.u_limit and self.char_counter >= self.l_limit:
			if self.char_counter <= self.char_u_limit and self.char_counter >= self.char_l_limit:
				self.characters[self.char_counter] = val
				self.char_counter += 1
				return self.char_counter - 1
			else:
				raise MemoryError("ERROR: ya no hay espacio para caracteres.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para caracteres.")

	def set_val(self, var_dir, val, var_type):
		if var_type == "entero":
			if var_dir <= self.int_u_limit and var_dir >= self.int_l_limit:
				self.integers[var_dir] = val
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "flotante":
			if var_dir <= self.float_u_limit and var_dir >= self.float_l_limit:
				self.floats[var_dir] = val
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "booleano":
			if var_dir <= self.bool_u_limit and var_dir >= self.bool_l_limit:
				self.booleans[var_dir] = val
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "cadena":
			if var_dir <= self.str_u_limit and var_dir >= self.str_l_limit:
				self.strings[var_dir] = val
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "caracter":
			if var_dir <= self.char_u_limit and var_dir >= self.char_l_limit:
				self.characters[var_dir] = val
			else:
				raise MemoryError("No se encontro la direccion.")

	def get_val_from_dir(self, address):
		if address <= self.int_u_limit and address >= self.int_l_limit:
			print("se encontro:", self.integers.get(address), "en:", address)
			return self.integers.get(address)
		elif address <= self.float_u_limit and address >= self.float_l_limit:
			return self.floats.get(address)
		elif address <= self.bool_u_limit and address >= self.bool_l_limit:
			return self.booleans.get(address)
		elif address <= self.str_u_limit and address >= self.str_l_limit:
			return self.strings.get(address)
		elif address <= self.char_u_limit and address >= self.char_l_limit:
			return self.characters.get(address)
		else:
			raise MemoryError("No se encontro la direccion.")
	

	def set_val_from_dir(self, address, val):
		if address <= self.int_u_limit and address >= self.int_l_limit:
			self.integers[address] = val
		elif address <= self.float_u_limit and address >= self.float_l_limit:
			self.floats[address] = val
		elif address <= self.bool_u_limit and address >= self.bool_l_limit:
			self.booleans[address] = val
		elif address <= self.str_u_limit and address >= self.str_l_limit:
			self.strings[address] = val
		elif address <= self.char_u_limit and address >= self.char_l_limit:
			self.characters[address] = val
		else:
			raise MemoryError("No se encontro la direccion.")


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

















