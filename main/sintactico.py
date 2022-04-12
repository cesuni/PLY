import ply.yacc as yacc
from lexico import *

# Palabras reservadas (RESERV)
reserved = {
    'if'        : 'IF',         # If
    'then'      : 'THEN',       # Then
    'else'      : 'ELSE',       # Else
    'while'     : 'WHILE',      # While
    'include'   : 'INCLUDE',    # Include
    'namespace' : 'NAMESPACE',  # Namespace
    'std'       : 'STD',        # Std
    'main'      : 'MAIN',       # Main
    'cout'      : 'COUT',       # Cout
    'print'     : 'PRINT',      # Print
    'cin'       : 'CIN',        # Cin
    'get'       : 'GET',        # Get
    'post'      : 'POST',       # Post
    'update'    : 'UPDATE',     # Update
    'delete'    : 'DELETE',     # Delete
}

# Lista de tokens
tokens = [
   'REVALUAR', 
   'ENTERO',            # 235
   'DECIMAL',           # 3.44
   'CADENA',            # "cadena"
   'MAS',
   'MENOS',
   'POR',
   'DIV',
   'LCOR',
   'RCOR',
   'LPAREN',
   'RPAREN',
   'LKEY',
   'RKEY',
   'MENORQ',
   'MAYORQ',
   'ASIGN',
   'PT',
   'PTCOMA',
   'RESERV',            # reserved
] + list(reserved.values())

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIV'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LCOR', 'RCOR'),
    ('right','UMENOS'),
)

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''

def p_instrucciones_evaluar(t):
    'instruccion : REVALUAR LCOR expresion RCOR PTCOMA'
    print('El valor de la expresión es: ' + str(t[3]))

def p_expresion_operators(t):
    '''expresion :  expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIV expresion'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : LPAREN expresion RPAREN'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

print(';;;;;Analizador sintactico')

parser.parse(data)
print(input)