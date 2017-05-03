from graphics_drawer import Graphics
from stack           import Stack
from queue           import Queue
import copy

class virtual_machine:
	def __init__(self):
		pass

	def start_execution(self, st, quadruples):
		"""Da inicio a la fase de ejecucion del programa leyendo el archivo
		generado en tiempo de compilacion analizando los cuadruplos con instrucciones
		y manejando la memoria de acuerdo a esas instrucciones para producit un resultado final.
		Args:
			st: referencia a la tabla de simbolos para tener acceso a direcciones y valores.
			quadruples: Diccionario de cuadruplos que contienen las instrucciones a seguir.
			"""
		# Codigo para depurar
		debug = False
		if debug :
			print("buscando:", dir_izq)
			print("buscando:", dir_der)
			print("buscando:", dir_res)
		
		# Lista de funciones predefinidas
		predefined_functions = [
								"insertaTexto", "insertaTriangulo", "insertaRectangulo", "insertaLinea",
								"insertaCirculo", "insertaOvalo", "insertaPunto", "insertaCurva",
								]
		# Variables utiles para el recorrido de los cuadruplos
		graphics        = None
		arg_dirs        = []
		actual_quad     = 0
		return_quad     = 0
		found_return    = False
		actual_fun      = ""
		fun_calls       = Queue()
		execution_stack = Stack()
		called_predefined_fun = False

		# Comienza la lectura de los cuadruplos
		while actual_quad < len(quadruples):
			# Instrucciones correspondientes a la asignacion
			if quadruples[actual_quad][0] == '=':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				st.set_val_from_dir(dir_der, val_izq)

			# Instrucciones correspondientes a la suma
			elif quadruples[actual_quad][0] == '+':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq + val_der
				st.set_val_from_dir(dir_res, result)

			# Instrucciones correspondientes a la resta
			elif quadruples[actual_quad][0] == '-':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq - val_der
				st.set_val_from_dir(dir_res, result)

			# Instrucciones correspondientes a la multiplicacion
			elif quadruples[actual_quad][0] == '*':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq * val_der
				st.set_val_from_dir(dir_res, result)

			# Instrucciones correspondientes a la division
			elif quadruples[actual_quad][0] == '/':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)

				# Valida division entre 0
				if val_der == 0 or val_der == 0.0:
					raise ZeroDivisionException('Division entre 0.')
				result  =  val_izq / val_der
				st.set_val_from_dir(dir_res, result)

			# Instrucciones correspondientes a la escritura
			elif quadruples[actual_quad][0] == "escritura":
				val = st.get_val_from_dir(quadruples[actual_quad][3])
				print(val)

			# Instrucciones correspondientes a la entrada
			elif quadruples[actual_quad][0] == "entrada":
				val = str(raw_input("Introduzca un valor: "))
				# Se intenta convertir el valor a entero, sino, se queda como cadena
				try: 
					val = int(val)
				except ValueError:
					pass
				var_dir = quadruples[actual_quad][3]
				st.set_val_from_dir(var_dir, val)

			# Instrucciones correspondientes a la conjuncion
			elif quadruples[actual_quad][0] == "&&":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq == "verdadero" and val_der == "verdadero":
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes a la disjuncion
			elif quadruples[actual_quad][0] == "||":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq == "verdadero" or val_der == "verdadero":
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes a la diferencia
			elif quadruples[actual_quad][0] == "!=":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq != val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes a la equivalencia
			elif quadruples[actual_quad][0] == "==":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq == val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes al mayor-que
			elif quadruples[actual_quad][0] == ">":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq > val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes al menor-que
			elif quadruples[actual_quad][0] == "<":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq < val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes al mayor-o-igual-que
			elif quadruples[actual_quad][0] == ">=":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq >= val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes al menor-o-igual-que
			elif quadruples[actual_quad][0] == "<=":
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_izq <= val_der:
					st.set_val_from_dir(dir_res, "verdadero")
				else:
					st.set_val_from_dir(dir_res, "falso")

			# Instrucciones correspondientes al goto en falso
			elif quadruples[actual_quad][0] == "GotoF":
				# Obtenemos el valor de la direccion
				result = st.get_val_from_dir(quadruples[actual_quad][1])
				# Si resulta ser falso
				if result == "falso":
					# Calculamos el numero de cuadruplo hacia el que hay que saltar
					step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
					actual_quad += step

			# Instrucciones correspondientes al goto
			elif quadruples[actual_quad][0] == "Goto":
				# Calculamos el numero de cuadruplo al que hay que ir y vamos
				step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
				actual_quad += step
 
			# # Instrucciones correspondientes a la instruccion era
			elif quadruples[actual_quad][0] == "ERA":
				st.check_available_memory(st.get_var_count(quadruples[actual_quad][1]))
				# Si no se trata de una llamada a una funcion predefinida
				if not quadruples[actual_quad][1] in predefined_functions:
					# Y si no es una llamada desde la funcion principal
					if not execution_stack.isEmpty():
						# Guardamos el estado actual de la funcion por medio de su tabla de variables
						var_table   = copy.deepcopy(st.get_func_dic().get(fun_calls.dequeue())[1])
						"""	
						if debug : print("ERA")		
						if not execution_stack.peek()[0] == None:
							if debug : print("Anteriormente")
							for var_id, lst in execution_stack.peek()[0].iteritems():
								if debug : print("direccion virtual:", lst[4])
								if debug : print("valor:", lst[3])
						"""
						# Obtenemos los valores de las variables locales
						for var_id, lst in var_table.iteritems():
							lst[3] = copy.deepcopy(st.get_val_from_dir(lst[4]))
							if debug : print("direccion virtual:", lst[4])
							if debug : print("valor:", lst[3])
						saved_fun   = [var_table, None]
						# Guardamos la tabla de la funcion en la pila de ejecucion
						execution_stack.push(list(saved_fun))

				# Eliminamos lista con direcciones de argumentos de funciones pasadas
				del arg_dirs[:]

				# Llevamos un registro de las llamadas a funciones que se han hecho antes
				# para poder accesar a la propia funcion mientras se esta dentro de ella.
				# El nombre se guardo en fun_calls desede que se llamo
				scope = quadruples[actual_quad][1]
				var_table = st.get_func_dic().get(scope)[1]
				fun_calls.enqueue(scope)
				# Codigo para depurar
				if debug:
					for calls in fun_calls.items:
						print("tengo:", calls)
				no_vars = st.get_var_count(scope)

				# Guardamos las direcciones de las variables locales en una lista
				# para poder despues usar esas direcciones al asignar valores a los parametros
				for var_id, var_lst in var_table.iteritems():
					arg_dirs.append(var_lst[4])
				
				"""
				for p_dir in arg_dirs:
					if debug : print(p_dir)
				
				if debug : print("diccionario con variables:")
				for k, v in var_table.iteritems():
					if debug : print("var", k)
					for e in v:
						if debug : print(e)
				"""
			# Instrucciones correspondientes a los parametros encontrados
			elif quadruples[actual_quad][0] == "PARAMETER":
				# Obtenemos el valor del argumento
				val = st.get_val_from_dir(quadruples[actual_quad][1])
				# Buscamos la posicion del parametro al que corresponde
				param_position = quadruples[actual_quad][3][5:]
				# Le asignamos el valor del argumento
				st.set_val_from_dir(arg_dirs[int(param_position)], val)

			# # Instrucciones correspondientes a la instruccion gosub
			elif quadruples[actual_quad][0] == "GOSUB":
				fun_name = quadruples[actual_quad][1]
				# Si la funcion pertenece a una de las predefinidas
				if fun_name in predefined_functions:
					called_predefined_fun = True
					if graphics is None:
						# Inicializamos la libreria de graficos
					 	graphics = Graphics()
					argument_lst = []
					# Guardamos en una lista los valores de los parametros correspondientes
					for arg_dir in arg_dirs:
						arg = st.get_val_from_dir(arg_dir)
						argument_lst.append(arg)
					# Construimos la figura en base a las especificaciones
					graphics.build_figure(fun_name, argument_lst)
				else:
					# Si se trata de una llamada a una funcion definida
					# Se guarda el cuadruplo actual y se cambia para
					# apuntar al numero de cuadruplo donde esta esa funcion
					return_quad  = actual_quad + 1
					actual_quad  = st.get_quadruple_count(fun_name) - 1
					# Si se llama desde la funcion principal 
					# no se guarda ningun estado
					if execution_stack.isEmpty():
						saved_fun = [None, return_quad]
					else:
						# Si se llama desde otra funcion (puede ser recursiva)
						# Sacamos la funcion que se agrego que es la que se esta llamando
						# de la pila de ejecucion.
						# Le damos un valor a su cuadruplo de retorno,
						saved_fun    = execution_stack.pop()
						saved_fun[1] = return_quad
					# Se agrega/regresa la funcion a la pila de ejecucion
					execution_stack.push(list(saved_fun))

			# Instrucciones correspondientes a la instruccion de terminacion de una funcion
			elif quadruples[actual_quad][0] == "ENDPROC":
				# Obtenemos la tabla de memoria que se habia guardado
				# reestablecemos el contador de cuadruplos
				# y los valores de la funcion guardada se restablecen
				# a menos que se trate de la funcion principal
				saved_fun   = execution_stack.pop()
				actual_quad = saved_fun[1] - 1
				if debug : print("desde endproc voy a regresar a:", actual_quad)
				if not execution_stack.isEmpty():
					if not saved_fun[0] is None:
						for var_id, lst in saved_fun[0].iteritems():
							if debug : print("direccion virtual:", lst[4])
							if debug : print("valor:", lst[3])
							st.set_val_from_dir(lst[4], lst[3])
				else:
					# Ya se termino de procesar esa funcion entonces ya no es necesario su nombre
					st.free_memory(st.get_var_count(fun_calls.dequeue()))

			# Instrucciones correspondientes al regreso de un valor
			elif quadruples[actual_quad][0] == "RETURN":
				# Obtenemos la direccion de la variable que representa a la funcion
				# que se acaba de llamar.
				fun_dir = st.get_func_dic().get("global")[1].get(fun_calls.peek())[4]
				# Obtenemos el valor que se quiere regresar y se le asigna
				# a la direccion especificada en el cuadruplo.
				var_dir = quadruples[actual_quad][1]
				val     = st.get_val_from_dir(var_dir)
				st.set_val_from_dir(fun_dir, val)
				"""
				saved_fun   = execution_stack.pop()
				if not execution_stack.isEmpty():
					for var_id, lst in saved_fun[0].iteritems():
						st.set_val_from_dir(lst[4], lst[3])
				else:
					fun_calls.dequeue()
				
				found_return = True
				"""
			# Instrucciones correspondientes a la verificacion de los limites de un vector
			elif quadruples[actual_quad][0] == "VER":
				index = quadruples[actual_quad][1]
				l_limit = quadruples[actual_quad][2]
				u_limit = quadruples[actual_quad][3]
				index = st.get_val_from_dir(index)
				if index < l_limit or index > u_limit:
					raise IndexError("Se intento acceder a un espacio fuera del arreglo.")

			actual_quad += 1
		# Si se hizo una llamada a una funcion predefinida entonces se debe dibujar hasta el final 
		# para evitar la aparicion de multiples ventanas
		if called_predefined_fun:
			graphics.display_graphics();















