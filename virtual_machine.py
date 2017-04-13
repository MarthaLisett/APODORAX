class virtual_machine:
	def __init__(self):
		pass

	def start_execution(self, st, quadruples):
		"""
		print("buscando:", dir_izq)
		print("buscando:", dir_der)
		print("buscando:", dir_res)
		"""
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
				scope = quadruples[actual_quad][1]
				var_table = st.get_func_dic().get(scope)[1]
				
				for var_id, var_lst in var_table.iteritems():
					arg_dirs.append(var_lst[4])

				"""
				for p_dir in arg_dirs:
					print(p_dir)

				print("diccioanrio con variables:")
				for k, v in var_table.iteritems():
					print("var", k)
					for e in v:
						print(e)
				"""

			elif quadruples[actual_quad][0] == "PARAMETER":
				val_dir = st.get_val_from_dir(quadruples[actual_quad][1])
				param_position = quadruples[actual_quad][3][5:]
				st.set_val_from_dir(arg_dirs[int(param_position)], val_dir)

			elif quadruples[actual_quad][0] == "GOSUB":
				return_quad = actual_quad + 1
				actual_quad = st.get_quadruple_count(quadruples[actual_quad][1]) - 1
				print("ire al cuadruplo:", actual_quad + 1)

			elif quadruples[actual_quad][0] == "ENDPROC":
				actual_quad = return_quad
				arg_dirs = []

			actual_quad += 1

















