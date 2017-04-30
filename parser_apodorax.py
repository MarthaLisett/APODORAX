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
vm            = virtual_machine() 
main_quad     = 0
debug         = False
current_vec_id = None
current_dim_var_id = None
dims_s        = Stack()

"""regla que describe la estructura completa del programa"""
def p_program(p):
  '''program : PROGRAMA ID inicializar DOSPUNTOS declaracion insertVarCount createMainQuad function INICIO fillMainQuad insertMainFun bloque FIN generarCuadruplos '''

"""crea el cuadruplo que apunta a la posicion de la funcion principal"""
def p_crateMainQuad(p):
  '''createMainQuad : '''
  global quad_lst
  global counter
  quad = ["Goto", "", "", ""]
  quad_lst.append(quad)
  counter += 1

"""rellena el cuadruplo que apunta a la funcion principal"""
def p_fillMainQuad(p):
  '''fillMainQuad : '''
  global quad_lst
  quad_lst[0][3] = counter

"""inserta la funcion principal a la tabal de simbolos y cambia el scope al de la misma funcion"""
def p_insertMainFun(p):
  '''insertMainFun : '''
  global st
  st.insert_function("inicio", "vacio")
  st.set_scope("inicio")

"""crea el archivo de salida que contiene todos los cuadruplos generados para ser leidos por la maquina virtual"""
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
  
  """crea entradas en la tabla de simbolos para todas las funciones predefinidas.
  Inicializa sus parametros y crea las variables globales correspondientes a cada funcion"""

  global st
  # funcion para insertar texto 
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

  # funcion para insertar texto 
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

  # funcion para insertar la figura rectangulo
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

  # funcion para generar el circulo
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

  # funcion para generar el ovalo
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

  # funcion para insertar puntos
  st.insert_function("insertaPunto", "vacio")
  st.set_scope("insertaPunto")
  st.insert_variable("flotante", "x")
  st.insert_variable("flotante", "y")
  st.insert_variable("cadena", "relleno")
  st.add_no_params(3)
  st.add_var_count(3)
  st.add_function_as_var("insertaPunto", "vacio")
  
  # funcion para insertar lineas
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

  # funcion para insertar curvas
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

  # se regresa el scope a global ya que anteriormente se cambio al de cada funcion
  # para indicar a la tabla de simbolos la funcion a la que corresponde cada parametro
  st.set_scope("global")

  # mensaje de interpretacion correcta
  p[0]="Interpretado Correctamente."

def p_guardarId(p):
  ''' guardarId : '''
  """revisa que los ids vayan a ser utilizados posterioremente de lo contrario
si se han leido identificadores que no seran utilizados entonces se vacian las pilas"""
  if len(p) >= 1:
    # si habia operandos antes entonces se agregan en caso
    # de que exista alguna operacion posterior
    if (not operands_s.isEmpty()):
      # si hay operandos pendientes pero no operadores entonces vaciamos
      if operators_s.isEmpty():
        while not operands_s.isEmpty():
          operands_s.pop()
        while not types_s.isEmpty():
           types_s.pop()
        operands_s.push(st.get_var(p[-3])[4])
        # agregamos el tipo en caso de que exista
        if st.get_var(p[-3]) is not None:
          types_s.push(st.get_var(p[-3])[1])
      else:
        operands_s.push(st.get_var(p[-3])[4])
    else:
      operands_s.push(st.get_var(p[-3])[4])
      types_s.push(st.get_var(p[-3])[1])

def p_buscarId(p):
  '''buscarId : '''
  """Verifica que una variable exista"""
  if len(p) >= 1:
    global st
    global current_var_id
    st.search_variable(current_var_id)


def p_cteid_declaracion(p):
    '''cteid_declaracion : ID saveVecID revisarId vectorSettings'''
    """Regla para la declaracion de arreglos"""
    p[0] = p[1]

def p_vectorSettings(p):
  '''vectorSettings : CORCHETEIZQ setDimFlag exp setLimits CORCHETEDER calculateK
             | '''
  """Regla que se encarga de asignar memoria para un arreglo recien declarado"""

def p_cteidaux(p):
    '''cteidaux : CORCHETEIZQ saveDimVarIDcte verifyDimVar exp CORCHETEDER generateVectorQuad
               | '''
    """Regla para acceder a los campos de un arreglo cuando se solicita"""

def p_saveDimVarIDcte(p):
  ''' saveDimVarIDcte : '''
  """Regla para salvar el id de un arreglo y evitar meterlo en la pila"""
  global current_var_id
  global current_dim_var_id
  global dims_s
  # salvamos la variable y la metemos en la pila de dimensiones
  current_dim_var_id = current_var_id
  dims_s.push(current_dim_var_id)

def p_saveDimVarID(p):
  '''saveDimVarID : '''
  """Guarda el id del arreglo, lo agrega a la pila de dimensiones
  y elimina el id de la pila de operadores"""
  global current_var_id
  global current_dim_var_id
  global operands_s
  global dims_s
  current_dim_var_id = current_var_id
  dims_s.push(current_dim_var_id)
  # como esta regla es usada por multiples reglas se verifica el estado de la pila
  if not operands_s.isEmpty() : operands_s.pop()

def p_generateVectorQuad(p):
  '''generateVectorQuad : '''
  """Genera el cuadruplo de acceso a los elementos de un arreglo
  """
  global current_dim_var_id
  global st
  global quad_lst
  global types_s
  global tmp_var_num
  global operators_s
  global operands_s
  global counter
  global dims_s

  # Obtiene los limites del arreglo y calcula la constante K
  current_dim_var_id = dims_s.pop()
  l_limit = st.get_dim_var(current_dim_var_id)[1]
  u_limit = st.get_dim_var(current_dim_var_id)[2]
  k       = st.get_dim_var(current_dim_var_id)[3]

  # Genera el cuadruplo de validacion de limites para el acceso al arreglo
  quad = ['VER', operands_s.peek(), l_limit, u_limit]
  quad_lst.append(quad)

  # se incrementa el contador de variables temporales
  temporal = 't_' + str(tmp_var_num)
  tmp_var_num += 1

  # obtiene los valores de la direccion base y
  # genera los cuadruplos para realizar la suma de S
  # a la constante K y a la direccion base
  aux      = operands_s.pop()
  aux_type = types_s.pop()
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
  # metemos en la pila de operandos el apuntador a la direccion
  # del valor que se obtuvo al acceder al arreglo
  operands_s.push("_" + str(tmp_dir))
  # eliminamos el fondo falso
  operators_s.pop()

def p_verifyDimVar(p):
  '''verifyDimVar : '''
  """Valida que la variable a la que se esta tratando de acceder 
  sea en efecto una variable dimensionada"""
  global operators_s
  global st
  global current_dim_var_id
  if debug : print("ultima variable dimensionada:", current_dim_var_id)
  var_id  = current_dim_var_id
  var_lst = st.get_var(var_id)
  if not var_lst[5]:
    raise TypeError("La variable " + "'" + var_id + "' no es dimensionada.")
  else:
    operators_s.push("(")

def p_saveVecID(p):
  '''saveVecID : '''
  """Salva el id de una variable dimensionada en una variable global
  de tal manera que no se tenga que guardar en la pila"""
  global current_vec_id
  current_vec_id = p[-1]

def p_setDimFlag(p):
  '''setDimFlag : '''
  """Accede al espacio en la tabla de simbolo correspondiente a una
  variable diensionada y prende una bandera que indica que es dimensionada"""
  global st
  global current_vec_id
  st.set_dim_flag(current_vec_id)

def p_setLimits(p):
  '''setLimits : '''
  """Se establecen los limites del arreglo y se valida que
  se trate de un valor valido"""
  global st
  global current_var_id
  global operands_s
  global types_s
  types_s.pop()
  if not type(operands_s.peek()) is int:
    raise TypeError("El indice del arreglo debe ser entero")
  st.set_vector_limits(st.get_val_from_dir(operands_s.pop()), current_vec_id)

def p_calculateK(p):
  '''calculateK : '''
  """Se genera el valor de la constante K para un arreglo"""
  global st
  st.calculate_k(current_vec_id)

def p_buscarFuncion(p):
  ''' buscarFuncion : '''
  """Se verifica en la tabla de simbolos que la funcion que se este llamando exista"""
  if len(p) >= 1:
    global st
    global current_id
    st.search_function(current_id)

# Instrucciones de las funciones
def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO declaracion insertVarCount insertQuadrupleCount bloqueaux regreso LLAVEDERECHO'''
  """Regla que describe el cuerpo de una funcion"""

def p_insertQuadrupleCount(p):
  '''insertQuadrupleCount : '''
  """Inserta el valor del contador actual en la tabla de simbolos para ser usado
  por la maquina virtual posteriormente"""
  st.add_quadruple_count(counter)

def p_insertVarCount(p):
  '''insertVarCount : '''
  """Se inserta en la tabla de simbolos la cantidad de variables locales
  que le pertenecen a una funcion en caso de ser utilizada por la maquina virtual"""
  global fun_var_count
  st.add_var_count(fun_var_count)
  fun_var_count = 0

def p_tiporegreso(p):
    '''tiporegreso : tipo
                   | VACIO'''
    """Regla que determina el tipo de retorno de una funcion"""
    p[0] = p[1]

def p_functionpam(p):
    '''functionpam : VAR tipo ID agregarParam functionpam2
                 | '''
    """Regla que describe la estructura de los parametros de una funcion"""

def p_incrementParamCounter(p):
  '''incrementParamCounter : '''
  """Regla que controla la cantidad de parametros que debe recibir
  una funcion"""
  global args_count
  args_count += 1

def p_addParamCount(p):
  '''addParamCount : '''
  """Agrega a la funcion presente la cantidad de parametros que debe utilizar"""
  global args_count
  if debug : print("Valor args_count:", args_count)
  st.add_no_params(args_count)
  args_count = 0

def p_agregarParam(p):
  '''agregarParam : '''
  """Regla que inserta el valor de un parametro en la tabla de variables
  de la funcion a la que pertenece"""
  if len(p) > 0:
    st.insert_variable(p[-2], p[-1])

def p_functionpam2(p):
  '''functionpam2 : COMA incrementParamCounter functionpam
                    | incrementParamCounter '''
  """Regla que le permite a la funcion recibir multiples argumentos."""

# Funcion
def p_function(p):
    '''function : FUNCION resetScope tiporegreso ID idFunctionCheck createGlobal PARENIZQUIERDO functionpam addParamCount PARENDERECHO bloquefun finishFun function
            | '''
    """Regla que describe la estructura completa de una funcion"""

def p_createGlobal(p):
  '''createGlobal : '''
  """Agrega a la tabla de simbolos la variable global que representa a la actual funcion
  que se esta insertando"""
  if len(p) > 0:
    st.add_function_as_var(p[-2], p[-3])

def p_finishFun(p):
  '''finishFun : '''
  """Regla que genera el cuadruplo de finalizacion de una funcion"""
  global counter
  quad = ['ENDPROC', '', '', '']
  quad_lst.append(quad)
  counter += 1

def p_resetScope(p):
  '''resetScope : '''
  """Regla que regresa el scope a su estado global"""
  st.scope ='global'
  global tmp_var_num
  tmp_var_num = 0

def p_idFunctionCheck(p):
  ''' idFunctionCheck : '''
  """Verifica que una funcion no este repetida y la agrega a la tabla de simbolos"""
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
  
    """Regla que obtiene el tipo de dato de una constate o id 
    y regresa su tipo, y dependiento de sus propiedades lo agrega a las pilas
    """

    if debug : print("Constante actual:", p[1])
    global st

    if not st.function_exists(p[1]):
      p[0] = p[1]
      # Agrega una constante a la memoria y obtiene su direccion
      const_dir = st.add_constant_to_memory(p[1], get_type(p[1]))
      # verificamos que el valor que se lee no sea entero
      if st.get_var(p[1]) is not None and get_type(p[1]) != "entero" and len(st.get_var(p[1])) >= 4:
        # si se trata de una variable dimensionada entonces no se agrega
        if not st.get_var(p[1])[5]:
          operands_s.push(st.get_var(p[1])[4])
        types_s.push(st.get_var(p[1])[1])
      else:
        operands_s.push(const_dir)
        types_s.push(get_type(p[1]))
        if debug : print("El tipo de la variable es:", get_type(p[1]))

def p_symbol(p):
  '''symbol : cteid
          |  verifyNullAssignment llamada '''
  """Regla auxiliar que a partir de un id toma el camino de convertirse
  en un arreglo o en la llamada a una funcion"""
  p[0] = p[-2]

def p_verifyNullAssignment(p):
  '''verifyNullAssignment : '''
  """Se verifica que cuando se haga asignacion a una variable
  la variable o funcion que se quiera asignar no este o regrese vacio"""
  global st
  current_return_type = st.get_var(p[-2])[1]
  if operators_s.peek() == '=' and current_return_type == "vacio":
    raise TypeError("No se puede obtener un valor de la funcion '" + p[-2] + "'.")

def p_tipo(p):
    '''tipo : ENTERO
            | FLOTANTE
            | CADENA
            | CARACTER
            | BOOL'''

    """Regla que define los tipos de dato del lenguaje"""
    p[0] = p[1]

def p_declaracion(p):
    '''declaracion : VAR tipo getVarType cteid_declaracion PUNTOYCOMA countVar declaracion
                | '''
    """Regla que describe la estructura de la declaracion de una variable"""

def p_getVarType(p):
  '''getVarType : '''
  """Regla que guarda el tipo del valor que se leyo mas recientemente"""
  global current_type
  current_type = p[-1]

def p_countVar(p):
  '''countVar : '''
  """Variable que cuenta la cantidad de variables declaradas dentro de una funcion"""
  global fun_var_count
  fun_var_count += 1

def p_revisarId(p):
  '''revisarId : '''
  """Regla que verifica repeticion e inserta una variable dimensionada a la tabla de simbolos"""
  pass
  if len(p) >= 1:
    global st
    global current_vec_id
    global current_type
    if debug : print("estoy regresando p[-1]", p[-1])
    st.insert_variable(current_type, current_vec_id)

def p_regreso(p):
    '''regreso : REGRESAR returnExp
              | nullReturn '''
    """Regla que define la estructura de regreso de una funcion"""

def p_returnExp(p):
  '''returnExp : exp verifyReturnType PUNTOYCOMA addReturn 
              | VACIO verifyReturnType PUNTOYCOMA addReturn '''
  """Regla que define el tipo de retorno que puede producir una funcion"""

def p_verifyReturnType(p):
    '''verifyReturnType : '''
    """Regla que valida el tipo de retorno de una funcion"""
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
  """Regla que valida que se regrese el tipo de dato correcto de 
  parte de una funcion"""
  global st
  func_lst = st.get_var(st.get_scope()) 
  if func_lst[1] != "vacio":
    raise TypeError("La funcion '" + func_lst[0] + "' debe regresar " + func_lst[1] + ".")

def p_addReturn(p):
  '''addReturn : '''
  """Se genera el cuadruplo de estatuto de retorno para una funcion"""
  global counter
  global st
  return_val = operands_s.pop() if p[-3] != "vacio" else "NULL"
  quad = ['RETURN', return_val, "", ""]
  st.set_var_val(st.get_scope(), return_val)
  quad_lst.append(quad)
  counter += 1

# Bloque
def p_bloque(p):
   '''bloque : LLAVEIZQUIERDO bloqueaux LLAVEDERECHO'''
   """Regla que describe la estructura del bloque del programa"""

# Auxiliar bloque permite poner 0 o mas estatutos
def p_bloqueaux(p): 
  '''bloqueaux : estatuto bloqueaux
              | '''
  """Regña que permite la existencia de estatutos en el programa"""


def p_expresion(p): 
    '''expresion : negacion exp expresionaux
                | color'''  
    """Regla que permite la comparacion entre expresiones"""

def p_exp(p):
    '''exp : termino checkExpTypes exp2 '''
    """Expresion para suma y resta"""
    p[0] = p[1]

def p_saveFunID(p):
  '''saveFunID : '''
  """Se guarda el nombre de la ultima funcion que se leyo para no depenter
  de los indices de la p"""
  global fun_calling
  global current_id 
  fun_calling = current_id

def p_generateGoSub(p):
  '''generateGoSub : '''
  """Regla que genera el cuadruplo goSub para mover el apuntador
  de ejecucion hacia donde se encuentra la memoria que le corresponde
  a la funcion que ha sido llamada"""
  global fun_calling
  global type_pointer
  global k
  global counter
  # generamos el cuadruplo
  quad = ['GOSUB', fun_calling, '', 'dir']
  quad_lst.append(quad)
  k = 0
  type_pointer = None
  counter += 1

  # obtenemos el tipo de retorno de la funcion
  var_lst = st.get_var(fun_calling)
  var_type = st.get_var_type(var_lst[0])

  # metemos el valor y el tipo de la funcion a las pilas
  if debug : print("generando sub------")
  if debug : print('type:', var_type)
  if debug : print('val:', var_lst[0])
  operands_s.push(var_lst[4]) #[0]
  types_s.push(var_type)
  
def p_verifyArgCount(p):
  '''verifyArgCount : '''
  """Regla que valida la cantidad de argumentos que son enviados a una funcion 
  cuando se llama"""
  global type_pointer
  global k
  type_pointer = None
  if k != st.get_no_params(fun_calling):
    raise AttributeError('La función recibe una cantidad distinta de argumentos.')

def p_generateERA(p):
  '''generateERA : '''
  """Regla que genera el cuadruplo ERA para guardar la memoria actual del programa
  y utilizar la pila de ejecucion"""
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

def p_llamadapar(p):
    '''llamadapar : exp validateArgs llamadaparaux
                 | '''
    """Regla que describe la estructura de los argumentos que seran
    enviados en una llamada a funcion"""

def p_validateArgs(p):
  '''validateArgs : '''
  """Se valida que los argumentos mandados en la llamada a una funcion
  correspondan en cuanto a tipo a los parametros que espera esta funcion
  y genera el cuadruplo correspondiente"""
  global counter
  global k
  global type_pointer
  argument = operands_s.pop()
  arg_type = types_s.pop()
  # mensajes para el proceso de depuracion
  if debug : print("mandando: " + str(argument) + " con tipo:" +  str(arg_type))
  if debug : print("esperando:", type_pointer)
  # se valida el tipo de argumentos con el tipo de parametros
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
    """Regla que permite mandar multiples argumentos en una llamada a funcion"""

def p_incrementK(p):
  '''incrementK : '''
  """Regla que incrementa el apuntador hacia los argumentos de una funcion
  vara ir validando a la par los argumento con los parametros"""
  global k
  global fun_calling
  global type_pointer
  k += 1
  if k != st.get_no_params(fun_calling):
    type_pointer = st.get_param_type(fun_calling, k)

def p_asignacionizq(p):
  '''asignacionizq : ID saveVarID buscarId guardarId asignacionizqaux'''
  """ Lado izquierdo de la asignacion para saber si es id normal o arreglo"""
  p[0] = p[1]

def p_saveVarID(p):
  '''saveVarID : '''
  """Regla auxiliar que salva el ultimo identificador encontrado para
  no depender de la p"""
  global current_var_id
  current_var_id = p[-1]
  if debug : print("variable actual:", current_var_id)

# Auxiliar asignacionizq
def p_asignacionizqaux(p):
  '''asignacionizqaux : CORCHETEIZQ saveDimVarID verifyDimVar exp CORCHETEDER generateVectorQuad
                     | '''
  """Regla que describe la estructura de la asgnacion a un valor de un arreglo"""

# Asignacion de valores
def p_asignacion(p):
  '''asignacion : asignacionizq ASIGNACION insertarAsignacion exp setAssignment PUNTOYCOMA'''
  """Regla que describe la estructura de asignacion para cualquier variable"""

def p_insertarAsignacion(p):
  '''insertarAsignacion : '''
  global operators_s
  """Inserta el operador de asignacion en la pila"""
  operators_s.push(p[-1])

def p_setAssignment(p):
  '''setAssignment : '''
  """Se genera el cuadruplo de asignacion para insertar un valor en una variable"""
  global operands_s
  global types_s
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '=':
        # se obtienen los valores de las pilas y se verifican los tipos
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        # se genera el cuadruplo
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

   """Regla que describe los posibles estatutos que pueden existir en el lenguaje"""

def p_getCurrentIDStatement(p):
  '''getCurrentIDStatement : saveVarID'''
  """Se guarda el id leido anteriormente para no depender de la p"""
  global current_id
  current_id = p[-1]

def p_getCurrentIDFun(p):
  '''getCurrentIDFun : '''
  """Se guarda el id de la funcion leida anteriormente para no depender de la p"""
  global current_id
  current_id = p[-1]

def p_getCurrentID(p):
  '''getCurrentID : saveVarID'''
  """Se guarda el id leido anteriormente para no depender de la p"""
  global current_id
  global operands_s
  current_id = p[-1]
  #if not st.function_exists(p[-1]) and st.get_var(p[-1])[5]:
    #if debug : print("voy a introducir:" + st.get_var(p[-1])[0])
    #operands_s.push(st.get_var(p[-1])[0])

def p_negacion(p):
    '''negacion : NO
              | '''   
    """Negar la expresion"""


def p_comparacion(p):
    '''comparacion : MENORQUE
                  | MAYORQUE
                  | MAYORIGUAL
                  | MENORIGUAL
                  | IGUAL
                  | DIFERENTE '''
    """Signos de comparacion"""
    p[0] = p[1]

def p_logico(p):
  '''logico : expresion checarLogico logicoAux '''
  """Regla para la comparacion logica"""

def p_checarLogico(p):
  '''checarLogico : '''
  """Regla que genera el cuadruplo correspondiente a las opreaciones logicas
  and y or"""
  if len(p) >= 1:
    if operators_s.size() > 0:
      # se verifica que tengamos pendiente una opreacion logica
      if operators_s.peek() == '&&' or operators_s.peek() == '||':
        # obtenemos todos los valores de las polas y validamos tipos
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        # asignamos valores de tipo cadena a los reusltados
        if result_type != -1:
          lo = False
          ro = False
          if left_op == 'verdadero':
            lo = True
          if right_op == 'verdadero':
            ro = True

          # codigo de depuracion
          if debug : print('lo:', left_op)
          if debug : print('ro:', right_op)
          if debug : print('op:', operator)

          # generamos temporal
          global counter
          global tmp_var_num
          #tipo_actual = get_type(result)
          result = 't_' + str(tmp_var_num)
          global st

          # insertamos resultado temporal en la tabla de simbolos
          # generamos cuadruplo e insertamos en la pila
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
  """Estructura de las opreaciones logicas"""

def p_agregarLogico(p):
  '''agregarLogico : '''
  """Agregamos un operador logico a la pila"""
  if len(p) > 0:
    operators_s.push(p[-1])

def p_checkRelopTypes(p):
  '''checkRelopTypes : '''
  """Regla para generar los cuadruplos de las operaciones relacionales"""
  if len(p) >= 1:
    if operators_s.size() >= 0:
      # verificamos que el operador sea uno relacional
      if operators_s.peek() in relops:
        # obtenemos todos los valores de las pilas y verificamos tipo
        right_op    = operands_s.pop()
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          global counter
          global tmp_var_num
          # generamos temporal
          result = 't_' + str(tmp_var_num)

          global st
          # insertamos temporal en la tabla de simbolos
          st.insert_variable(result_type, result)
          # generamos el nuevo cuadruplo
          quad = [operator, left_op, right_op, st.get_var(result)[4]]
          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(st.get_var(result)[4])

          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

def p_expresionaux(p) :
    '''expresionaux : comparacion addRelop exp checkRelopTypes
                   | '''
    """Auxiliar de expresion para tener muchas expresiones relacionales seguidas"""

def p_addRelop(p):
  '''addRelop : '''
  """Agregamos los operadores relacionales a la pila"""
  if len(p) >= 0:
    operators_s.push(p[-1])

def p_checkExpTypes(p):
  '''checkExpTypes : '''
  """Regla que genera los cuadruplos correspondientes a las expresiones
  de suma y resta"""
  if len(p) >= 1:
    if operators_s.size() > 0:
      # verificamos los operadores pendientes
      if operators_s.peek() == '+' or operators_s.peek() == '-':
        # obtenemos todos los valores de la pila y validamos tipos
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
          # generamos temporal
          #tipo_actual = get_type(result)
          result = 't_' + str(tmp_var_num)

          global st
          # codigo para depurar
          if debug : print("SCOPE ACTUAL:",st.get_scope())
          if debug : print("CONTENIDO DE TABLA")
          if debug : print(st.print_var_table(st.get_scope()))
          if debug : print("Estoy intentando agregar:", result)

          # insertamos resulado en tabla y generamos cuadruplo
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
  """Agregamos un operador a la pila"""
  if len(p) > 0:
    if operands_s.size() > 0:
      operators_s.push(p[-1])

def p_exp2(p):
    '''exp2 : SUMA addExp exp
          | RESTA addExp exp
          | '''
    """Auxiliar de exp que permite tener 1 o más terminos"""

def p_termino(p):
  '''termino : factor checkTermTypes termino2'''
  """Termino multiplicacion y division"""
  p[0] = p[1]

def p_checkTermTypes(p):
  '''checkTermTypes : '''
  """Regla que genera los cuadruplos correspondientes a las
  operaciones de multiplicacione y division"""
  if len(p) >= 1:
    if operators_s.size() > 0:
      # verificamos los operadores pendientes
      if operators_s.peek() == '*' or operators_s.peek() == '/':
        # obtenemos todos los valores de las pilas y validamos tipos
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

          # insertamos resultado en tabla y generamos cuadruplo
          global st
          st.insert_variable(result_type, result)
          quad = [operator, left_op, right_op, st.get_var(result)[4]]
          quad_lst.append(quad)

          if debug : print("---encontre esto---")
          if debug : print(left_op)
          if debug : print(right_op)
          # insertamos resultado en pila
          tmp_var_num += 1
          counter += 1
          operands_s.push(st.get_var(result)[4])
          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

def p_termino2(p):
  '''termino2 : MULTIPLICACION addFactor termino
             | DIVISION addFactor termino
             | '''  
  """Auxiliar termino que permite tener 1 o mas factores"""  

def p_addFactor(p):
  '''addFactor : '''
  """Agregamos un factor a la pila"""
  if len(p) > 0:
    if operands_s.size() > 0:
      operators_s.push(p[-1])

def p_factor(p):
    '''factor : PARENIZQUIERDO crearFondoFalso logico PARENDERECHO quitarFondoFalso
            | cte 
            '''
    """Factor numerico o mediante IDs"""

def p_llamada(p):
    '''llamada : buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub'''
    """Regla que describe la estructura de una llamada a funcion"""

def p_cteid(p):
    '''cteid : buscarId cteidaux''' 
    """Constante ID"""
    p[0] = p[-1]

def p_crearFondoFalso(p):
  '''crearFondoFalso : '''
  """Se crea un fondo falso para las operaciones anidadas"""
  if len(p) > 0:
    operators_s.push(p[-1])

def p_quitarFondoFalso(p):
  '''quitarFondoFalso : '''
  """Se quita el fondo falso para terminar con una operacion anidada"""
  if len(p) > 0:
    operators_s.pop()

# Condicion que maneja si, sino, entonces
def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO logico PARENDERECHO generarCond ENTONCES bloque condicionaux'''
    """Regla que describe la estructura de un estatuto condicional"""

def p_generarCond(p):
  '''generarCond : '''
  """Regla que genera el cuadruplo correspondiente al estatuto condicional"""
  if len(p) > 0:
    tipo_exp = types_s.pop()
    # verificamos el tipo de expresion pendiente
    if tipo_exp != 'bool':
      raise TypeError('Tipos incompatibles.')
    else:
      # generamos el cuadruplo e inseramos el contador de cuadruplo en la pila de saltos
      result = operands_s.pop()
      global counter
      quad = ['GotoF', result, "", ""]
      quad_lst.append(quad)
      counter += 1
      jumps_s.push(counter - 1)

def p_condicionaux(p):
   '''condicionaux : SINO ENTONCES generarElse bloque rellenarCond
                  | rellenarCond '''
   """Auxiliar de condicion que maneja el sino"""

def p_generarElse(p):
  '''generarElse : '''
  """Regla que genera el cuadruplo correspondiente al sino"""
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
  """Regla que obtiene de la pila de saltos el numero de cuadruplo
  correspondiente para rellenar una condicion"""
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
    """Regla que describe la estructura de un ciclo en el lenguaje"""

def p_crearRegreso(p):
  '''crearRegreso : '''
  """Regla que genera el cuadruplo correspondiente al goto para los ciclos"""
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
  """Regla que se encarga de generar el cuadruplo correspondiente a los ciclos"""
  if len(p) > 0:
    exp_type = types_s.pop()
    # verificamos que la expresion a evaluar sea booleana
    if (exp_type != 'bool'):
      if debug : print('tipo exp en condicion:', exp_type)
      raise TypeError('Tipos incompatibles en ciclo.')
    else:
      # generamos el cuadruplo
      result = operands_s.pop()
      quad = ['GotoF', result, "", ""]
      global counter
      quad_lst.append(quad)
      counter += 1
      jumps_s.push(counter - 1)

def p_insertarSalto(p):
  '''insertarSalto : '''
  """Regla para el manejo de la pila de saltos"""
  jumps_s.push(counter)

# Desplegar en consola  
def p_escritura(p):
    '''escritura : DESPLEGAR PARENIZQUIERDO expresion PARENDERECHO generarEscritura PUNTOYCOMA'''
    """Regla que describe la estructura del estatuto de entrada del lenguaje"""

def p_generarEscritura(p):
  '''generarEscritura : '''
  """Regla que genera el cuadruplo correspondiente al estatuto de escritura"""
  quad = ['escritura', "", "", operands_s.pop()]
  quad_lst.append(quad)
  global counter
  counter += 1

# Aceptar/ingresar info del usuario
def p_ingreso(p):
    '''ingreso : ENTRADA PARENIZQUIERDO cte PARENDERECHO generarEntrada PUNTOYCOMA'''
    """Regla que genera el cuadruplo correspondiente al estatuto de lectura"""

def p_generarEntrada(p):
  '''generarEntrada : '''
  """Regla que genera el cuadruplo correspondiente al estatuto de entrada"""
  global st
  global current_var_id
  global operands_s
  quad = ["entrada", "", "", operands_s.pop()]
 # quad = ["entrada", "", "", st.get_var(p[-4])[4]]
  quad_lst.append(quad)
  global counter
  counter += 1


def p_texto(p):
    '''texto : INSERTATEXTO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir texto"""

def p_rectangulo(p):
    '''rectangulo : INSERTARECTANGULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir un rectangulo"""

def p_triangulo(p):
    '''triangulo :  INSERTATRIANGULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir un triangulo"""

def p_circulo(p):
    '''circulo : INSERTACIRCULO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir un circulo"""

def p_ovalo(p):
    '''ovalo : INSERTAOVALO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir un ovalo"""

def p_punto(p):
    '''punto : INSERTAPUNTO getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir un punto"""

def p_linea(p):
    '''linea : INSERTALINEA getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir una linea"""

def p_curva(p):
    '''curva : INSERTACURVA getCurrentIDFun buscarFuncion saveFunID PARENIZQUIERDO generateERA llamadapar PARENDERECHO verifyArgCount generateGoSub PUNTOYCOMA'''
    """Funcion para incluir una curva"""

def p_error(p):
  """Funcion que maneja mensajes de error en la estructura de la sintaxis"""
  if debug : print("Error de sintaxis: '%s' en línea: %s."  % (p.value, p.lineno))

def get_type(symbol):
  """Funcion que obtiene el tipo de dato de una variable
  Argumentos: symbol con la variable
  Regreso: el tipo de la variable
  """
  if symbol == "verdadero" or symbol == "falso":
    return 'bool'
  t = str(type(symbol))[7:10]
  if t == 'int':
    return "entero"
  elif t == 'flo':
    return "flotante"
  elif len(symbol) == 3 and type(symbol) is str:
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