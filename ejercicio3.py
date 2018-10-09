import ply.lex as lex

tokens = ['NEWLINE','NOAN','NOAS','NOAE','NOAO','OAN','OAS','OAE','OAO','JZUMB','JNZUMB','AZMOCHILA','NZMOCHILA','FLIBRE','FBLOQ','IZQLIBRE','IZQBLOQ','DERLIBRE','DERBLOQ','NO','O','Y','MIENTRAS','HACER','REPETIR','VECES','SI','ENTONCES','SINO','PUNTOYCOMA','APAGAR','INICIARPROGRAMA', 'INICIAREJECUCION', 'TERMINAEJECUCION', 'FINALIZARPROGRAMA', 'GIRAIZQ','AVANZA','COGEZUMBADOR','DEJAZUMBADOR','SALDEINSTRUCCION', 'INICIO', 'FIN' ]

t_ignore = ' \t'
t_NEWLINE = r' \n'
t_PUNTOYCOMA = r';'
t_APAGAR = r'apagate'
t_INICIARPROGRAMA = r'iniciar-programa' 
t_INICIAREJECUCION = r'inicia-ejecucion'
t_TERMINAEJECUCION = r'termina-ejecucion'
t_FINALIZARPROGRAMA = r'finalizar-programa'
t_GIRAIZQ = r'gira-izquierda'
t_AVANZA = r'avanza'
t_COGEZUMBADOR = r'coge-zumbador'
t_DEJAZUMBADOR = r'deja-zumbador'
t_SALDEINSTRUCCION = r'sal-de-instruccion'
t_INICIO = r'inicio'
t_MIENTRAS = r'mientras'
t_HACER = r'hacer'
t_REPETIR = r'repetir'
t_VECES = r'veces'
t_NO = r'no'
t_O = r'o'
t_Y = r'y'
t_SI = r'si'
t_ENTONCES = r'entonces'
t_SINO = r'sino'
t_FLIBRE = r'frente-libre'
t_FBLOQ = r'frente-bloqueado'
t_IZQLIBRE = r'izquierda-libre'
t_IZQBLOQ = r'izquierda-bloqueado'
t_DERLIBRE = r'derecha-libre'
t_DERBLOQ = r'derecha-bloqueado'
t_JZUMB = r'junto-a-zumbador'
t_JNZUMB = r'no-junto-a-zumbador'
t_AZMOCHILA = r'algun-zumbador-en-la mochila'
t_NZMOCHILA = r'ningun-zumbador-en-la mochila'
t_OAN = r'orientado-al-norte'
t_OAS = r'orientado-al-sur'
t_OAE = r'orientado-al-este'
t_OAO = r'orientado-al-oeste'
t_NOAN = r'no-orientado-al-norte'
t_NOAS = r'no-orientado-al-sur'
t_NOAE = r'no-orientado-al-este'
t_NOAO = r'no-orientado-al-oeste'
t_FIN = r'fin'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

archivoEntrada = open("E:\expresiones.in", "r")
lineasArchivo = archivoEntrada.readlines()

for lineas in lineasArchivo:
    lex.input(lineas)

    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
