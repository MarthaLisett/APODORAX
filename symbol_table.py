#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Clase symbol_table
Implementa funcionalidad para el manejo de las tablas
de variables y funciones para el compilador APODORAX.

José González Ayerdi - A01036121
Martha Benavides - A01280115

10/03/2017 """

class symbol_table:
	""" Constructor de la clase inicializa diccionario (que contiene las tablas)
	y el scope inicial. En el diccionario las llaves son los id de las variables
	mientras que los valores son diccionarios de variables, cuyas llaves son los
	id de las variables y sus valores son sus propiedades. """
	def __init__(self, func_dic={}, scope='global'):
		self.__func_dic           = func_dic
		self.__func_dic['global'] = (None, {})
		self.__scope              = scope

	""" search_function busca el id de una función en la tabla de funciones,
	si no la encuentra despliega un error """
	def search_function(self, fun_id):
		if fun_id not in self.__func_dic:
			raise KeyError("La funcion '" + fun_id + "' no esta desclarada.")

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
				self.__func_dic[self.__scope][1][var_id] = [var_id, var_type, self.__scope]
			else:
				raise KeyError("Variable repetida: " + "'" + var_id + "'")
		else:
			raise KeyError('Error en estructura de funciones/scope.')

	""" insert_function revisa si el id de esta funciónya existe en la tabla de funciones,
	si no existe la inserta y la inicializa con vacío como valor. """
	def insert_function(self, fun_id, return_type):
		if self.__func_dic.get(fun_id) is None:
			self.__func_dic[fun_id] = (return_type, {})
			self.set_scope(fun_id)
		else:
			raise KeyError("Funcion '" + fun_id + "' repetida.")

	""" Sección de setters """
	def set_scope(self, scope):
		self.__scope = scope

	def set_func_dic(self, func_dic):
		self.__func_dic = func_dic

	def set_var_val(self, var_id, val):
		if self. __func_dic.get(self.__scope)[1].get(var_id) is not None:
			self.__func_dic[self.__scope][1][var_id].append(val)
		else:
			self.__func_dic['global'][1][var_id].append(val)

	""" Sección de getters  """
	def get_scope(self):
		return self.__scope

	def get_func_dic(self):
		return self.__func_dic

	def get_var(self, var_id):
		if var_id  in self.__func_dic.get(self.__scope)[1]:
			return self.__func_dic.get(self.__scope)[1].get(var_id)
		elif var_id  in self.__func_dic.get('global')[1]:
			return self.__func_dic.get('global')[1].get(var_id)

	""" Sección para declarar propiedades de la clase. """
	scope    = property(get_scope, set_scope)
	func_dic = property(get_func_dic, set_func_dic)