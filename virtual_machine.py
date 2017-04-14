from graphics_drawer import Graphics
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

		graphics = Graphics()
		arg_dirs = []
		actual_quad = 0
		return_quad = 0
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
				del arg_dirs[:]
				scope = quadruples[actual_quad][1]
				var_table = st.get_func_dic().get(scope)[1]
				# TODO: obtener unicamente parametros por medio de la var n
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
				print("val",val)
				param_position = quadruples[actual_quad][3][5:]
				print("param_pos:",param_position)
				print("dirs:", arg_dirs)
				st.set_val_from_dir(arg_dirs[int(param_position)], val)

			elif quadruples[actual_quad][0] == "GOSUB":
				fun_name = quadruples[actual_quad][1]
				if fun_name in predefined_functions:
					argument_lst = []
					for arg_dir in arg_dirs:
						arg = st.get_val_from_dir(arg_dir)
						argument_lst.append(arg)
					graphics.build_figure(fun_name, argument_lst)
				else:
					return_quad = actual_quad + 1
					actual_quad = st.get_quadruple_count(fun_name) - 1

			elif quadruples[actual_quad][0] == "ENDPROC":
				actual_quad = return_quad - 1

			actual_quad += 1

		graphics.display_graphics();















