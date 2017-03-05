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
from scanner_apodorax import tokens

# Reglas Gramaticales
def p_program(p):
  '''program : PROGRAMA ID DOSPUNTOS declaracion function INICIO bloque FIN'''

def p_declaracion(p):
  '''declaracion : VAR tipo asignacion declaracion
               | empty'''

def p_asignacion(p):
  '''asignacion : ID asignacion2 '''

def p_asignacion2(p):
  '''asignacion2 : ASIGNACION asignacionaux
               | CORCHETEIZQ CENTERO CORCHETEDER PUNTOYCOMA
               | PUNTOYCOMA
               | empty'''

def p_asignacionaux(p):
  '''asignacionaux : expresion PUNTOYCOMA
                  | llamada'''

def p_function(p):
  '''function : FUNCION tiporegreso ID PARENIZQUIERDO functionaux PARENDERECHO bloquefun'''

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
   '''estatuto : ingreso
              | texto
              | rectangulo
              | circulo
              | ovalo
              | triangulo
              | punto
              | linea
              | llamada
              | asignacion
              | condicion
              | ciclo
              | escritura
              | curva'''



def p_discon(p):
    '''discon : CONJUNCION expresion
            | DISYUNCION expresion
            | CONJUNCION expresion discon
            | DISYUNCION expresion discon
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
    '''exp :  termino SUMA exp
          | termino RESTA exp
          | termino'''

def p_termino(p):
    '''termino : factor MULTIPLICACION termino
             | factor DIVISION termino
             | factor'''

def p_factor(p):
    '''factor : PARENIZQUIERDO expresion PARENDERECHO
            | expresion
            | cte
            | SUMA cte
            | RESTA cte'''


def p_cte(p):
    '''cte : cteid
           | CENTERO
           | CFLOTANTE
           | CCADENA
           | CCARACTER
           | VERDADERO
           | FALSO'''

def p_cteid(p):
    '''cteid : ID cteidaux'''

def p_cteidaux(p):
    '''cteidaux : empty
               | CORCHETEIZQ exp CORCHETEDER
               | PARENIZQUIERDO exp PARENDERECHO'''

def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO factor PARENDERECHO ENTONCES bloque condicionaux'''

def p_condicionaux(p):
   '''condicionaux : empty
                  | SINO ENTONCES bloque'''

def p_comparacion(p):
    '''comparacion : MENORQUE
                  | MAYORQUE
                  | MAYORIGUAL
                  | MENORIGUAL
                  | IGUAL
                  | DIFERENTE'''

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
    '''color : NEGRO
                | GRIS
                | AZUL
                | AMARILLO
                | VERDE
                | ROJO'''

def p_ciclo(p):
    '''ciclo : MIENTRAS PARENIZQUIERDO factor PARENDERECHO bloque'''

def p_escritura(p):
    '''escritura : DESPLEGAR PARENIZQUIERDO escritura2 PARENDERECHO PUNTOYCOMA'''

def p_escritura2(p):
    '''escritura2 : expresion
                 | expresion COMA escritura2'''

def p_regreso(p):
    '''regreso : REGRESAR expresion PUNTOYCOMA
              | empty'''

def p_tiporegreso(p):
    '''tiporegreso : tipo
                   | VACIO'''

def p_tipo(p):
    '''tipo : ENTERO
            | FLOTANTE
            | CADENA
            | CARACTER
            | BOOL'''

def p_ingreso(p):
    '''ingreso : ENTRADA PARENIZQUIERDO ingreso2 PARENDERECHO PUNTOYCOMA'''

def p_ingreso2(p):
    '''ingreso2 : cteid
              | cteid COMA ingreso2'''

def p_args(p):
    '''args : expresion
           | expresion COMA args'''

def p_texto(p):
    '''texto : INSERTATEXTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_rectangulo(p):
    '''rectangulo : INSERTARECTANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_triangulo(p):
    '''triangulo :  INSERTATRIANGULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_circulo(p):
    '''circulo : INSERTACIRCULO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_ovalo(p):
    '''ovalo : INSERTAOVALO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_punto(p):
    '''punto : INSERTAPUNTO PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_linea(p):
    '''linea : INSERTALINEA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_curva(p):
    '''curva : INSERTACURVA PARENIZQUIERDO args PARENDERECHO PUNTOYCOMA'''

def p_empty(p):
  '''empty : '''
  pass

def p_error(p):
    print("Error de sintaxis: '%s'"  % p.value)
    
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
      if (parser.parse(data, tracking=True) == 'Trabajando correctamente - APROPIADO'):
        print ('Trabajando correctamente - APROPIADO');
    except EOFError:
        print(EOFError)
  else:
    print('No existe el archivo')