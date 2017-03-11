class symbol_table:
	def __init__(self, func_dic={}, scope='global'):
		self.__func_dic           = func_dic
		self.__func_dic['global'] = {}
		self.__scope              = scope

	def set_scope(self, scope):
		self.__scope = scope

	def get_scope(self):
		return self.__scope

	def set_func_dic(self, func_dic):
		self.__func_dic = func_dic
	
	def get_func_dic(self):
		return self.__func_dic

	def search_function(self, fun_id):
		if fun_id not in self.__func_dic:
			raise KeyError("La funcion '" + fun_id + "' no esta desclarada.")

	def search_variable(self, var_id):
		if self. __func_dic.get(self.__scope).get(var_id) is None:
			if self.__func_dic.get('global').get(var_id) is None:
				raise KeyError('La variable: ' + var_id + ' no ha sido declarada.')

	def insert_variable(self, var_type, var_id):
		if self.__func_dic.get(self.__scope) is not None:
			if self.__func_dic.get(self.__scope).get(var_id) is None:
				self.__func_dic[self.__scope][var_id] = [var_id, var_type, self.__scope]
			else:
				raise KeyError("Variable repetida: " + "'" + var_id + "'")
		else:
			raise KeyError('Error en estructura de funciones/scope.')

	def insert_function(self, fun_id):
		if self.__func_dic.get(fun_id) is None:
			self.__func_dic[fun_id] = {}
			self.set_scope(fun_id)
		else:
			raise KeyError("Funcion '" + fun_id +"' repetida.")

	scope    = property(get_scope, set_scope)
	func_dic = property(get_func_dic, set_func_dic)