# @author Matheus Alves dos Santos
# TITLE: Conversao de Tempo
# ID: 1019

segundo = int(raw_input())

hora = 0
minuto = 0

if segundo >= 60:
    minuto = (segundo / 60)
    segundo -= (minuto * 60)
    
    if minuto >= 60:
        hora = (minuto / 60)
        minuto -= (hora * 60)

print '%d:%d:%d' % (hora, minuto, segundo)
