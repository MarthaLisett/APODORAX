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
function_dict['global'] = {}
error_list = []
repeated_id = ''
scope = 0

# Programa
def p_program(p):
  '''program : PROGRAMA ID DOSPUNTOS declaracion function INICIO bloque FIN'''
  #p[0]="Interpretado Correctamente"
  scope = 0
# Constante ID
def p_cteid(p):
    '''cteid : ID cteidaux'''

# Auxiliar Constante ID
def p_cteidaux(p):
    '''cteidaux : CORCHETEIZQ exp CORCHETEDER
               | PARENIZQUIERDO exp PARENDERECHO
               | '''

# Valores constantes
def p_cte(p):
    '''cte : cteid
           | CENTERO
           | CFLOTANTE
           | CCADENA
           | CCARACTER
           | VERDADERO
           | FALSO'''

# Tipo de dato
def p_tipo(p):
    '''tipo : ENTERO
            | FLOTANTE
            | CADENA
            | CARACTER
            | BOOL'''

# Declaracion de variables
def p_declaracion(p):
  '''declaracion : VAR tipo cteid PUNTOYCOMA declaracion
                | '''


def p_declaracion_error(p):
  '''declaracion : VAR tipo error PUNTOYCOMA declaracion
                | '''
  pass
  if len(p) > 1:
    error_message = insertVariable(p[0], p[1], scope)
    if error_message != None:
      repeated_id = p[3]
      error_list.append(error_message)


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

# Instrucciones de las funciones
def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO declaracion bloqueaux regreso LLAVEDERECHO'''

# Tipo de regreso de las funciones
def p_tiporegreso(p):
    '''tiporegreso : tipo
                   | VACIO'''

# Parametros de las funciones
def p_functionpam(p):
   '''functionpam : VAR tipo ID functionpam2
                 | '''

# Auxiliar Parametros de las funciones
def p_functionpam2(p):
   '''functionpam2 : COMA functionpam
                    | '''
# Funcion
def p_function(p):
  '''function : FUNCION tiporegreso ID PARENIZQUIERDO functionpam PARENDERECHO bloquefun function
            | '''

# Llamada a funcion
def p_llamada(p):
    '''llamada : ID PARENIZQUIERDO llamadapar PARENDERECHO'''

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
  '''asignacionizq : ID asignacionizqaux'''

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
  print 'adlrgkhskjf'
  for em in error_list:
    print '{} : {}'.format(em, repeated_id)
  if p: print('Error de sintaxis.')

  #print("Error de sintaxis: '%s' en linea: %s."  % (p.value, p.lineno))


def insertVariable(var_type, var_id, var_scope):
  if var_scope is 0:
    if function_dict.get('global').get(var_id) is None:
      function_dict['global'][var_id] = [var_id, var_type, scope]
      return None
    else:
      return 'Variable repetida.'

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