# @author Matheus Alves dos Santos
# TITLE: Loop Musical
# ID: 1089

while (True):
    peak = 0
    size = int(raw_input())
    if size == 0:
        break
        
    values = map(int, raw_input().split())
    
    for i in range(1, size - 1):
        if values[i] > values[i+1]:
            if values[i] > values[i-1]:
                peak +=1
        elif values[i] < values[i+1]:
            if values[i] < values[i-1]:
                peak +=1
                
    if values[0] > values[1]:
        if values[0] > values[size-1]:
            peak += 1
    elif values[0] < values[1]:
        if values[0] < values[size-1]:
            peak += 1
            
    if values[size-1] > values[0]:
        if values[size-1] > values[size-2]:
            peak += 1
    elif values[size-1] < values[0]:
        if values[size-1] < values[size-2]:
            peak += 1
            
    print peak
