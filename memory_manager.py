""" Clase memory_manager
Clase que se encarga de comunicar a la tabla de simbolos
con la memoria y administrar las ubicaciones de las variables
José González Ayerdi - A01036121
Martha Benavides - A01280115
03/05/2017 """
from memory        import Memory
from temporal      import Temporal
from globs         import Globs
from local         import Local
from constant      import Constant

debug = False
class memory_manager():

	def __init__(self):
		""" Inicializa los scopes de las variables : Temporales, Globales,
		Locales y Constantes.
			"""
		self.tmp   = Temporal()
		self.glob  = Globs()
		self.loc   = Local()
		self.const = Constant()
		self.max_memory = 20000
		self.current_used_memory = 0

	def free_memory(self, no_vars):
		""" Libera la memoria que ha sido utilizada por una llamada a funcion.
		Args:
			no_vars: Cantidad de variables de una funcion. """
		self.current_used_memory -= no_vars

	def check_available_memory(self, no_vars):
		""" Pide la memoria que sera utilizada por una llamada a funcion.
		Args:
			no_vars: Cantidad de variables de una funcion. """
		if self.current_used_memory + no_vars <= self.max_memory:
			self.current_used_memory += no_vars
		else:
			# muestra un error en caso de que ya no haya mas memoria.
			raise MemoryError("ERROR: ya no hay espacio en memoria.")

	def increment_address_pointer(self, var_type, var_dir, offset):
		""" Almacenar y manejar direcciones de arreglos.
		Args:
			var_dir: Diccionario del tipo de dato.
			var_type: Tipo de dato de la variable.
			offset: Tamanio del arreglo.
			"""
		# Checar la direccion y si cabe dentro de los limites de la memoria entonces
		# incrementar el contador de ese scope en la cantidad de casillas del arreglo.		
		if var_dir >= self.tmp.l_limit and var_dir <= self.tmp.u_limit:
			self.tmp.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.glob.l_limit and var_dir <= self.glob.u_limit:
			self.glob.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.loc.l_limit and var_dir <= self.loc.u_limit:
			self.loc.increment_address_pointer(var_dir, var_type, offset)
		elif var_dir >= self.const.l_limit and var_dir <= self.const.u_limit:
			self.const.increment_address_pointer(var_dir, var_type, offset)

	def set_val(self, var_dir, val, var_type):
		""" Asignar valor a las direcciones de cada scope.
		Args:
		    var_dir: Direccion de la variable.
			val: Valor de la variable.
			var_type: Tipo de dato de la variable.
			"""
		# Checar la direccion y dependiendo del mismo asignarle el valor a la
		# direccion de la variable.
		if var_dir >= self.tmp.l_limit and var_dir <= self.tmp.u_limit:
			self.tmp.set_val(var_dir, val, var_type)
		elif var_dir >= self.glob.l_limit and var_dir <= self.glob.u_limit:
			self.glob.set_val(var_dir, val, var_type)
		elif var_dir >= self.loc.l_limit and var_dir <= self.loc.u_limit:
			self.loc.set_val(var_dir, val, var_type)
		elif var_dir >= self.const.l_limit and var_dir <= self.const.u_limit:
			self.const.set_val(var_dir, val, var_type)

	
	def get_val_from_dir(self, address):
		""" Obtener el valor de una direccion.
		Args:
		    address: Direccion de la cual se quiere obtener el valor.
		Return:
		    Valor de la direccion	
			"""
		# Checar si la direccion esta dentro de los limites para ver el scope 
		# de dato que es para posteriormente obtener la direccion.

		# Usar en arreglos (numero)
		if str(address)[len(str(address)) - 1] == '_':
			return int(address[:len(str(address)) - 1])
		# Apuntador a una direccion	
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

	def set_val_from_dir(self, address, val):
		""" Asignar el valor a una direccion. Si no se encuentra la 
		direccion entonces mostrar un error.
		Args:
		    address: Direccion de la cual se quiere asignar el valor.
			val: Valor a asignar.
			"""
		# Checar si la direccion esta dentro de los limites para ver el scope
		# del dato que es para posteriormente asignarle un valor a la direccion.	

		# Apuntador a una direccion
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
	
	def insert_variable(self, var_type, var_id, var_scope, var_val):
		""" Funcion exclusiva para agregar variables locales/globales
		Args:
			var_type: El tipo de la variable.
			var_id: Id de la variable.
			var_scope: Scope de la variable.
			var_val: Valor de la variable.
		"""
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
		"""" Revisa si la variable es temporal, global o local
		Args:
			var_scope: Scope de la variable.
			var_id: id de la variable
		Regreso:
			El objeto correspondiente a la funcionalidad de la variable."""
		if var_id == "const":
			return self.const
		elif var_id[0:2] == "t_":
			return self.tmp
		elif var_scope == "global":
			return self.glob
		else:
			return self.loc

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







