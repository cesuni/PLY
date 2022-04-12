import ply.lex as lex

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


# Regla de expresion regular
t_REVALUAR = r'Evaluar'
t_MAS    = r'\+'
t_MENOS   = r'-'
t_POR   = r'\*'
t_DIV  = r'/'
t_LCOR = r'\['
t_RCOR = r'\]'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LKEY = r'{'
t_RKEY = r'}'
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_ASIGN = r'='
t_PT = r'.'
t_PTCOMA = r';'

# Numeros decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal muy largo %d", t.value)
        t.value = 0
    return t

# Numeros enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero muy largo %d", t.value)
        t.value = 0
    return t  

# Cadena
def t_CADENA(t):
    r'\".*?"'
    t.value = t.value[1: -1]
    return t

# Palabras reservadas
def t_RESERV(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'RESERV')    
    return t             

# Ignorar un comentario
def t_ignore_COMMENT(t):
    r'\#.*'
    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore  = ' \t'

# Caracter Ilegal
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

  
# Build the lexer
lexer = lex.lex()

data = input("Ingrese: ")

# Give the lexer some input
lexer.input(data)

print(';;;;;Analizador Lexico;;;;;')

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)