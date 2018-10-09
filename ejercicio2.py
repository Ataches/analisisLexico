import ply.lex as lex

tokens = ['NEWLINE', 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'ASIGN' ]

t_ignore = ' \t'
t_NEWLINE = r' \n'
t_PLUS = r'SUMA'
t_MINUS = r'RESTA'
t_TIMES = r'MULTIPLICACION'
t_DIVIDE = r'DIVISION'
t_ASIGN = r'ASIGNACION'
t_EQUALS = r':='
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

lex.input("MULTIPLICACION x = 3 - 4 + 5 * 6 SUMA ASIGNACION RESTA")

while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)

