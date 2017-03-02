#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
#  Jose Gonzalez Ayerdi - A01036121
#  Martha Benavides - 
#  Proyecto Final, Diseño de Compiladores
#  Sintaxis para el lenguaje APODORAZ
#  Gramatica regular para el análisis sintactico con PLY
# ------------------------------------------------------------

import ply.yacc as yacc
import sys
# obtenemos la lista de tokens generadas por el analizador lexico
from scanner import tokens

''' a continuacion de definen las reglas para determinar la gramatica '''

def p_programa(p):
  ''' programa : ID declaracion funcion INICIO bloque FIN '''

def p_declaracion(p):
  '''declaracion : 
   empty | VAR tipo ID decaracion_aux '''

def p_declaracion_aux(p):
  '''delcaracion_aux : asignacion | asignacion declaracion | declaracion2 PUNTO_COMA | declaracion2 PUNTO_COMA declaración'''

def p_decalracion2(p):
  '''declaracion2 : empty | CORCHETE_IZQ C_ENTERO CORCHETE_DER'''

def p_asignacion(p):
  ''' asignacion : IGUAL asignacion2  '''

def p_asignacion2(p):
  ''' asignacion2 : expresion PUNTO_COMA | llamada ''' 

def p_funcion(p):
  ''' funcion : tipo_regreso ID PARENTESIS_IZQ funcion2 PARENTESIS_DER bloquefun'''

def p_funcion2(p):
  ''' funcinon2 :  empty | tipo ID | tipo ID COMA funcion2 '''

def p_bloquefun(p):
  ''' bloquefun : LLAVE_IZQ bloquefun2 regreso LLAVE_DER '''

def p_bloquefun2(p):
  ''' bloquefun2 : declaracion_fun estatuto_fun  '''

def p_declaracion_fun(p):
  ''' declaracion_fun : empty | declaracion | declaracion declaracion_fun '''

def p_estatuto_fun(p):
  '''  estatuto_fun : eempty | estatuto | estatuto estatuto_fun '''

def p_bloque(p):
  ''' bloque : LLAVE_IZQ LLAVE_DER | LLAVE_IZQ estatuto LLAVE_DER '''

def p_estatuto(p):
  ''' estatuto : entrada | texto | rectangulo | circulo | ovalo | triangulo | punto | linea | llamada | asignacion | condicion | ciclo '''

def p_asignacion_arreglo(p):
  ''' asignacion_arreglo : ID CORCHETE_IZQ exp CORCHETE_DER IGUAL asignacion_valor '''

def p_asignacion_valor(p):
  ''' asignacion_valor : cte PUNTO_COMA | llamada '''

def p_expresion(p):
  ''' expresion : color | not_expresion exp expresion2 dis_con '''

def p_not_expresion(p):
  ''' not_expresion : empty | negacion '''

def p_expresion2(p):
  ''' expresion2 : empty | comparacion exp '''

def p_exp(p):
  ''' exp : termino ops '''

def p_ops(p):
  ''' ops : epmpty | MAS exp | MENOS exp '''

def p_termino(p):
  ''' termino : epmpty | POR factor | ENTRE factor '''

def p_factor(p):
  ''' factor : PARENTESIS_IZQ expresion PARENTESIS_DERECHO | cte | MAS cte | MENOS cte '''

def p_cte(p):
  ''' cte : cte_id | C_ENTERO | C_FLOTANTE | C_CADENA | C_BOOL | C_CARACTER '''

def p_cte_id(p):
  ''' cte_id : emtpy | CORCHETE_IZQ exp CORCHETE_DER | PARENTESIS_IZQ exp PARENTESIS_DER '''

def p_condicion(p):
  ''' condicion : SI PARENTESIS_IZQ expresion PARENTESIS_DER ENTONCES BLOQUE condicion2 '''

def p_condicion2(p):
  ''' condicion2 : empty | SINO ENTONCES bloque '''

def p_comparacion(p):
  ''' comparacion : MENOR | MAYOR | DIFERENTE | IGUAL | MENOR_IGUAL | MAYOR_IGUAL '''

def p_llamada(p):
  ''' llamada : ID PARENTESIS_IZQ llamada2 PARENTESIS_DER PUNTO_COMA'''

def p_llamada2(p):
  '''  llamada2 : expresion | expresion COMA llamada2 '''

## TODO: wtf nadie está usando esta regla!!
def p_argumentos(p):
  ''' argumentos : CTE | ID | ID CORCHETE_IZQ EXP CORCHETE_DER | ID CORCHETE_IZQ EXP CORCHETE_DER COMA argumentos | empty'''

def p_color(p):
  ''' color : NEGRO | GRIS | AZUL | AMARILLO | VERDE | ROJO  '''

def p_ciclo(p):
  ''' color : MIENTRAS PARENTESIS_IZQ expresion PARENTESIS_DER bloque '''

def p_negacion(p):
  '''negacion : empty | NO  '''

def dis_con(p):
  ''' dis_con : empty | CONJUNCION expresion | CONJUNCION expresion dis_con | DISJUNCION expresion | DISJUNCION expresion dis_con '''

def p_escritura(p):
  ''' escritura : DESPLEGAR PARENTESIS_IZQ escritura2 PARENTESIS_DER PUNTO_COMA'''

def p_escritura2(p):
  ''' escritura2 : expresion | expresion COMA escritura2 '''

def p_regreso(p):
  ''' regreso : empty | REGRESAR expresion PUNTO_COMA '''

def p_tipo_regreso(p):
  '''  tipo_regreso : tipo | VACIO '''

def p_tipo(p):
  ''' tipo : CADENA | ENTERO | FLOTANTE | BOOL | CARACTER '''

def p_entrada(p):
  ''' entrada : ENTRADA PARENTESIS_IZQ entrada2 PARENTESIS_DER PUNTO_COMA '''

def p_entrada2(p):
  ''' entrada2 : cte_id | cte_id COMA entrada2 '''

def p_coordenada(p):
  ''' coordenada : ENTERO | FLOTANTE '''

def p_texto(p):
  ''' texto : INSERTATEXTO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_rectangulo(p):
  ''' rectangulo : INSERTAECTANGULO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_circulo(p):
  ''' circulo : INSERTACIRCULO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_ovalo(p):
  ''' ovalo : INSERTAOVALO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_triangulo(p):
  ''' triangulo : INSERTATRIANGULO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_punto(p):
  ''' punto : INSERTAPUNTO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_linea(p):
  ''' linea : INSERTARTRIANGULO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_curva(p):
  ''' curva : INSERTARTRIANGULO PARENTESIS_IZQ args PARENTESIS_DER PUNTO_COMA  '''

def p_args(p):
  '''args : expresion | expresion COMA args  '''

def p_emtpy:
  'empty:'
  pass


# funcion para manejar errores
def p_error(p):
  print("Error de sintaxis!")

# se contruye el parser
parser = yacc.yacc()

# lista para guardar la lineas de la entrada
lines = []

# se lee linea por linea el contenido de un archivo
# especificado como argumento al momento de correr el programa
for line in sys.stdin:
  stripped = line.strip()
  if not stripped: break
  lines.append(stripped)
# se crea un solo string con los strings en la lista
input = ' '.join(lines)
# se parsea la entrada
#print input
result = parser.parse(input)

#if result is None:
  #print result#'Sintaxis correcta.'
