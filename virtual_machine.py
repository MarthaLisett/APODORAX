class virtual_machine:
	def __init__(self):
		pass

	def start_execution(self, st, quadruples):
		"""
		print("buscando:", dir_izq)
		print("buscando:", dir_der)
		print("buscando:", dir_res)
		"""
		actual_quad = 0
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
				print("estoy evaluando:", result)
				if result == "falso":
					step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
					actual_quad += step

			elif quadruples[actual_quad][0] == "Goto":

				step = int(str(quadruples[actual_quad][3])) - actual_quad - 1
				actual_quad += step
				print("quiero ir a: ", actual_quad+1)


			actual_quad += 1

















