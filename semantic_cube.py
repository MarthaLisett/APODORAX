class semantic_cube:

    # Formato del cubo semantico
    # var1        var2       -       +       *      /       &&      ||       >      <     >=     <=    !=    ==    =   

    # entero     entero     ENT     ENT     ENT   FLOAT   ERROR    ERROR    BOOL   BOOL  BOOL   BOOL  BOOL  BOOL  ENT
    # entero     flotante  FLOAT   FLOAT   FLOAT  FLOAT   ERROR    ERROR    BOOL   BOOL  BOOL   BOOL  BOOL  BOOL  ENT
    # entero     cadena    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR 
    # entero     caracter  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # entero     bool      ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
     
    # flotante   entero    FLOAT   FLOAT   FLOAT  FLOAT   ERROR    ERROR    BOOL   BOOL  BOOL   BOOL  BOOL  BOOL  FLOAT
    # flotante   flotante  FLOAT   FLOAT   FLOAT  FLOAT   ERROR    ERROR    BOOL   BOOL  BOOL   BOOL  BOOL  BOOL  FLOAT
    # flotante   cadena    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # flotante   caracter  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # flotante   bool      ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  

    # cadena     entero    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # cadena     flotante  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # cadena     cadena    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR BOOL  BOOL  CADENA 
    # cadena     caracter  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # cadena     bool      ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  

    # caracter   entero    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # caracter   flotante  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # caracter   cadena    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  
    # caracter   caracter  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR BOOL  BOOL  CHAR  
    # caracter   bool      ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR  

    # bool       entero    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR 
    # bool       flotante  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR 
    # bool       cadena    ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR 
    # bool       caracter  ERROR   ERROR   ERROR  ERROR   ERROR    ERROR    ERROR  ERROR ERROR  ERROR ERROR ERROR ERROR 
    # bool       bool      ERROR   ERROR   ERROR  ERROR   BOOL     BOOL     ERROR  ERROR ERROR  ERROR BOOL  BOOL  BOOL

    def __init__(self, booleanos=[], operadores=[]):
        """Inicializacion de propiedades de la clase"""
        self.booleanos = ("verdadero", "falso")
        self.operadores = ("-", "+", "*", "/", "&&", "||", ">", "<", ">=", "<=", "!=", "==", "=")
        global debug
        debug = False

    def verify_type_match(self, left, right, operator):
        """Verifica que los tipos sean compatibles y si lo son regresa el tipo 
        resultante de la operacion.
        Args:
            left: Operando izquierdo.
            right: Operando derecho.
            operator: Operador
        Regreso: 
            Valor resultante de la operacion."""
        
        # codigo para depurar
        global debug
        if debug :
            print('antes')
            print('l: ',  left)
            print('r: ',  right)
            print('op: ', operator)
        
        # se obtienen los codigos que representan a cada tipo
        l  = self.get_val(left)
        r  = self.get_val(right)
        op = self.get_val(operator)

        # codigo para depurar
        if debug :
            print('despues')
            print('l: ',  l)
            print('r: ',  r)
            print('op: ', op)

        # Se asigna un codigo a cada tipo
        ERROR, ENT, FLOAT, CADENA, CHAR, BOOL = 0, 1, 2, 3, 4, 5

        # Se inicializa el cubo semantico
        cube = (
            ((ENT, ENT, ENT, FLOAT, ERROR, ERROR, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL, ENT),
            (FLOAT, FLOAT, FLOAT, FLOAT, ERROR, ERROR, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL, ENT),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            ),
            ((FLOAT, FLOAT, FLOAT, FLOAT, ERROR, ERROR, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL, FLOAT),
            (FLOAT, FLOAT, FLOAT, FLOAT, ERROR, ERROR, BOOL, BOOL, BOOL, BOOL, BOOL, BOOL, FLOAT),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            ),
            ((ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, BOOL, BOOL, CADENA),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR)
            ),
            ((ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, BOOL, BOOL, CHAR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            ),
            ((ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR, ERROR),
            (ERROR, ERROR, ERROR, ERROR, BOOL, BOOL, ERROR, ERROR, ERROR, ERROR, BOOL, BOOL, BOOL),
            ),
            )

        # Se guarda el resultado producido por el cubo
        result = cube[l][r][op]

        # Dependiendo del reusltado se regresa una cadena con el tipo resultante
        # o un -1 en caso de error de tipos.
        if result is 0:
            return -1 
        elif result is 1:
            return "entero"
        elif result is 2:
            return "flotante"
        elif result is 3:
            return "cadena"
        elif result is 4:
            return "caracter"
        elif result is 5:
            return "bool"

    def get_val(self, val):
        """Obtiene el codigo correspondiente al tipo de dato 
        que corresponda el valor.
        Args:
            val: Valor para analizar.
        Regresa: Codigo correspondiente al tipo de dato."""
        global debug
        if val in self.operadores:
            return self.operadores.index(val)
        elif val == 'entero' :#or type(val) is int:
            if debug : print('entero')
            return 0
        elif val == "flotante" :#or type(val) is float:
            if debug : print('flotante')
            return 1
        elif val == "caracter" :#or type(val) is str and len(val) is 1 and val not in self.operadores:
            if debug : print('caracter')
            return 3
        elif val == "bool" :#or type(val) is str and val in self.booleanos:
            if debug : print('booleano')
            return 4
        elif val == "cadena" :#or type(val) is str and val not in self.operadores:
            if debug : print('cadena')
            return 2