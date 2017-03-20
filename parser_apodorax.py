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
import ply.yacc as yacc
import sys
# obtenemos la lista de tokens generadas por el analizador lexico
from scanner_apodorax import tokens

# Reglas Gramaticales

precedence = (
    ('nonassoc', 'MENORQUE', 'MAYORQUE'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

operators_s = Stack()
operands_s  = Stack()
types_s     = Stack()
quad_s      = Stack()
error_list  = []
st          = symbol_table()
sc          = semantic_cube()
# Programa
def p_program(p):
  '''program : PROGRAMA ID inicializar DOSPUNTOS declaracion function INICIO bloque FIN'''

def p_inicializar(p):
  '''inicializar : '''
  pass
  p[0]="Interpretado Correctamente"

# Constante ID
def p_cteid(p):
    '''cteid : ID buscarId guardarId cteidaux'''
    p[0] = p[1]

def p_guardarId(p):
	''' guardarId : '''
	if len(p) >= 1:
		if (not operands_s.isEmpty()):
			if operators_s.isEmpty():
				while not operands_s.isEmpty():
					operands_s.pop()
					types_s.pop()
				operands_s.push(p[-2])
				if st.get_var(p[-2]) is not None:
					types_s.push(st.get_var(p[-2])[1])
		else:
			operands_s.push(p[-2])
			types_s.push(st.get_var(p[-2]))


def p_buscarId(p):
  '''buscarId : '''
  pass
  if len(p) >= 1:
    global st
    st.search_variable(p[-1])

 # Constante ID declaracion
def p_cteid_declaracion(p):
    '''cteid_declaracion : ID cteidaux'''
    p[0] = p[1]

# Auxiliar Constante ID
def p_cteidaux(p):
    '''cteidaux : CORCHETEIZQ exp CORCHETEDER
               | PARENIZQUIERDO exp PARENDERECHO
               | '''

def p_buscarFuncion(p):
  ''' buscarFuncion : '''
  pass
  if len(p) >= 1:
    global st
    st.search_function(p[-1])

# Instrucciones de las funciones
def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO declaracion bloqueaux regreso LLAVEDERECHO'''

# Tipo de regreso de las funciones
def p_tiporegreso(p):
    '''tiporegreso : tipo
                   | VACIO'''

# Parametros de las funciones
def p_functionpam(p):
    '''functionpam : VAR tipo ID revisarId functionpam2
                 | '''
    
# Auxiliar Parametros de las funciones
def p_functionpam2(p):
   '''functionpam2 : COMA functionpam
                    | '''
# Funcion
def p_function(p):
    '''function : FUNCION tiporegreso ID idFunctionCheck PARENIZQUIERDO functionpam PARENDERECHO bloquefun resetScope function
            | '''

def p_resetScope(p):
  '''resetScope : '''
  st.scope ='global'

def p_idFunctionCheck(p):
  ''' idFunctionCheck : '''
  if len(p) >= 1:
     global st
     st.insert_function(p[-1], p[-2])

# Valores constantes
def p_cte(p):
    '''cte : cteid
           | CENTERO
           | CFLOTANTE
           | CCADENA
           | CCARACTER
           | VERDADERO
           | FALSO'''
    p[0] = p[1]

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
    '''declaracion : VAR tipo cteid_declaracion revisarId PUNTOYCOMA declaracion
                | '''

def p_revisarId(p):
	'''revisarId : '''
	pass
	if len(p) >= 1:
		global st
		st.insert_variable(p[-2], p[-1])

# Return de las funciones
def p_regreso(p):
    '''regreso : REGRESAR exp PUNTOYCOMA
              | '''

# Bloque
def p_bloque(p):
   '''bloque : LLAVEIZQUIERDO bloqueaux LLAVEDERECHO'''

# Auxiliar bloque permite poner 0 o mas estatutos
def p_bloqueaux(p): 
  '''bloqueaux : estatuto bloqueaux
              | '''

# Llamada a funcion
def p_llamada(p):
    '''llamada : ID buscarFuncion PARENIZQUIERDO llamadapar PARENDERECHO'''

# Parametros de la llamada
def p_llamadapar(p):
    '''llamadapar : exp llamadaparaux
                 | '''

# Auxiliar de parametros de llamada
def p_llamadaparaux(p):
    '''llamadaparaux : COMA llamadapar
                  | '''

# Lado izquierdo de la asignacion para saber si es id normal o arreglo
def p_asignacionizq(p):
  '''asignacionizq : ID buscarId asignacionizqaux'''

# Auxiliar asignacionizq
def p_asignacionizqaux(p):
  '''asignacionizqaux : CORCHETEIZQ exp CORCHETEDER
                     | '''

# Asignacion de valores
def p_asignacion(p):
  '''asignacion : asignacionizq ASIGNACION asignacionaux PUNTOYCOMA'''

# Auxiliar de asignacion
def p_asignacionaux(p):
  '''asignacionaux : exp
                  | llamada'''

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
              | llamada PUNTOYCOMA
              | asignacion
              | condicion
              | ciclo'''

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
                  | DIFERENTE
                  | CONJUNCION
                  | DISYUNCION'''

# Expresion que permite la comparacion
def p_expresion(p): 
    '''expresion : negacion exp expresionaux
                | color'''  

# Auxiliar de expresion
def p_expresionaux(p) :
    '''expresionaux : comparacion exp
                   | '''

# Exp suma y resta
def p_exp(p):
    '''exp : termino checkExpTypes exp2 '''

def p_checkExpTypes(p):
  '''checkExpTypes : '''
  if len(p) >= 1:
    if operators_s.size() > 0:
      if operators_s.peek() == '+' or operators_s.peek() == '-':
        right_op    = operands_s.pop()
        print(right_op)
        right_type  = types_s.pop()
        left_op     = operands_s.pop()
        left_type   = types_s.pop()
        operator    = operators_s.pop()
        result_type = sc.verify_type_match(left_type, right_type, operator)
        if result_type != -1:
          result = left_op + right_op if operator is '+' else left_op - right_op
          quad = (operator, left_op, right_op, result)
          quad_s.push(quad)
          operands_s.push(result)
          types_s.push(result_type)
          # TODO: if any operand were a temporal space, return it to AVAIL
        else:
          raise TypeError("Tipos incompatibles.")

def p_addExp(p):
	''' addExp : '''
	if len(p) >= 1:
		if operands_s.size() > 1:
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
          result = left_op * right_op if operator is '*' else left_op / right_op
          quad = (operator, left_op, right_op, result)
          quad_s.push(quad)
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
  if len(p) >= 1:
    if operands_s.size() > 1:
      operators_s.push(p[-1])

# Factor numerico o mediante IDs
def p_factor(p):
    '''factor : PARENIZQUIERDO expresion PARENDERECHO
            | cte'''

# Condicion que maneja si, sino, entonces
def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO expresion PARENDERECHO ENTONCES bloque condicionaux'''

# Auxiliar de condicion que maneja el sino
def p_condicionaux(p):
   '''condicionaux : SINO ENTONCES bloque
                  | '''

# Colores a usar en las figuras
def p_color(p):
    '''color : NEGRO
            | GRIS
            | AZUL
            | AMARILLO
            | VERDE
            | ROJO'''

# Mientras (while)
def p_ciclo(p):
    '''ciclo : MIENTRAS PARENIZQUIERDO expresion PARENDERECHO bloque'''

# Desplegar en consola
def p_escritura(p):
    '''escritura : DESPLEGAR PARENIZQUIERDO escrituraaux PARENDERECHO PUNTOYCOMA'''
 
# Auxiliar para desplegar
def p_escrituraaux(p):
    '''escrituraaux : exp escritura2aux'''

# Auxiliar para desplegar aceptando uno o mas exp
def p_escritura2aux(p):
    '''escritura2aux : COMA escrituraaux
                    | '''

# Aceptar/ingresar info del usuario
def p_ingreso(p):
    '''ingreso : ENTRADA PARENIZQUIERDO ingresoaux PARENDERECHO PUNTOYCOMA'''

# Auxiliar ingreso
def p_ingresoaux(p):
    '''ingresoaux : cteid ingreso2aux'''

# Auxiliar ingreso para que acepte uno o varios cteid
def p_ingreso2aux(p):
    '''ingreso2aux : COMA ingresoaux
                  | '''

# Argumentos para las funciones de figura, pueden ser cualquier constante o color
def p_args(p):
    '''args : expresion args2'''

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