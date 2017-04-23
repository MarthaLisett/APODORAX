from graphics_drawer import Graphics
from stack           import Stack
from queue           import Queue
import copy

class virtual_machine:
	def __init__(self):
		pass

	def start_execution(self, st, quadruples):
		"""
		print("buscando:", dir_izq)
		print("buscando:", dir_der)
		print("buscando:", dir_res)
		"""
		predefined_functions = [
								"insertaTexto", "insertaTriangulo", "insertaRectangulo", "insertaLinea",
								"insertaCirculo", "insertaOvalo", "insertaPunto", "insertaCurva",
								]
		graphics = None
		arg_dirs = []
		actual_quad = 0
		return_quad = 0
		called_predefined_fun = False
		found_return = False
		actual_fun = ""
		fun_calls = Queue()
		execution_stack = Stack()

		while actual_quad < len(quadruples):
			if quadruples[actual_quad][0] == '=':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				st.set_val_from_dir(dir_der, val_izq)

			elif quadruples[actual_quad][0] == '+':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq + val_der
				st.set_val_from_dir(dir_res, result)

			elif quadruples[actual_quad][0] == '-':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq - val_der
				st.set_val_from_dir(dir_res, result)

			elif quadruples[actual_quad][0] == '*':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				result  =  val_izq * val_der
				st.set_val_from_dir(dir_res, result)

			elif quadruples[actual_quad][0] == '/':
				dir_izq = quadruples[actual_quad][1]
				dir_der = quadruples[actual_quad][2]
				dir_res = quadruples[actual_quad][3]
				val_izq = st.get_val_from_dir(dir_izq)
				val_der = st.get_val_from_dir(dir_der)
				if val_der == 0 or val_der == 0.0:
					raise ZeroDivisionException('Division entre 0.')
				result  =  val_izq / val_der
				st.set_val_from_dir(dir_res, result)

			elif quadruples[actual_quad][0] == "escritura":
				val = st.get_val_from_dir(quadruples[actual_quad][3])
				print(val)

			elif quadruples[actual_quad][0] == "entrada":
				val = raw_input("Introduza un valor: ")
				var_dir = quadruples[actual_quad][3]
				st.set_val_from_dir(var_dir, val)

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

			elif quadruples[actual_quad][0] == "GotoF":
				result = st.get_val_from_dir(quadruples[actual_quad][1])
				if result == "falso":
					step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
					actual_quad += step

			elif quadruples[actual_quad][0] == "Goto":

				step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
				actual_quad += step

			elif quadruples[actual_quad][0] == "ERA":
				if not execution_stack.isEmpty():
					var_table   = copy.deepcopy(st.get_func_dic().get(fun_calls.dequeue())[1])
					
					
					"""	
					print("ERA")		
					if not execution_stack.peek()[0] == None:
						print("Anteriormente")
						for var_id, lst in execution_stack.peek()[0].iteritems():
							print("direccion virtual:", lst[4])
							print("valor:", lst[3])
					"""
					for var_id, lst in var_table.iteritems():
						lst[3] = copy.deepcopy(st.get_val_from_dir(lst[4]))
						#print("direccion virtual:", lst[4])
						#print("valor:", lst[3])
					saved_fun   = [var_table, None]

					execution_stack.push(list(saved_fun))



				# eliminamos lista con direcciones de argumentos
				del arg_dirs[:]
				
				scope = quadruples[actual_quad][1]
				var_table = st.get_func_dic().get(scope)[1]
				fun_calls.enqueue(scope)
				no_vars = st.get_var_count(scope)

				for var_id, var_lst in var_table.iteritems():
					arg_dirs.append(var_lst[4])
				
				"""
				for p_dir in arg_dirs:
					print(p_dir)
				
				print("diccionario con variables:")
				for k, v in var_table.iteritems():
					print("var", k)
					for e in v:
						print(e)
				"""
				
			elif quadruples[actual_quad][0] == "PARAMETER":
				val = st.get_val_from_dir(quadruples[actual_quad][1])
				param_position = quadruples[actual_quad][3][5:]
				st.set_val_from_dir(arg_dirs[int(param_position)], val)

			elif quadruples[actual_quad][0] == "GOSUB":
				fun_name = quadruples[actual_quad][1]
				if fun_name in predefined_functions:
					called_predefined_fun = True
					if graphics is None:
					 	graphics = Graphics()
					argument_lst = []
					for arg_dir in arg_dirs:
						arg = st.get_val_from_dir(arg_dir)
						argument_lst.append(arg)
					graphics.build_figure(fun_name, argument_lst)
				else:
					return_quad  = actual_quad + 1
					actual_quad  = st.get_quadruple_count(fun_name) - 1
					if execution_stack.isEmpty():
						saved_fun = [None, return_quad]
					else:
						saved_fun    = execution_stack.pop()
						saved_fun[1] = return_quad
					execution_stack.push(list(saved_fun))

			elif quadruples[actual_quad][0] == "ENDPROC":
				if not found_return:
					saved_fun   = execution_stack.pop()
					actual_quad = saved_fun[1] - 1
					if not execution_stack.isEmpty():
						for var_id, lst in saved_fun[0].iteritems():
							#print("direccion virtual:", lst[4])
							#print("valor:", lst[3])
							st.set_val_from_dir(lst[4], lst[3])
					else:
						fun_calls.dequeue()
				else:
					found_return = False

			elif quadruples[actual_quad][0] == "RETURN":
				fun_dir = st.get_func_dic().get("global")[1].get(fun_calls.peek())[4]
				var_dir = quadruples[actual_quad][1]
				val     = st.get_val_from_dir(var_dir)
				st.set_val_from_dir(fun_dir, val)

				saved_fun   = execution_stack.pop()
				actual_quad = saved_fun[1] - 1
				if not execution_stack.isEmpty():
					for var_id, lst in saved_fun[0].iteritems():
						st.set_val_from_dir(lst[4], lst[3])
				else:
					fun_calls.dequeue()
				found_return = True

			elif quadruples[actual_quad][0] == "VER":
				index = quadruples[actual_quad][1]
				l_limit = quadruples[actual_quad][2]
				u_limit = quadruples[actual_quad][3]
				index = st.get_val_from_dir(index)
				if index < l_limit or index > u_limit:
					raise IndexError("Se intento acceder a un espacio fuera del arreglo.")

			actual_quad += 1

		if called_predefined_fun:
			graphics.display_graphics();















