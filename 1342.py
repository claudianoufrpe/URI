# @author Matheus Alves dos Santos
# TITLE: Dado
# ID: 1342

while (True):
    info = map(int, raw_input().split())
    
    if info == [0, 0]:
        break
        
    position = []
    status = []
    player = 0
    
    trap = map(int, raw_input().split())
    rows = int(raw_input())
    
    for i in range(info[0]):
        status.append(0)
        position.append(0)
        
    for i in range(rows):
        dices = map(int, raw_input().split())
        
        while status[player] == 1:
            status[player] = 0
            player += 1
            if player == len(position):
                player = 0
                
        position[player] += (dices[0] + dices[1])
        if position[player] == trap[0] or position[player] == trap[1] or position[player] == trap[2]:
                status[player] = 1
                
        player += 1
        if player == len(position):
            player = 0
            
    for i in range(len(position)):
        if position[i] > info[1]:
            print i + 1
            break
