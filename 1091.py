# @author Matheus Alves dos Santos
# TITLE: Divisão da Nlogônia
# ID: 1091

# -*- coding: utf-8 -*-

while (True):
    query = int(raw_input())
    
    if query == 0:
        break
        
    border = raw_input().split()
        
    for i in range(query):
        position = raw_input().split()
        
        if (border[0] == position[0]) or (border[1] == position[1]):
            print 'divisa'
            
        elif (int(position[0]) > int(border[0])):
            if (int(position[1]) > int(border[1])):
                print 'NE'
            else:
                print 'SE'
                
        else:
            if (int(position[1]) > int(border[1])):
                print 'NO'
            else:
                print 'SO'
