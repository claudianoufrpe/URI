# @author Matheus Alves dos Santos
# TITLE: Alarme Despertador
# ID: 1103

while (True):
    entrada = raw_input().split()
    
    if entrada == ['0', '0', '0', '0']:
        break
    
    if entrada[0] == '0':
        inicio = 1440 + int(entrada[1])
    else:
        inicio = (int(entrada[0])*60) + int(entrada[1])
        
    if entrada[2] == '0':
        fim = 1440 + int(entrada[3])
    else:
        fim = (int(entrada[2])*60) + int(entrada[3])
        
    minutos = fim - inicio
    
    if minutos < 0:
        print (minutos + 1440)
    else:
        print minutos
