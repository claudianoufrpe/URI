# @author Matheus Alves dos Santos
# TITLE: Dama
# ID: 1087

while True:
    entrada = raw_input().split()
    
    if entrada == ['0', '0', '0', '0']:
        break
        
    x_move = abs(int(entrada[0]) - int(entrada[2]))
    y_move = abs(int(entrada[1]) - int(entrada[3]))
        
    if x_move == y_move == 0:
        move = 0
    elif (x_move == 0) or (y_move == 0) or (x_move == y_move):
        move = 1
    else:
        move = 2
        
    print move
