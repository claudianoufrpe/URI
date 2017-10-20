# @author Matheus Alves dos Santos
# TITLE: Sub-prime
# ID: 1105

# -*- coding: utf-8 -*-

while (True):
    size = map(int, raw_input().split())
    result = 'S'
    if size == [0, 0]:
        break
        
    cash = map(int, raw_input().split())
    
    for i in range(size[1]):
        deb = map(int, raw_input().split())
        cash[deb[0] - 1] -= deb[2]
        cash[deb[1] - 1] += deb[2]
        
    for i in cash:
        if i < 0:
            result = 'N'
            break
            
    print result
