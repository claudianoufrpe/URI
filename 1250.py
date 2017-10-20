# @author Matheus Alves dos Santos
# TITLE: KiloMan
# ID: 1250

# -*- coding: utf-8 -*-

number = int(raw_input())

for i in range(number):
    hits = 0
    n_shots = int(raw_input())
    pos_shots = raw_input().split()
    pos_player = list(raw_input())
    
    for j in range(n_shots):
        if pos_player[j] == 'S':
            if int(pos_shots[j]) <= 2:
                hits += 1
        else:
            if int(pos_shots[j]) > 2:
                hits += 1
    print hits
