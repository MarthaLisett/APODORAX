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
current_id    = ""
# Programa
def p_program(p):
  '''program : PROGRAMA ID inicializar DOSPUNTOS declaracion function INICIO bloque FIN generarCuadruplos '''

def p_generarCuadruplos(p):
  '''generarCuadruplos : '''
  archivo = open('cuadruplos.bigsheep', 'w')
  dic = { key : value  for key, value in enumerate(quad_lst)}
  od = collections.OrderedDict(sorted(dic.items()))
  with open('cuadruplos.bigsheep', 'w') as f:
    for key, value in dic.items():
        f.write('%s:%s\n' % (key, value))

def p_inicializar(p):
  '''inicializar : '''
  pass
  p[0]="Interpretado Correctamente."

def p_guardarId(p):
  ''' guardarId : '''
  if len(p) >= 1:
    if (not operands_s.isEmpty()):
      if operators_s.isEmpty():
        while not operands_s.isEmpty():
          operands_s.pop()
          types_s.pop()
        operands_s.push(p[-3])
        if st.get_var(p[-3]) is not None:
          types_s.push(st.get_var(p[-3])[1])
      else:
        operands_s.push(st.get_var(p[-3])[0])
    else:
      operands_s.push(st.get_var(p[-3])[0])
      types_s.push(st.get_var(p[-3])[1])


def p_buscarId(p):
  '''buscarId : '''
  if len(p) >= 1:
    global st
    global current_var_id
    print("recibi:", current_var_id)
    st.search_variable(current_var_id)

 # Constante ID declaracion
def p_cteid_declaracion(p):
    '''cteid_declaracion : ID cteidaux'''
    p[0] = p[1]

# Auxiliar Constante ID
def p_cteidaux(p):
    '''cteidaux : CORCHETEIZQ exp CORCHETEDER
               | '''

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

def p_icrementParamCounter(p):
  '''icrementParamCounter : '''
  global args_count
  args_count += 1

def p_addParamCount(p):
  '''addParamCount : '''
  global args_count
  print("Valor args_count:", args_count)
  st.add_no_params(args_count)
  args_count = 0

def p_agregarParam(p):
  '''agregarParam : '''
  if len(p) > 0:
    st.insert_variable(p[-2], p[-1])

# Auxiliar Parametros de las funciones
def p_functionpam2(p):
  '''functionpam2 : COMA icrementParamCounter functionpam
                    | icrementParamCounter '''

# Funcion
def p_function(p):
    '''function : FUNCION tiporegreso ID idFunctionCheck createGlobal PARENIZQUIERDO functionpam addParamCount PARENDERECHO bloquefun finishFun resetScope function
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
    
    if not st.function_exists(p[1]):
      p[0] = p[1]
      if st.get_var(p[1]) is not None and get_type(p[1]) != "entero" and len(st.get_var(p[1])) >= 4:
        operands_s.push(st.get_var(p[1])[0])
        types_s.push(st.get_var(p[1])[1])
      else:
        operands_s.push(p[1])
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
    '''declaracion : VAR tipo cteid_declaracion revisarId PUNTOYCOMA countVar declaracion
                | '''

def p_countVar(p):
  '''countVar : '''
  global fun_var_count
  fun_var_count += 1

def p_revisarId(p):
  '''revisarId : '''
  pass
  if len(p) >= 1:
    global st
    st.insert_variable(p[-2], p[-1])

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

def p_saveFunID(p):
  '''saveFunID : '''
  global fun_calling
  global current_id 
  fun_calling = current_id

def p_generateGoSub(p):
  '''generateGoSub : '''
  quad = ['GOSUB', current_id, '', 'dir']
  quad_lst.append(quad)
  global type_pointer
  global k
  global counter
  k = 0
  type_pointer = None
  counter += 1
  var_lst = st.get_var(current_id)
  var_type = st.get_var_type(var_lst[0])
  print("generando sub------")
  print('type:', var_type)
  print('val:', var_lst[0])
  operands_s.push(var_lst[0])
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

# Auxiliar asignacionizq
def p_asignacionizqaux(p):
  '''asignacionizqaux : CORCHETEIZQ exp CORCHETEDER
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
          result = right_op
          st.set_var_val(left_op, result)
          print("resultado final:", st.get_var(left_op))
          global counter
          result = right_op#'t_' + str(counter)
          quad = [operator, result, "", left_op]
          quad_lst.append(quad)
          counter += 1
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

# Auxiliar de asignacion
def p_asignacionaux(p):
  '''asignacionaux : exp '''

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
              | ID getCurrentID llamada PUNTOYCOMA
              | asignacion
              | condicion
              | ciclo'''

def p_getCurrentID(p):
  '''getCurrentID : saveVarID'''
  global current_id
  current_id = p[-1]

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

          print('lo:', left_op)
          print('ro:', right_op)
          print('op:', operator)
          '''
          if operator == '&&':
            result = (lo and ro)
          elif operator == '||': 
            print('res:', (left_op or right_op))
            result = (lo or ro) 
          
          if result:
            result = "verdadero"
          else:
            result = "falso"
          '''
          global counter
          global tmp_var_num
          #tipo_actual = get_type(result)
          result = 't_' + str(tmp_var_num)
          quad = [operator, left_op, right_op, result]
          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(result)
          types_s.push(result_type)
          print("resultado bool:", result)
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
          quad = [operator, left_op, right_op, result]
          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(result)
          print("resultado if:", result)
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
          quad = [operator, left_op, right_op, result]
          quad_lst.append(quad)
          counter += 1
          tmp_var_num += 1
          operands_s.push(result)
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
          quad = [operator, left_op, right_op, result]
          quad_lst.append(quad)
          tmp_var_num += 1
          counter += 1
          operands_s.push(result)
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
  print("counter else:", counter)
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
      print('tipo exp en condicion:', exp_type)
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
    '''ingreso : ENTRADA PARENIZQUIERDO ID saveVarID cteid PARENDERECHO generarEntrada PUNTOYCOMA'''

def p_generarEntrada(p):
  '''generarEntrada : '''
  quad = ["entrada", "", "", p[-2]]
  quad_lst.append(quad)
  global counter
  counter += 1

# Argumentos para las funciones de figura, pueden ser cualquier constante o color
def p_args(p):
    '''args : logico args2'''

# Auxiliar argumentos
def p_args2(p):
    '''args2 : COMA args
            | '''

# Funcion para incluir texto
def p_texto(p):
    '''texto : INSERTATEXTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir un rectangulo
def p_rectangulo(p):
    '''rectangulo : INSERTARECTANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir un triangulo
def p_triangulo(p):
    '''triangulo :  INSERTATRIANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir un circulo
def p_circulo(p):
    '''circulo : INSERTACIRCULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir un ovalo
def p_ovalo(p):
    '''ovalo : INSERTAOVALO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir un punto
def p_punto(p):
    '''punto : INSERTAPUNTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir una linea
def p_linea(p):
    '''linea : INSERTALINEA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

# Funcion para incluir una curva
def p_curva(p):
    '''curva : INSERTACURVA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_error(p):
  print("Error de sintaxis: '%s' en línea: %s."  % (p.value, p.lineno))

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
        print(EOFError)
  else:
    print('No existe el archivo')