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
  '''declaracion : VAR tipo ID asignacion declaracionaux'''

def p_declaracionaux(p):
    '''declaracionaux : declaracion
                    | '''

def p_asignacion(p):
  '''asignacion : asignacion2'''

def p_asignacion2(p):
  '''asignacion2 : ASIGNACION asignacionaux
               | CORCHETEIZQ CENTERO CORCHETEDER PUNTOYCOMA
               | PUNTOYCOMA'''

def p_asignacionaux(p):
  '''asignacionaux : ID asignacionaux3
                  | cte
                  | llamada'''
def p_asignacionaux3(p):
   '''asignacionaux3 : factor PUNTOYCOMA
                    | asignacionaux2 '''

def p_asignacionaux2(p):
  ''' asignacionaux2 : CORCHETEIZQ CENTERO CORCHETEDER PUNTOYCOMA
                    | PUNTOYCOMA
                    | '''

def p_function(p):
  '''function : FUNCION tiporegreso ID PARENIZQUIERDO functionaux PARENDERECHO bloquefun'''

def p_functionaux(p):
   '''functionaux : VAR tipo ID functionaux2
                 | '''

def p_functionaux2(p):
   '''functionaux2 : COMA functionaux
               | '''

def p_bloquefun(p):
  '''bloquefun : LLAVEIZQUIERDO bloquefun2 bloquefun3 bloquefunaux'''

def p_bloquefunaux(p):
    '''bloquefunaux : LLAVEDERECHO
                  | regreso LLAVEDERECHO'''

def p_bloquefun2(p):
  '''bloquefun2 : declaracion bloquefun2aux'''

def p_bloquefun2aux(p):
    '''bloquefun2aux : bloquefun2
                    | '''     

def p_bloquefun3(p):
  '''bloquefun3 : estatuto bloquefun3aux'''

def p_bloquefun3aux(p):
    '''bloquefun3aux : bloquefun3
                    | '''               

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
    '''discon : CONJUNCION expresion discon
            | DISYUNCION expresion discon
            | '''

def p_negacion(p):
    '''negacion : NO
              | '''   

def p_expresion(p): 
    '''expresion : negacion exp expresionaux discon
                | color'''  

def p_expresionaux(p) :
    '''expresionaux : comparacion exp
                   | '''

def p_exp(p):
    '''exp : termino exp2'''

def p_exp2(p):
    '''exp2 : SUMA exp
          | RESTA exp
          | '''

def p_termino(p):
    '''termino : factor termino2'''

def p_termino2(p):
  '''termino2 : MULTIPLICACION termino
             | DIVISION termino
             | '''

def p_factor(p):
    '''factor : PARENIZQUIERDO expresion PARENDERECHO
            | cte
            | SUMA factoresSuma
            | RESTA factoresResta'''

def p_factoresSuma(p):
  ''' factoresSuma : ID
                | cte'''

def p_factoresResta(p):
  ''' factoresResta : ID
                | cte'''

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
    '''cteidaux : CORCHETEIZQ exp CORCHETEDER
               | PARENIZQUIERDO exp PARENDERECHO
               | '''

def p_condicion(p):
    '''condicion : SI PARENIZQUIERDO factor PARENDERECHO ENTONCES bloque condicionaux'''

def p_condicionaux(p):
   '''condicionaux : SINO ENTONCES bloque
                  | '''

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
    '''llamada2 : expresion llamada2aux'''

def p_llamada2aux(p):
    '''llamada2aux : COMA llamada2
                  | '''

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
    '''escritura2 : expresion escritura2aux'''

def p_escritura2aux(p):
    '''escritura2aux : COMA escritura2
                    | '''

def p_regreso(p):
    '''regreso : REGRESAR expresion PUNTOYCOMA
              | '''

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
    '''ingreso2 : cteid ingreso2aux'''

def p_ingreso2aux(p):
    '''ingreso2aux : COMA ingreso2
                  | '''

def p_args(p):
    '''args : expresion args2'''

def p_args2(p):
    '''args2 : COMA args
            | '''

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