#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------
#
#  Jose Gonzalez Ayerdi - A01036121
#  Martha Benavides - 
#  Proyecto Final, Diseño de Compiladores
#  Sintaxis para el lenguaje APODORAX
#  Gramatica regular para el analisis sintactico con PLY
# ------------------------------------------------------------

import ply.yacc as yacc
import sys
# obtenemos la lista de tokens generadas por el analizador lexico
from scanner import tokens

# Reglas Gramaticales
def p_empty:
  '''empty:'''
  pass

def p_program(p):
  '''program : PROGRAMA ID DOSPUNTOS declaracion function INICIO bloque FIN'''

def p_declaracion(p):
  '''declaracion : VAR tipo asignacion declaracion
               | empty'''

def p_asignacion(p):
  '''asignacion : id asignacion2 '''

def p_asignacion2(p):
  '''asignacion2: IGUAL asignacionaux
               | CORCHETEIZQ CENTERO CORCHETEDER PUNTOYCOMA
               | PUNTOYCOMA
               | empty'''

def p_asignacionaux(p):
  '''asignacionaux : expresion PUNTOYCOMA
                  | llamada'''

def p_function(p):
  '''function : FUNCION tiporegreso ID PARENIZQUIERDO funtionaux PARENDERECHO bloquefun'''

def p_functionaux(p):
   '''functionaux : VAR tipo ID
                 | VAR tipo ID COMA functionaux
                 | empty'''

def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO bloquefun2 bloquefun3 LLAVEDERECHO
                | LLAVEIZQUIERDO bloquefun2 bloquefun3 regreso LLAVEDERECHO'''

def p_bloquefun2(p):
  '''bloquefun2 : empty
               | declaracion
               | declaracion bloquefun2'''

def p_bloquefun3(p):
  '''bloquefun3 : empty
               | estatuto
               | estatuto bloquefun3'''

def p_bloque(p):
   '''bloque : LLAVEIZQUIERDO bloquefun3 LLAVEDERECHO'''

def p_estatuto(p):
   '''estatuto : ingreso | texto | rectangulo | circulo | ovalo
              | triangulo | punto | linea | llamada | asignacion
              | condicion | ciclo | escritura'''

def p_asignacionarreglo(p):
    '''asignacionarreglo : ID CORCHETEIZQ exp CORCHETEDER IGUAL asignacionvalor'''

def p_asignacionvalor(p): 
    '''asignacionvalor : cte PUNTOYCOMA
                      | llamada'''

def p_discon(p):
    '''discon : CONJUNCION expresion
            | DISJUNCION expresion
            | CONJUNCION expresion discon
            | DISJUNCION expresion discon
            | empty'''

def p_negacion(p):
    '''negacion : empty 
              | NO'''   

def p_expresion(p): 
    '''expresion : negacion exp expresionaux discon
                | color'''  

def p_expresionaux(p) :
    '''expresionaux : empty
                   | comparacion exp'''

def p_exp(p):
    '''exp :  termino SUMARESTA exp
          | termino'''

def p_termino(p):
    '''termino: factor MULTIPLICACIONDIVISION termino
             | factor'''

def p_factor(p):
    '''factor: PARENIZQUIERDO expresion PARENDERECHO
            | expresion
            | cte
            | SUMARESTA cte'''

def p_cte(p):
    '''cte : cteid | CENTERO | CFLOTANTE | CCADENA
           | CCARACTER | CBOOL'''

def p_cteid(p):
    '''cteid : ID cteidaux'''

def p_cteidaux(p):
    '''cteidaux: empty
               | CORCHETEIZQ exp CORCHETEDER
               | PARENIZQUIERDO exp PARENDERECHO'''

def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO factor PARENDERECHO ENTONCES bloque condicionaux'''

def p_condicionaux(p):
   '''condicionaux : empty
                  | SINO ENTONCES bloque'''

def p_condicionaux(p):
    '''condicionaux: ''' 

def p_comparacion(p):
    '''comparacion : COMPARACION | IGUALDAD | DIFERENTE'''

def p_llamada(p):
    '''llamada : ID PARENIZQUIERDO llamada2 PARENDERECHO PUNTOYCOMA'''

def p_llamada2(p):
    '''llamada2 : expresion
              | expresion COMA llamada2'''

def p_argumentos(p):
    '''argumentos : ID
                | ID COMA argumentos
                | ID CORCHETEIZQ CENTERO CORCHETEDER
                | ID CORCHETEIZQ CENTERO CORCHETEDER COMA argumentos
                | cte
                | cte COMA argumentos'''

def p_color(p):
    '''color : NEGRO | GRIS | AZUL | AMARILLO | VERDE | ROJO'''

def p_ciclo(p):
    '''ciclo : MIENTRAS PARENIZQUIERDO factor PARENDERECHO bloque'''

def p_escritura(p):
    '''entrada : DESPLEGAR PARENIZQUIERDO escritura2 PARENDERECHO PUNTOYCOMA'''

def p_escritura(p):
    '''entrada2 : expresion
                 | expresion COMA escritura2'''

def p_regreso(p):
    '''regreso : REGRESAR expresion PUNTOYCOMA
              | empty'''

def p_tiporegreso(p):
    '''tiporegreso : tipo | VACIO'''

def p_tipo(p):
    '''tipo: ENTERO | FLOTANTE | CADENA | CARACTER | BOOL'''

def p_ingreso(p):
    '''ingreso : ENTRADA PARENIZQUIERDO ingreso2 PARENDERECHO PUNTOYCOMA'''

def p_ingreso2(p):
    '''ingreso2: cteid
              | cteid COMA ingreso2'''

def p_coordenada(p):
    '''coordenada : CENTERO | CFLOTANTE'''

def p_args(p):
    '''args : expresion
           | expresion COMA args'''

def p_texto(p):
    '''texto: INSERTATEXTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_rectangulo(p):
    '''rectangulo: INSERTARECTANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_triangulo(p):
    '''triangulo: INSERTATRIANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_circulo(p):
    '''circulo: INSERTACIRCULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_ovalo(p):
    '''ovalo: INSERTAOVALO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_punto(p):
    '''punto: INSERTAPUNTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_linea(p):
    '''linea: INSERTALINEA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_curva(p):
    '''curva: INSERTACURVA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_error(p):
    print("Error de sintaxis: '%s'"  % t.value)
    
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