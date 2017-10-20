# @author Matheus Alves dos Santos
# TITLE: Leitura Ótica
# ID: 1129

# -*- coding: utf-8 -*-

answer = ['A', 'B', 'C', 'D', 'E']

while (True):
    size = int(raw_input())
    
    if size == 0:
        break
        
    for i in range(size):
        question = raw_input().split()
        chosen = []
        
        for j in range(len(question)):
            if int(question[j]) <= 127:
                chosen.append(j)
        
        if len(chosen) == 1:
            print answer[chosen[0]]
        else:
            print '*'
