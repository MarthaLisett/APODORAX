#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Clase symbol_table
Implementa funcionalidad para el manejo de las tablas
de variables y funciones para el compilador APODORAX.
José González Ayerdi - A01036121
Martha Benavides - A01280115
10/03/2017 """
from collections import OrderedDict
from memory_manager import memory_manager
mm = memory_manager()
const_counter = 0

class symbol_table:
	""" Constructor de la clase inicializa diccionario (que contiene las tablas)
	y el scope inicial. En el diccionario las llaves son los id de las variables
	mientras que los valores son diccionarios de variables, cuyas llaves son los
	id de las variables y sus valores son sus propiedades. """
	def __init__(self, func_dic={}, scope='global'):
		self.__func_dic           = func_dic
		self.__func_dic['global'] = (None, OrderedDict())
		self.__scope              = scope
		self.__no_params          = {}
		self.__var_count          = {}
		self.__quadruple_count    = {}
		self.__dim_vars           = {}

	def add_function_as_var(self, fun_id, return_type):
		global mm
		new_dir = mm.insert_variable(return_type, fun_id, 'global', None)
		self.__func_dic['global'][1][fun_id] = [fun_id, return_type, 'global', None, new_dir, False]

	def print_var_table(self, fun_id):
		table = self.__func_dic[fun_id]
		for var_table in table:
			print(var_table)

	def get_param_type(self, fun_id, k):
		key = self.__func_dic[fun_id][1].keys()[k]
		return self.__func_dic[fun_id][1][key][1]

	def add_quadruple_count(self, counter):
		self.__quadruple_count[self.__scope] = counter

	def get_quadruple_count(self, scope):
		return self.__quadruple_count.get(scope)

	def add_var_count(self, var_count):
		print("la funcion:", self.__scope, "tiene:", var_count, "locales !=")
		param_count = 0
		if self.__scope != "main" and self.__scope != "global":
			param_count = self.get_no_params(self.__scope)
		self.__var_count[self.__scope] = var_count + param_count

	def get_var_count(self, scope):
		return self.__var_count.get(scope)

	def add_no_params(self, num_args):
		self.__no_params[self.__scope] = num_args

	def get_no_params(self, fun_id):
		return self.__no_params.get(fun_id)

	""" search_function busca el id de una función en la tabla de funciones,
	si no la encuentra despliega un error """
	def search_function(self, fun_id):
		if fun_id not in self.__func_dic:
			raise KeyError("La funcion '" + fun_id + "' no esta declarada.")

	def function_exists(self, fun_id):
		return fun_id in self.__func_dic

	""" search_variable busca el id de una vairable primero dentro del scope actual,
	si no la encuentra busca en el scope global, si no la encuentra despliega un error. """
	def search_variable(self, var_id):
		if self. __func_dic.get(self.__scope)[1].get(var_id) is None:
			if self.__func_dic.get('global')[1].get(var_id) is None:
				raise KeyError('La variable: ' + var_id + ' no ha sido declarada.')

	""" insert_variable busca enla tabla de variables (dado un scope) si la variable existe,
	si no existe la agrega a la tabla, de lo contrario despliega un error. """
	def insert_variable(self, var_type, var_id):
		if self.__func_dic.get(self.__scope) is not None:
			if self.__func_dic.get(self.__scope)[1].get(var_id) is None:
				global mm
				new_dir = mm.insert_variable(var_type, var_id, self.__scope, None)
				print("a",var_id,"se le asigno",new_dir)
				self.__func_dic[self.__scope][1][var_id] = [var_id, var_type, self.__scope, None, new_dir, False]
			else:
				raise KeyError("Variable repetida: " + "'" + var_id + "'")
		else:
			raise KeyError('Error en estructura de funciones/scope.')

	""" metodos para arreglos """
	def set_dim_flag(self, var_id):
		self.__func_dic[self.__scope][1][var_id][5] = True
		# dim, l_inf, l_sup, k, r, aux, base_dir
		self.__dim_vars[var_id] = [1, 0, None, None, 1, None, None]

	def set_vector_limits(self, u_limit, var_id):
		print("u_limit:-", u_limit)
		self.__dim_vars[var_id][2] = u_limit - 1
		u_limit = self.__dim_vars.get(var_id)[2]
		l_limit = self.__dim_vars.get(var_id)[1]
		r = self.__dim_vars.get(var_id)[4]
		r = (u_limit - l_limit + 1) * r
		self.__dim_vars[var_id][4] = r
		self.__dim_vars[var_id][5] = r
		global mm
		base_dir = self.__func_dic[self.__scope][1][var_id][4]
		var_type = self.__func_dic[self.__scope][1][var_id][1]
		aux = self.__dim_vars.get(var_id)[5]
		mm.increment_address_pointer(var_type, base_dir, aux)
		print("el arreglo cubre desde:", base_dir, "hasta", base_dir+aux)

	def calculate_k(self, var_id):
		k = 0
		u_limit = self.__dim_vars.get(var_id)[2]
		l_limit = self.__dim_vars.get(var_id)[1]
		r = self.__dim_vars.get(var_id)[4]
		r = r / (u_limit - l_limit + 1)
		k += l_limit * r
		self.__dim_vars[var_id][3] = k * (-1)
		print("el valor de k es:", k)

	def add_constant_to_memory(self, val, val_type):
		global mm
		global const_counter
		new_dir = mm.insert_variable(val_type, "const", "const_" + str(const_counter), val)
		const_counter += 1
		return new_dir

	""" insert_function revisa si el id de esta funciónya existe en la tabla de funciones,
	si no existe la inserta y la inicializa con vacío como valor. """
	def insert_function(self, fun_id, return_type):
		if self.__func_dic.get(fun_id) is None:
			self.__func_dic[fun_id] = (return_type, OrderedDict())
			self.set_scope(fun_id)
		else:
			raise KeyError("Funcion '" + fun_id + "' repetida.")

	""" Sección de setters """
	def set_scope(self, scope):
		self.__scope = scope

	def set_func_dic(self, func_dic):
		self.__func_dic = func_dic

	def set_var_val(self, var_id, val):
		global mm
		if self. __func_dic.get(self.__scope)[1].get(var_id) is not None:
			self.__func_dic[self.__scope][1][var_id][3] = val
			print("Estoy buscando", var_id)
			var_dir = self.__func_dic[self.__scope][1][var_id][4]
			var_type = self.__func_dic[self.__scope][1][var_id][1]
			print("dentro de if id:",var_id,var_dir)
			mm.set_val(var_dir, val, var_type)
		else:
			self.__func_dic['global'][1][var_id][3] = val
			var_dir = self.__func_dic['global'][1][var_id][4]
			print("dentro de else id:",var_id,var_dir)
			var_type = self.__func_dic['global'][1][var_id][1]
			mm.set_val(var_dir, val, var_type)

	""" Sección de getters """
	def get_scope(self):
		return self.__scope

	def get_func_dic(self):
		return self.__func_dic

	def get_val_from_dir(self, address):
		global mm
		return mm.get_val_from_dir(address)

	def set_val_from_dir(self, address, val):
		global mm
		mm.set_val_from_dir(address, val)

	def get_var(self, var_id):
		if var_id  in self.__func_dic.get(self.__scope)[1]:
			print("dir de tmp en if:", self.__func_dic.get(self.__scope)[1].get(var_id))
			return self.__func_dic.get(self.__scope)[1].get(var_id)
		elif var_id  in self.__func_dic.get('global')[1]:
			print("dir de tmp en else:", self.__func_dic.get(self.__scope)[1].get(var_id))
			return self.__func_dic.get('global')[1].get(var_id)

	def get_var_type(self, var_id):
		if var_id in self.__func_dic.get(self.__scope)[1]:
			return self.__func_dic.get(self.__scope)[1].get(var_id)[1]
		elif var_id in self.__func_dic.get('global')[1]:
			return self.__func_dic.get('global')[1].get(var_id)[1]

	""" Sección para declarar propiedades de la clase. """
	scope    = property(get_scope, set_scope)
	func_dic = property(get_func_dic, set_func_dic)