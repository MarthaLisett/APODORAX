#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
#  Jose Gonzalez Ayerdi - A01036121
#  Martha Benavides - A01280115
#  Proyecto Final, Diseño de Compiladores
#  Sintaxis para el lenguaje APODORAX
#  Gramatica regular para el analisis sintactico con PLY
# ------------------------------------------------------------
from symbol_table  import symbol_table
from stack         import Stack
from semantic_cube import semantic_cube
from queue         import Queue
from memory        import Memory
from temporal      import Temporal
from globs         import Globs
from local         import Local
from constant      import Constant
from virtual_machine import virtual_machine
import ply.yacc as yacc
import sys
import collections
# obtenemos la lista de tokens generadas por el analizador lexico
from scanner_apodorax import tokens

# Reglas Gramaticales

precedence = (
    ('nonassoc', 'MENORQUE', 'MAYORQUE', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

operators_s   = Stack()
operands_s    = Stack()
types_s       = Stack()
quad_lst      = []
jumps_s       = Stack()
counter       = 0
error_list    = []
st            = symbol_table()
sc            = semantic_cube()
relops        = ["&&", "||", ">", "<", ">=", "<=", "!=", "=="]
args_count    = 0
tmp_var_num   = 1
fun_var_count = 0
k             = 0
type_pointer  = None
fun_calling   = None
current_id    = None
current_type  = None
current_vec_id = None
current_dim_var_id = None
vm            = virtual_machine() 
main_quad     = 0
dim_vars_s    = Stack()
debug         = False
# Programa
def p_program(p):
  '''program : PROGRAMA ID inicializar DOSPUNTOS declaracion insertVarCount createMainQuad function INICIO fillMainQuad insertMainFun bloque FIN generarCuadruplos '''

def p_crateMainQuad(p):
  '''createMainQuad : '''
  global quad_lst
  global counter
  quad = ["Goto", "", "", ""]
  quad_lst.append(quad)
  counter += 1

def p_fillMainQuad(p):
  '''fillMainQuad : '''
  global quad_lst
  quad_lst[0][3] = counter

def p_insertMainFun(p):
  '''insertMainFun : '''
  global st
  st.insert_function("inicio", "vacio")
  st.set_scope("inicio")

def p_generarCuadruplos(p):
  '''generarCuadruplos : '''
  global quad_lst
  archivo = open('cuadruplos.bigsheep', 'w')
  dic = { key : value  for key, value in enumerate(quad_lst)}
  od = collections.OrderedDict(sorted(dic.items()))
  with open('cuadruplos.bigsheep', 'w') as f:
    for key, value in dic.items():
        f.write('%s:%s\n' % (key, value))
  global vm
  vm.start_execution(st, quad_lst)


def p_inicializar(p):
  '''inicializar : '''
  
  global st
  st.insert_function("insertaTexto", "vacio")
  st.set_scope("insertaTexto")
  st.insert_variable("flotante", "x")
  st.insert_variable("flotante", "y")
  st.insert_variable("cadena", "color")
  st.insert_variable("cadena", "texto")
  st.insert_variable("entero", "tamanio")
  st.add_no_params(5)
  st.add_var_count(5)
  st.add_function_as_var("insertaTexto", "vacio")

  st.insert_function("insertaTriangulo", "vacio")
  st.set_scope("insertaTriangulo")
  st.insert_variable("flotante", "x1")
  st.insert_variable("flotante", "x2")
  st.insert_variable("flotante", "y1")
  st.insert_variable("flotante", "y2")
  st.insert_variable("flotante", "z1")
  st.insert_variable("flotante", "z2")
  st.insert_variable("cadena", "relleno")
  st.insert_variable("cadena", "linea")
  st.insert_variable("entero", "grosor")
  st.add_no_params(9)
  st.add_var_count(9)
  st.add_function_as_var("insertaTriangulo", "vacio")

  st.insert_function("insertaRectangulo", "vacio")
  st.set_scope("insertaRectangulo")
  st.insert_variable("flotante", "x")
  st.insert_variable("flotante", "y")
  st.insert_variable("flotante", "z")
  st.insert_variable("flotante", "w")
  st.insert_variable("cadena", "relleno")
  st.insert_variable("cadena", "linea")
  st.insert_variable("entero", "grosor")
  st.add_no_params(7)
  st.add_var_count(7)
  st.add_function_as_var("insertaRectangulo", "vacio")

  st.insert_function("insertaCirculo", "vacio")
  st.set_scope("insertaCirculo")
  st.insert_variable("flotante", "x")
  st.insert_variable("flotante", "y")
  st.insert_variable("flotante", "radio")
  st.insert_variable("cadena", "relleno")
  st.insert_variable("cadena", "linea")
  st.insert_variable("entero", "grosor")
  st.add_no_params(6)
  st.add_var_count(6)
  st.add_function_as_var("insertaCirculo", "vacio")

  st.insert_function("insertaOvalo", "vacio")
  st.set_scope("insertaOvalo")
  st.insert_variable("flotante", "x1")
  st.insert_variable("flotante", "y1")
  st.insert_variable("flotante", "x2")
  st.insert_variable("flotante", "y2")
  st.insert_variable("cadena", "relleno")
  st.insert_variable("cadena", "linea")
  st.insert_variable("entero", "grosor")
  st.add_no_params(7)
  st.add_var_count(7)
  st.add_function_as_var("insertaOvalo", "vacio")

  st.insert_function("insertaPunto", "vacio")
  st.set_scope("insertaPunto")
  st.insert_variable("flotante", "x")
  st.insert_variable("flotante", "y")
  st.insert_variable("cadena", "relleno")
  st.add_no_params(3)
  st.add_var_count(3)
  st.add_function_as_var("insertaPunto", "vacio")
  
  st.insert_function("insertaLinea", "vacio")
  st.set_scope("insertaLinea")
  st.insert_variable("flotante", "x1")
  st.insert_variable("flotante", "y1")
  st.insert_variable("flotante", "x2")
  st.insert_variable("flotante", "y2")
  st.insert_variable("cadena", "relleno")
  st.insert_variable("entero", "grosor")
  st.add_no_params(6)
  st.add_var_count(6)
  st.add_function_as_var("insertaLinea", "vacio")

  st.insert_function("insertaCurva", "vacio")
  st.set_scope("insertaCurva")
  st.insert_variable("flotante", "x1")
  st.insert_variable("flotante", "y1")
  st.insert_variable("flotante", "x2")
  st.insert_variable("flotante", "y2")
  st.insert_variable("cadena", "relleno")
  st.add_no_params(5)
  st.add_var_count(5)
  st.add_function_as_var("insertaCurva", "vacio")

  st.set_scope("global")

  p[0]="Interpretado Correctamente."

def p_guardarId(p):
  ''' guardarId : '''
  if len(p) >= 1:
    if (not operands_s.isEmpty()):
      if operators_s.isEmpty():
        while not operands_s.isEmpty():
          operands_s.pop()
          types_s.pop()
        operands_s.push(st.get_var(p[-3])[4])
        if st.get_var(p[-3]) is not None:
          types_s.push(st.get_var(p[-3])[1])
      else:
        operands_s.push(st.get_var(p[-3])[4])
    else:
      operands_s.push(st.get_var(p[-3])[4])
      types_s.push(st.get_var(p[-3])[1])

def p_buscarId(p):
  '''buscarId : '''
  if len(p) >= 1:
    global st
    global current_var_id
    st.search_variable(current_var_id)

 # Constante ID declaracion
def p_cteid_declaracion(p):
    '''cteid_declaracion : ID saveVecID revisarId vectorSettings'''
    p[0] = p[1]

def p_vectorSettings(p):
  '''vectorSettings : CORCHETEIZQ setDimFlag exp setLimits CORCHETEDER calculateK
             | '''

# Auxiliar Constante ID
def p_cteidaux(p):
    '''cteidaux : CORCHETEIZQ saveDimVarID verifyDimVar exp CORCHETEDER generateVectorQuad
               | '''

def p_saveDimVarID(p):
  '''saveDimVarID : '''
  global current_var_id
  global current_dim_var_id
  global operands_s
  current_dim_var_id = current_var_id


def p_generateVectorQuad(p):
  '''generateVectorQuad : '''
  global current_dim_var_id
  global st
  global quad_lst
  global types_s
  global tmp_var_num
  global operators_s
  global operands_s
  global counter

  l_limit = st.get_dim_var(current_dim_var_id)[1]
  u_limit = st.get_dim_var(current_dim_var_id)[2]
  k       = st.get_dim_var(current_dim_var_id)[3]

  quad = ['VER', operands_s.peek(), l_limit, u_limit]
  quad_lst.append(quad)

  temporal = 't_' + str(tmp_var_num)
  tmp_var_num += 1
  aux      = operands_s.pop()
  aux_type = types_s.peek()
  if debug : print("este es el ultimo tipo que llego:", aux_type)
  st.insert_variable(aux_type, temporal)
  tmp_dir  = st.get_var(temporal)[4]
  base_dir = st.get_dim_var(current_dim_var_id)[6]
  if debug : print("la direccion recuperada:", tmp_dir)
  quad1 = ['+', aux, str(k) + "_", tmp_dir]
  quad2 = ['+', tmp_dir, str(base_dir) + "_", tmp_dir]

  quad_lst.append(quad1)
  quad_lst.append(quad2)
  counter += 3

  operands_s.push("_" + str(tmp_dir))

  operators_s.pop()
  dim_vars_s.pop()

def p_verifyDimVar(p):
  '''verifyDimVar : '''
  global dim_vars_s
  global operators_s
  global st
  global current_dim_var_id
  if debug : print("ultima variable dimensionada:", current_dim_var_id)
  var_id  = current_dim_var_id #operands_s.pop()
  var_lst = st.get_var(var_id)
  if not var_lst[5]:
    raise TypeError("La variable " + "'" + var_id + "' no es dimensionada.")
  else:
    dim_var = (var_id, 1)
    dim_vars_s.push(dim_var)
    operators_s.push("(")

def p_saveVecID(p):
  '''saveVecID : '''
  global current_vec_id
  current_vec_id = p[-1]

def p_setDimFlag(p):
  '''setDimFlag : '''
  global st
  global current_vec_id
  st.set_dim_flag(current_vec_id)

def p_setLimits(p):
  '''setLimits : '''
  global st
  global current_var_id
  global operands_s
  st.set_vector_limits(st.get_val_from_dir(operands_s.pop()), current_vec_id)

def p_calculateK(p):
  '''calculateK : '''
  global st
  st.calculate_k(current_vec_id)


def p_buscarFuncion(p):
  ''' buscarFuncion : '''
  if len(p) >= 1:
    global st
    global current_id
    st.search_function(current_id) #tendria que cambiar a -2

# Instrucciones de las funciones
def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO declaracion insertVarCount insertQuadrupleCount bloqueaux regreso LLAVEDERECHO'''

def p_insertQuadrupleCount(p):
  '''insertQuadrupleCount : '''
  st.add_quadruple_count(counter)

def p_insertVarCount(p):
  '''insertVarCount : '''
  global fun_var_count
  st.add_var_count(fun_var_count)
  fun_var_count = 0

# Tipo de regreso de las funciones
def p_tiporegreso(p):
    '''tiporegreso : tipo
                   | VACIO'''
    p[0] = p[1]

# Parametros de las funciones
def p_functionpam(p):
    '''functionpam : VAR tipo ID agregarParam functionpam2
                 | '''

def p_incrementParamCounter(p):
  '''incrementParamCounter : '''
  global args_count
  args_count += 1

def p_addParamCount(p):
  '''addParamCount : '''
  global args_count
  if debug : print("Valor args_count:", args_count)
  st.add_no_params(args_count)
  args_count = 0

def p_agregarParam(p):
  '''agregarParam : '''
  if len(p) > 0:
    st.insert_variable(p[-2], p[-1])

# Auxiliar Parametros de las funciones
def p_functionpam2(p):
  '''functionpam2 : COMA incrementParamCounter functionpam
                    | incrementParamCounter '''

# Funcion
def p_function(p):
    '''function : FUNCION resetScope tiporegreso ID idFunctionCheck createGlobal PARENIZQUIERDO functionpam addParamCount PARENDERECHO bloquefun finishFun function
            | '''

def p_createGlobal(p):
  '''createGlobal : '''
  if len(p) > 0:
    st.add_function_as_var(p[-2], p[-3])

def p_finishFun(p):
  '''finishFun : '''
  global counter
  quad = ['ENDPROC', '', '', '']
  quad_lst.append(quad)
  counter += 1

def p_resetScope(p):
  '''resetScope : '''
  st.scope ='global'
  global tmp_var_num
  tmp_var_num = 0

def p_idFunctionCheck(p):
  ''' idFunctionCheck : '''
  if len(p) >= 1:
     global st
     st.insert_function(p[-1], p[-2])

# Valores constantes
def p_cte(p):
    '''cte : ID getCurrentID symbol
           | CENTERO
           | CFLOTANTE
           | CCADENA
           | CCARACTER
           | VERDADERO
           | FALSO'''
    
    if debug : print("Constante actual:", p[1])
    global st

    if not st.function_exists(p[1]):
      p[0] = p[1]
      const_dir = st.add_constant_to_memory(p[1], get_type(p[1]))
      if st.get_var(p[1]) is not None and get_type(p[1]) != "entero" and len(st.get_var(p[1])) >= 4:
        if not st.get_var(p[1])[5]:
          operands_s.push(st.get_var(p[1])[4]) #[0]
          types_s.push(st.get_var(p[1])[1])
      else:
        operands_s.push(const_dir)#operands_s.push(p[1])
        types_s.push(get_type(p[1]))

def p_symbol(p):
  '''symbol : cteid
          |  verifyNullAssignment llamada '''
  p[0] = p[-2]

def p_verifyNullAssignment(p):
  '''verifyNullAssignment : '''
  global st
  current_return_type = st.get_var(p[-2])[1]
  if operators_s.peek() == '=' and current_return_type == "vacio":
    raise TypeError("No se puede obtener un valor de la funcion '" + p[-2] + "'.")


# Tipo de dato
def p_tipo(p):
    '''tipo : ENTERO
            | FLOTANTE
            | CADENA
            | CARACTER
            | BOOL'''

    p[0] = p[1]
# Declaracion de variables
def p_declaracion(p):
    '''declaracion : VAR tipo getVarType cteid_declaracion PUNTOYCOMA countVar declaracion
                | '''

def p_getVarType(p):
  '''getVarType : '''
  global current_type
  current_type = p[-1]

def p_countVar(p):
  '''countVar : '''
  global fun_var_count
  fun_var_count += 1

def p_revisarId(p):
  '''revisarId : '''
  pass
  if len(p) >= 1:
    global st
    global current_vec_id
    global current_type
    if debug : print("estoy regresando p[-1]", p[-1])
    st.insert_variable(current_type, current_vec_id)

# Return de las funciones
def p_regreso(p):
    '''regreso : REGRESAR returnExp
              | nullReturn '''

def p_returnExp(p):
  '''returnExp : exp verifyReturnType PUNTOYCOMA addReturn 
              | VACIO verifyReturnType PUNTOYCOMA addReturn '''

def p_verifyReturnType(p):
    '''verifyReturnType : '''
    if len(p) > 0:
      written_type = types_s.peek() if p[-1] != "vacio" else "vacio"
      func_lst = st.get_var(st.get_scope()) 
      if written_type != func_lst[1]:
        if func_lst[1] == "vacio":
          raise TypeError("La funcion '" + func_lst[0] + "' no puede regresar un valor.")
        else:
          raise TypeError("La funcion '" + func_lst[0] + "' debe regresar " + func_lst[1] + ".")

def p_voidReturn(p):
  '''nullReturn : '''
  global st
  func_lst = st.get_var(st.get_scope()) 
  if func_lst[1] != "vacio":
    raise TypeError("La funcion '" + func_lst[0] + "' debe regresar " + func_lst[1] + ".")

def p_addReturn(p):
  '''addReturn : '''
  global counter
  global st
  return_val = operands_s.pop() if p[-3] != "vacio" else "NULL"
  quad = ['RETURN', return_val, "", ""]
  st.set_var_val(st.get_scope(), return_val)
  quad_lst.append(quad)
  counter += 1;

# Bloque
def p_bloque(p):
   '''bloque : LLAVEIZQUIERDO bloqueaux LLAVEDERECHO'''

# Auxiliar bloque permite poner 0 o mas estatutos
def p_bloqueaux(p): 
  '''bloqueaux : estatuto bloqueaux
              | '''

# Expresion que permite la comparacion
def p_expresion(p): 
    '''expresion : negacion exp expresionaux
                | color'''  

# Exp suma y resta
def p_exp(p):
    '''exp : termino checkExpTypes exp2 '''
    p[0] = p[1]

def p_saveFunID(p):
  '''saveFunID : '''
  global fun_calling
  global current_id 
  fun_calling = current_id

def p_generateGoSub(p):
  '''generateGoSub : '''
  global fun_calling
  global type_pointer
  global k
  global counter
  quad = ['GOSUB', fun_calling, '', 'dir']
  quad_lst.append(quad)
  k = 0
  type_pointer = None
  counter += 1

  var_lst = st.get_var(fun_calling)
  var_type = st.get_var_type(var_lst[0])

  if debug : print("generando sub------")
  if debug : print('type:', var_type)
  if debug : print('val:', var_lst[0])
  operands_s.push(var_lst[4]) #[0]
  types_s.push(var_type)
  
def p_verifyArgCount(p):
  '''verifyArgCount : '''
  global type_pointer
  global k
  type_pointer = None
  if k != st.get_no_params(fun_calling):
    raise AttributeError('La función recibe una cantidad distinta de argumentos.')

def p_generateERA(p):
  '''generateERA : '''
  if len(p) > 0:
    global current_id
    quad = ['ERA', current_id, '', '']
    quad_lst.append(quad)
    global k
    global type_pointer
    global counter
    if st.get_no_params(fun_calling) > 0:
      type_pointer = st.get_param_type(current_id, k)
    counter += 1


# Parametros de la llamada
def p_llamadapar(p):
    '''llamadapar : exp validateArgs llamadaparaux
                 | '''

def p_validateArgs(p):
  '''validateArgs : '''
  global counter
  global k
  global type_pointer
  argument = operands_s.pop()
  arg_type = types_s.pop()

  if debug : print("mandando: " + str(argument) + " con tipo:" +  str(arg_type))
  if debug : print("esperando:", type_pointer)

  if arg_type != type_pointer:
    raise TypeError("Los tipos en la llamada y la función no coinciden.")
  else:
    quad = ['PARAMETER', argument, '', 'arg #' + str(k)]
    quad_lst.append(quad)
    counter += 1

# Auxiliar de parametros de llamada
def p_llamadaparaux(p):
    '''llamadaparaux : COMA incrementK llamadapar
                  | incrementK'''

def p_incrementK(p):
  '''incrementK : '''
  global k
  global fun_calling
  global type_pointer
  k += 1
  if k != st.get_no_params(fun_calling):
    type_pointer = st.get_param_type(fun_calling, k)

# Lado izquierdo de la asignacion para saber si es id normal o arreglo
def p_asignacionizq(p):
  '''asignacionizq : ID saveVarID buscarId guardarId asignacionizqaux'''
  p[0] = p[1]

def p_saveVarID(p):
  '''saveVarID : '''
  global current_var_id
  current_var_id = p[-1]
  if debug : print("variable actual:", current_var_id)

# Auxiliar asignacionizq
def p_asignacionizqaux(p):
  '''asignacionizqaux : CORCHETEIZQ saveDimVarID verifyDimVar exp CORCHETEDER generateVectorQuad
                     | '''

# Asignacion de valores
def p_asignacion(p):
  '''asignacion : asignacionizq ASIGNACION insertarAsignacion exp setAssignment PUNTOYCOMA'''


def p_insertarAsignacion(p):
  '''insertarAsignacion : '''
  operators_s.push(p[-1])

def p_setAssignment(p):
  '''setAssignment : '''
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '=':
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)

        if result_type != -1:
          global counter
          global st
          result = right_op
          if debug : print("l_op:", left_op)
          if debug : print("r_op:", right_op)
          #st.set_var_val(left_op, result)

          #if debug : print("resultado final:", st.get_var(left_op))
          #t = str(type(right_op))[7:10]
          # revisar que no sea ya una direccion de memoria debido a agregar constantes
          #if t != 'int':
          #  result = st.get_var(right_op)[4]
          #else:
          result = right_op
          quad = [operator, result, "", left_op] #st.get_var(left_op)[4]]
          quad_lst.append(quad)
          counter += 1
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")


# Estatutos a estar dentro de los bloques
def p_estatuto(p):
   '''estatuto : ingreso
              | escritura
              | texto
              | rectangulo
              | circulo
              | ovalo
              | triangulo
              | punto
              | linea
              | curva
              | ID getCurrentIDStatement llamada PUNTOYCOMA
              | asignacion
              | condicion
              | ciclo'''

def p_getCurrentIDStatement(p):
  '''getCurrentIDStatement : saveVarID'''
  global current_id
  current_id = p[-1]

def p_getCurrentIDFun(p):
  '''getCurrentIDFun : '''
  global current_id
  current_id = p[-1]

def p_getCurrentID(p):
  '''getCurrentID : saveVarID'''
  global current_id
  global operands_s
  current_id = p[-1]
  #if not st.function_exists(p[-1]) and st.get_var(p[-1])[5]:
    #if debug : print("voy a introducir:" + st.get_var(p[-1])[0])
    #operands_s.push(st.get_var(p[-1])[0])

# Negar la expresion
def p_negacion(p):
    '''negacion : NO
              | '''   

# Signos de comparacion
def p_comparacion(p):
    '''comparacion : MENORQUE
                  | MAYORQUE
                  | MAYORIGUAL
                  | MENORIGUAL
                  | IGUAL
                  | DIFERENTE '''
    p[0] = p[1]

def p_logico(p):
  '''logico : expresion checarLogico logicoAux '''


def p_checarLogico(p):
  '''checarLogico : '''
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '&&' or operators_s.peek() == '||':
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          lo = False
          ro = False
          if left_op == 'verdadero':
            lo = True
          if right_op == 'verdadero':
            ro = True

          if debug : print('lo:', left_op)
          if debug : print('ro:', right_op)
          if debug : print('op:', operator)

          global counter
          global tmp_var_num
          #tipo_actual = get_type(result)
          result = 't_' + str(tmp_var_num)
          global st

          st.insert_variable(result_type, result)
          quad = [operator, left_op, right_op, st.get_var(result)[4]]
          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(st.get_var(result)[4])
          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

def p_logicoAux(p):
  '''logicoAux : CONJUNCION agregarLogico logico
                | DISYUNCION agregarLogico logico
                | '''

def p_agregarLogico(p):
  '''agregarLogico : '''
  if len(p) > 0:
    operators_s.push(p[-1])

def p_checkRelopTypes(p):
  '''checkRelopTypes : '''
  if len(p) >= 1:
    if operators_s.size() >= 0:
      if operators_s.peek() in relops:
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          '''
          if operator == '<':
            result = left_op < right_op
          elif operator == '>':
            result = left_op > right_op
          elif operator == '<=':
            result = left_op <= right_op
          elif operator == '>=':
            result = left_op >= right_op
          elif operator == '==':
            result = left_op == right_op
          elif operator == '!=':
            result = left_op != right_op
          if result:
            result = "verdadero"
          else:
            result = "falso"
          '''
          global counter
          global tmp_var_num
          result = 't_' + str(tmp_var_num)

          global st
          st.insert_variable(result_type, result)

          quad = [operator, left_op, right_op, st.get_var(result)[4]]

          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(st.get_var(result)[4])

          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

# Auxiliar de expresion
def p_expresionaux(p) :
    '''expresionaux : comparacion addRelop exp checkRelopTypes
                   | '''

def p_addRelop(p):
  '''addRelop : '''
  if len(p) >= 0:
    operators_s.push(p[-1])

def p_checkExpTypes(p):
  '''checkExpTypes : '''
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '+' or operators_s.peek() == '-':
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          #result = left_op + right_op if operator is '+' else left_op - right_op
          global counter
          global tmp_var_num
          #tipo_actual = get_type(result)
          result = 't_' + str(tmp_var_num)

          global st
          if debug : print("SCOPE ACTUAL:",st.get_scope())
          if debug : print("CONTENIDO DE TABLA")
          if debug : print(st.print_var_table(st.get_scope()))
          if debug : print("Estoy intentando agregar:", result)
          st.insert_variable(result_type, result)
          quad = [operator, left_op, right_op, st.get_var(result)[4]]
 
          quad_lst.append(quad)
          counter += 1
          tmp_var_num += 1
          operands_s.push(st.get_var(result)[4])
          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

def p_addExp(p):
  ''' addExp : '''
  if len(p) > 0:
    if operands_s.size() > 0:
      operators_s.push(p[-1])

# Auxiliar de exp que permite tener 1 o más terminos
def p_exp2(p):
    '''exp2 : SUMA addExp exp
          | RESTA addExp exp
          | '''

# Termino multiplicacion y division
def p_termino(p):
  '''termino : factor checkTermTypes termino2'''
  p[0] = p[1]

def p_checkTermTypes(p):
  '''checkTermTypes : '''
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '*' or operators_s.peek() == '/':
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          #result = left_op * right_op if operator is '*' else left_op / right_op
          global counter
          #tipo_actual = get_type(result)
          global tmp_var_num
          result = 't_' + str(tmp_var_num)

          global st
          st.insert_variable(result_type, result)
          quad = [operator, left_op, right_op, st.get_var(result)[4]]
          quad_lst.append(quad)

          if debug : print("---encontre esto---")
          if debug : print(left_op)
          if debug : print(right_op)

          tmp_var_num += 1
          counter += 1
          operands_s.push(st.get_var(result)[4])
          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

# Auxiliar termino que permite tener 1 o mas factores
def p_termino2(p):
  '''termino2 : MULTIPLICACION addFactor termino
             | DIVISION addFactor termino
             | '''

def p_addFactor(p):
  '''addFactor : '''
  if len(p) > 0:
    if operands_s.size() > 0:
      operators_s.push(p[-1])

# Factor numerico o mediante IDs
def p_factor(p):
    '''factor : PARENIZQUIERDO crearFondoFalso logico PARENDERECHO quitarFondoFalso
            | cte 
            '''

# Llamada a funcion
def p_llamada(p):
    '''llamada : buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub'''

# Constante ID
def p_cteid(p):
    '''cteid : buscarId cteidaux'''    
    p[0] = p[-1]

def p_crearFondoFalso(p):
  '''crearFondoFalso : '''
  if len(p) > 0:
    operators_s.push(p[-1])

def p_quitarFondoFalso(p):
  '''quitarFondoFalso : '''
  if len(p) > 0:
    operators_s.pop()

# Condicion que maneja si, sino, entonces
def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO logico PARENDERECHO generarCond ENTONCES bloque condicionaux'''

def p_generarCond(p):
  '''generarCond : '''
  if len(p) > 0:
    tipo_exp = types_s.pop()
    if tipo_exp != 'bool':
      raise TypeError('Tipos incompatibles.')
    else:
      result = operands_s.pop()
      global counter
      quad = ['GotoF', result, "", ""]
      quad_lst.append(quad)
      counter += 1
      jumps_s.push(counter - 1)

# Auxiliar de condicion que maneja el sino
def p_condicionaux(p):
   '''condicionaux : SINO ENTONCES generarElse bloque rellenarCond
                  | rellenarCond '''

def p_generarElse(p):
  '''generarElse : '''
  if len(p) > 0:
    quad = ['Goto', "", "", ""]
    global counter
    quad_lst.append(quad)
    counter += 1
    false = jumps_s.pop()
    jumps_s.push(counter - 1)
    # FILL(false, counter)
    quad_lst[false][3] = counter

def p_rellenarCond(p):
  '''rellenarCond : '''
  global counter
  # fill
  if debug : print("counter else:", counter)
  end = jumps_s.pop()
  quad_lst[end][3] = counter

# Colores a usar en las figuras
def p_color(p):
    '''color : NEGRO
            | GRIS
            | AZUL
            | AMARILLO
            | VERDE
            | ROJO
            | ROSA
            | NARANJA'''

# Mientras (while)
def p_ciclo(p):
    '''ciclo : MIENTRAS insertarSalto PARENIZQUIERDO logico PARENDERECHO crearCiclo bloque crearRegreso '''

def p_crearRegreso(p):
  '''crearRegreso : '''
  end = jumps_s.pop()
  ret = jumps_s.pop()
  quad = ['Goto', "", "", ret]
  global counter
  quad_lst.append(quad)
  counter += 1
  # FILL(end, counter)
  quad_lst[end][3] = counter

def p_crearCiclo(p):
  '''crearCiclo : '''
  if len(p) > 0:
    exp_type = types_s.pop()
    if (exp_type != 'bool'):
      if debug : print('tipo exp en condicion:', exp_type)
      raise TypeError('Tipos incompatibles en ciclo.')
    else:
      result = operands_s.pop()
      quad = ['GotoF', result, "", ""]
      global counter
      quad_lst.append(quad)
      counter += 1
      jumps_s.push(counter - 1)

def p_insertarSalto(p):
  '''insertarSalto : '''
  jumps_s.push(counter)

# Desplegar en consola  
def p_escritura(p):
    '''escritura : DESPLEGAR PARENIZQUIERDO expresion PARENDERECHO generarEscritura PUNTOYCOMA'''

def p_generarEscritura(p):
  '''generarEscritura : '''
  quad = ['escritura', "", "", operands_s.pop()]
  quad_lst.append(quad)
  global counter
  counter += 1

# Aceptar/ingresar info del usuario
def p_ingreso(p):
    '''ingreso : ENTRADA PARENIZQUIERDO ID saveVarID buscarId PARENDERECHO generarEntrada PUNTOYCOMA'''

def p_generarEntrada(p):
  '''generarEntrada : '''
  global st
  quad = ["entrada", "", "", st.get_var(p[-4])[4]]
  quad_lst.append(quad)
  global counter
  counter += 1

"""
# Argumentos para las funciones de figura, pueden ser cualquier constante o color
def p_args(p):
    '''args : logico args2'''

# Auxiliar argumentos
def p_args2(p):
    '''args2 : COMA args
            | '''
"""

# Funcion para incluir texto
def p_texto(p):
    '''texto : INSERTATEXTO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir un rectangulo
def p_rectangulo(p):
    '''rectangulo : INSERTARECTANGULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir un triangulo
def p_triangulo(p):
    '''triangulo :  INSERTATRIANGULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir un circulo
def p_circulo(p):
    '''circulo : INSERTACIRCULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir un ovalo
def p_ovalo(p):
    '''ovalo : INSERTAOVALO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir un punto
def p_punto(p):
    '''punto : INSERTAPUNTO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir una linea
def p_linea(p):
    '''linea : INSERTALINEA getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

# Funcion para incluir una curva
def p_curva(p):
    '''curva : INSERTACURVA getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''

def p_error(p):
  if debug : print("Error de sintaxis: '%s' en línea: %s."  % (p.value, p.lineno))

def get_type(symbol):
  if symbol == "verdadero" or symbol == "falso":
    return 'bool'
  t = str(type(symbol))[7:10]
  if t == 'int':
    return "entero"
  elif t == 'flo':
    return "flotante"
  elif t == 'str' and len(symbol) == 1:
    return "caracter"
  elif t == 'str':
    return "cadena"
  else:
    return st.get_var(symbol)[3]

parser = yacc.yacc()

if __name__ == '__main__':
  if (len(sys.argv) > 1):
    # Obtiene el archivo
    file = sys.argv[1]
    try:
      f = open(file,'r')
      data = f.read()
      f.close()
      #Se realiza la gramatica
      if (parser.parse(data, tracking=True) == 'Interpretado Correctamente'):
        print ('Interpretado Correctamente');
    except EOFError:
        if debug : print(EOFError)
  else:
    if debug : print('No existe el archivo')