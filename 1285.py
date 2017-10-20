# @author Matheus Alves dos Santos
# TITLE: Dígitos Diferentes
# ID: 1285

# -*- coding: utf-8 -*-

while (True):
    try:
        limites = map(int, raw_input().split())
        valores = range(limites[0], limites[1] + 1)
        aceitos = len(valores)
        
        for i in valores:
            if len(str(i)) > len(set(str(i))):
                aceitos-=1
        print aceitos
    
    except:
        break
