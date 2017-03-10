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
import ply.yacc as yacc
import sys
# obtenemos la lista de tokens generadas por el analizador lexico
from scanner_apodorax import tokens

# Reglas Gramaticales

function_dict = {}
#function_dict['global'] = {}
error_list = []
repeated_id = ''
scope = None

# Programa
def p_program(p):
  '''program : PROGRAMA ID inicializar DOSPUNTOS declaracion function INICIO bloque FIN'''

def p_inicializar(p):
	'''inicializar : '''
	pass
	global scope
	global function_dict
	function_dict['global'] = {}
	scope = 'global'
	p[0]="Interpretado Correctamente"

# Constante ID
def p_cteid(p):
    '''cteid : ID buscarId cteidaux'''
    p[0] = p[1]

def p_buscarId(p):
	''' buscarId : '''
	pass
	if len(p) >= 1:
		error_message = buscarVar(p[-1])
		if error_message is None:
			# TODO: necesario???
			p[0] = p[-1]
		else:
			raise KeyError(p[-1] + ' ' + error_message)


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
	if len(p) >= 1:
		global function_dict
		error_message = buscarFuncion(p[-1])
		if error_message is None:
			p[0] = p[-1]
		else:
			raise KeyError(error_message)



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
	global scope
	scope = 'global'

def p_idFunctionCheck(p):
	''' idFunctionCheck : '''
	if len(p) >= 1:
	   global function_dict
	   global scope
	   error_message = insertarFuncion(p[-1])
	   if error_message is None:
	   	scope = p[-1]
	   else:
	   	raise KeyError(error_message + ":"  + "'" + p[-1] + "'")

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
  		global function_dict
  		global scope
  		error_message = insert_variable(p[-2], p[-1], scope)
  		if error_message != None:
  			repeated_id = p[-1]
  			raise KeyError("Variable repetida: " + "'" + repeated_id + "'")

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
    '''exp : termino exp2'''

# Auxiliar de exp que permite tener 1 o más terminos
def p_exp2(p):
    '''exp2 : SUMA exp
          | RESTA exp
          | '''

# Termino multiplicacion y division
def p_termino(p):
  '''termino : factor termino2'''

# Auxiliar termino que permite tener 1 o mas factores
def p_termino2(p):
  '''termino2 : MULTIPLICACION termino
             | DIVISION termino
             | '''

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
  '''
  print 'adlrgkhskjf'
  for em in error_list:
    print '{} : {}'.format(em, repeated_id)
  if p: print('Error de sintaxis.')
  '''
  print("Error de sintaxis: '%s' en línea: %s."  % (p.value, p.lineno))
  pass


parser = yacc.yacc()

def buscarFuncion(fun_id):
	global function_dict
	if fun_id not in function_dict:
		return "La funcion '" + fun_id + "' no esta desclarada."
	else:
		return None

def buscarVar(var_id):
	global function_dict
	global scope
	if function_dict.get(scope).get(var_id) is None:
		if function_dict.get('global').get(var_id) is None:
			return ' no ha sido declarada.'
		else:
			return None
	else:
		return None

def insert_variable(var_type, var_id, var_scope):
    global function_dict
    if function_dict.get(var_scope) is not None:
      if function_dict.get(var_scope).get(var_id) is None:
        function_dict[var_scope][var_id] = [var_id, var_type, scope]
        return None
      else:
      	return 'Variable repetida.'
    else:
    	raise KeyError('Error en estructura de funciones.')

def insertarFuncion(fun_id):
	global function_dict
	if function_dict.get(fun_id) is None:
		function_dict[fun_id] = {}
		return None
	else:
		return "Funcion repetida"

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