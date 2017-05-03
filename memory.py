class Memory(object):
	def __init__(self, integers={}, floats={}, booleans={}, strings={}, characters={}):
		""" Inicializa las variables de cada tipo de dato.
		Args:
			integers: Diccionario de enteros.
			floats: Diccionario de flotantes.
			booleans: Diccionario de bools.
			strings: Diccionario de strings.
			characters: Diccionario de caracteres.
			"""
		# Asigna al diccionario el valor de cada tipo de dato.	
		self.integers   = integers
		self.floats     = floats
		self.booleans   = booleans
		self.strings    = strings
		self.characters = characters

	def insert_integer(self, val):
		"""Agrega un valor entero al diccionario de enteros. Revisa que el numero quepa
		dentro de los limites establecidos para el tipo de dato, si se inserta en el
		diccionario entonces el contador se incrementara en 1, de lo contrario mandara
		un mensaje de error.
		Args:
			val: Valor del entero.
		Return:
		    int_counter - 1: Direccion donde fue almacenado el valor
			"""
		# Checar que el numero quepa dentro de los limites establecidos en la memoria 
		if self.int_counter <= self.u_limit and self.int_counter >= self.l_limit:
			if self.int_counter <= self.int_u_limit and self.int_counter >= self.int_l_limit:
				self.integers[self.int_counter] = val
				# Incrementar el contador de enteros en 1.
				self.int_counter += 1
				# Regresar la direccion
				return self.int_counter - 1
			# Mostrar errores si ya no hay espacio disponible en memoria.	
			else:
				raise MemoryError("ERROR: ya no hay espacio para enteros.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para enteros.")

	def insert_float(self, val,var_id):
	    """Agrega un valor flotante al diccionario de flotantes. Revisa que el numero quepa
		dentro de los limites establecidos para el tipo de dato, si se inserta en el
		diccionario entonces el contador se incrementara en 1, de lo contrario mandara
		un mensaje de error.
		Args:
			val: Valor del flotante.
			var_id: Usado para hacer pruebas
		Return:
		    float_counter - 1: Direccion donde fue almacenado el valor
			"""
		# Checar que el numero quepa dentro de los limites establecidos en la memoria 	
	    if self.float_counter <= self.u_limit and self.float_counter >= self.l_limit:
			if self.float_counter <= self.float_u_limit and self.float_counter >= self.float_l_limit:
				self.floats[self.float_counter] = val
				# Incrementar el contador de flotantes en 1.
				self.float_counter += 1
				# Regresar la direccion
				return self.float_counter - 1
			# Mostrar errores si ya no hay espacio disponible en memoria.		
			else:
				raise MemoryError("ERROR: ya no hay espacio para flotantes.")
	    else:
			raise MemoryError("ERROR: ya no hay espacio para flotantes.")


	def insert_boolean(self, val):
		"""Agrega un valor bool al diccionario de booleans. Revisa que la variable quepa
		dentro de los limites establecidos para el tipo de dato, si se inserta en el
		diccionario entonces el contador se incrementara en 1, de lo contrario mandara
		un mensaje de error.
		Args:
			val: Valor del bool.
		Return:
		    bool_counter - 1: Direccion donde fue almacenado el valor
			"""
		if self.bool_counter <= self.u_limit and self.bool_counter >= self.l_limit:
			if self.bool_counter <= self.bool_u_limit and self.bool_counter >= self.bool_l_limit:
				self.booleans[self.bool_counter] = val
				# Incrementar el contador de booleans en 1.
				self.bool_counter += 1
                # Regresar la direccion
				return self.bool_counter - 1
			# Mostrar errores si ya no hay espacio disponible en memoria.		
			else:
				raise MemoryError("ERROR: ya no hay espacio para booleanos.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para booleanos.")


	def insert_string(self, val):
		"""Agrega una cadena al diccionario de strings. Revisa que la variable quepa
		dentro de los limites establecidos para el tipo de dato, si se inserta en el
		diccionario entonces el contador se incrementara en 1, de lo contrario mandara
		un mensaje de error.
		Args:
			val: Valor de la cadena.
		Return:
		    str_counter - 1: Direccion donde fue almacenado el valor
			"""
		if self.str_counter <= self.u_limit and self.str_counter >= self.l_limit:
			if self.str_counter <= self.str_u_limit and self.str_counter >= self.str_l_limit:
				self.strings[self.str_counter] = val
				# Incrementar el contador de strings en 1.
				self.str_counter += 1
				# Regresar la direccion
				return self.str_counter - 1
			# Mostrar errores si ya no hay espacio disponible en memoria.	
			else:
				raise MemoryError("ERROR: ya no hay espacio para cadenas.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para cadenas.")


	def insert_character(self, val):
		"""Agrega una caracter al diccionario de characters. Revisa que la variable quepa
		dentro de los limites establecidos para el tipo de dato, si se inserta en el
		diccionario entonces el contador se incrementara en 1, de lo contrario mandara
		un mensaje de error.
		Args:
			val: Valor del caracter.
		Return:
		    char_counter - 1: Direccion donde fue almacenado el valor
			"""
		if self.char_counter <= self.u_limit and self.char_counter >= self.l_limit:
			if self.char_counter <= self.char_u_limit and self.char_counter >= self.char_l_limit:
				self.characters[self.char_counter] = val
				# Incrementar el contador de caracteres en 1.
				self.char_counter += 1
				# Regresar la direccion
				return self.char_counter - 1
			# Mostrar errores si ya no hay espacio disponible en memoria.	
			else:
				raise MemoryError("ERROR: ya no hay espacio para caracteres.")
		else:
			raise MemoryError("ERROR: ya no hay espacio para caracteres.")


	def increment_address_pointer(self, var_dir, var_type, offset):
		"""Almacenar y manejar direcciones de arreglos. Si no se encuentra la 
		direccion entonces mostrar un error.
		Args:
			var_dir: Diccionario del tipo de dato.
			var_type: Tipo de dato de la variable.
			offset: Tamanio del arreglo.
			"""
		# Checar el tipo y si cabe dentro de los limites de la memoria entonces
		# incrementar el contador de ese tipo en la cantidad de casillas del arreglo.	
		if var_type == "entero":
			if var_dir <= self.int_u_limit and var_dir >= self.int_l_limit:
				self.int_counter += offset - 1
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "flotante":
			if var_dir <= self.float_u_limit and var_dir >= self.float_l_limit:
				self.float_counter += offset - 1
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "booleano":
			if var_dir <= self.bool_u_limit and var_dir >= self.bool_l_limit:
				self.bool_counter += offset - 1
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "cadena":
			if var_dir <= self.str_u_limit and var_dir >= self.str_l_limit:
				self.str_counter += offset - 1
			else:
				raise MemoryError("No se encontro la direccion.")
		elif var_type == "caracter":
			if var_dir <= self.char_u_limit and var_dir >= self.char_l_limit:
				self.char_counter += offset - 1
			else:
				raise MemoryError("No se encontro la direccion.")

	def set_val(self, var_dir, val, var_type):
		"""Asignar valor a las direcciones de cada tipo. Si no se encuentra la 
		direccion entonces mostrar un error.
		Args:
		    var_dir: Direccion de la variable.
			val: Valor de la variable.
			var_type: Tipo de dato de la variable.
			"""
		# Checar el tipo de dato y dependiendo del mismo asignarle el valor a la
		# direccion de la variable.
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
		""" Obtener el valor de una direccion. Si no se encuentra la 
		direccion entonces mostrar un error.
		Args:
		    address: Direccion de la cual se quiere obtener el valor.
		Return:
		    Valor de la direccion	
			"""
		# Checar si la direccion esta dentro de los limites para ver el tipo 
		# de dato que es para posteriormente obtener la direccion.	
		if address <= self.int_u_limit and address >= self.int_l_limit:
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
		""" Asignar el valor a una direccion. Si no se encuentra la 
		direccion entonces mostrar un error.
		Args:
		    address: Direccion de la cual se quiere asignar el valor.
			val: Valor a asignar.
			"""
		# Checar si la direccion esta dentro de los limites para ver el tipo 
		# de dato que es para posteriormente asignarle un valor a la direccion.		
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

















