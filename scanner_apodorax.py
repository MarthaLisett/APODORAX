# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#  José González Ayerdi - A01036121
#  3/02/17
#  Tarea 3, Diseño de Compiladores
#  Sintaxis para el lenguaje MyLittleDuck2017
#  Archivo con expresiones regulares para el análisis lexico con PLY
# ------------------------------------------------------------
import ply.lex as lex

# tupla con los nombres de los tokens
tokens = (
   'PROGRAMA',
   'ID',
   'INICIO',
   'FIN',
   'FUNCION',
   'VAR',
   'CONJUNCION',
   'DISYUNCION',
   'CENTERO',
   'ENTERO',
   'CFLOTANTE',
   'FLOTANTE',
   'CCADENA',
   'CADENA',
   'CCARACTER',
   'CARACTER',
   'BOOL',
   'SI',
   'NO',
   'SINO',
   'ENTONCES',
   'MIENTRAS',
   'ENTRADA',
   'VERDADERO',
   'FALSO',
   'VACIO',
   'DESPLEGAR',
   'REGRESAR',
   'MENORQUE',
   'MAYORQUE',
   'MAYORIGUAL',
   'MENORIGUAL',
   'DIFERENTE',
   'NEGRO',
   'GRIS',
   'AZUL',
   'AMARILLO',
   'VERDE',
   'ROJO',
   'INSERTATEXTO',
   'INSERTARECTANGULO',
   'INSERTACIRCULO',
   'INSERTACURVA',
   'INSERTAOVALO',
   'INSERTATRIANGULO',
   'INSERTAPUNTO',
   'INSERTALINEA',
   'IGUAL',
   'SUMA',
   'RESTA',
   'MULTIPLICACION',
   'DIVISION',
   'PARENIZQUIERDO',
   'PARENDERECHO',
   'CORCHETEIZQ',
   'CORCHETEDER',
   'LLAVEIZQUIERDO',
   'LLAVEDERECHO',
   'PUNTOYCOMA',
   'COMA',
   'DOSPUNTOS',
   'ASIGNACION',
)

# expresiones regulares que definen los tokens
t_CCADENA                      = r'\"(\\.|[^"])*\"'
t_CCARACTER                    = r'\'[a-z]\'|\'[A-Z]\''
t_PUNTOYCOMA                   = r'\;'
t_DOSPUNTOS                    = r'\:'
t_COMA                         = r'\,'
t_PARENIZQUIERDO               = r'\('
t_PARENDERECHO                 = r'\)'
t_LLAVEIZQUIERDO               = r'\{'
t_LLAVEDERECHO                 = r'\}'
t_CORCHETEIZQ                  = r'\['
t_CORCHETEDER                  = r'\]'
t_SUMA                         = r'\+'
t_RESTA                        = r'\-'
t_MULTIPLICACION               = r'\*'
t_DIVISION                     = r'\/'
t_MENORQUE                     = r'\<'
t_MAYORQUE                     = r'\>'
t_MAYORIGUAL                   = r'\<\='
t_MENORIGUAL                   = r'\>\='
t_ASIGNACION                   = r'\='
t_IGUAL                        = r'\=\='
t_DIFERENTE                    = r'\!\='
t_CONJUNCION                   = r'\&\&'
t_DISYUNCION                   = r'\|\|'

reserved = {
   'si'                : 'SI',
   'sino'              : 'SINO',
   'no'                : 'NO',
   'entonces'          : 'ENTONCES',
   'entero'            : 'ENTERO',
   'flotante'          : 'FLOTANTE',
   'cadena'            : 'CADENA',
   'caracter'          : 'CARACTER',
   'bool'              : 'BOOL',
   'verdadero'         : 'VERDADERO',
   'falso'             : 'FALSO',
   'inicio'            : 'INICIO',
   'fin'               : 'FIN',
   'var'               : 'VAR',
   'funcion'           : 'FUNCION',
   'entrada'           : 'ENTRADA',
   'mientras'          : 'MIENTRAS',
   'desplegar'         : 'DESPLEGAR',
   'regresar'          : 'REGRESAR',
   'programa'          : 'PROGRAMA',
   'negro'             : 'NEGRO',
   'gris'              : 'GRIS',
   'azul'              : 'AZUL',
   'amarillo'          : 'AMARILLO',
   'verde'             : 'VERDE',
   'rojo'              : 'ROJO',
   'vacio'             : 'VACIO',
   'insertaTexto'      : 'INSERTATEXTO',
   'insertaRectangulo' : 'INSERTARECTANGULO',
   'insertaTriangulo'  : 'INSERTATRIANGULO',
   'insertaCirculo'    : 'INSERTACIRCULO',
   'insertaOvalo'      : 'INSERTAOVALO',
   'insertaPunto'      : 'INSERTAPUNTO',
   'insertaCurva'      : 'INSERTACURVA',
   'insertaLinea'      : 'INSERTALINEA',
}

def t_CFLOTANTE (t):
    r'([\+|-]?[0-9]+[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_CENTERO(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

# funcion con la regla para definir la identificacion de un ID TODO:regex para id comienza con mayusculas??
def t_ID(t):
    r'[a-zA-Z](_?[a-zA-Z0-9]+)*'
    t.type = reserved.get(t.value,'ID')
    return t
# funcion para saber el numero de linea que se esta analizando
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

# se ignoran los espacios en blanco
t_ignore  = ' \t\r'

# manejo de errores
def t_error(t):
    print("Caracter desconocido: '%s' en linea:'%s'" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# manejo de comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# construccion del lexer
lexer = lex.lex()

data = '''  = "alicia" '''

#data_err = '''? | .'''

'''
# string para probar el analizador lexico con tokens incorrectos
# se corre el lexer con el string de prueba, descomentar para probar
lexer.input(data)
# se generan los tokens y se verifica que sean validos
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)  # se imprime el tipo de token que se encontro
'''