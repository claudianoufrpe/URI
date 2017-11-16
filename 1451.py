# @author Matheus Alves dos Santos
# TITLE: Teclado Quebrado
# ID: 1451

# -*- coding: utf-8 -*-

while (True):
    try:
        beiju = aux = ''
        home_pressed = False
        text = raw_input()
        
        for char in text:
            if char == '[':
                home_pressed = True
                beiju = aux + beiju
                aux = ''
            elif char == ']':
                home_pressed = False
                beiju = aux + beiju
                aux = ''
            else:
                if home_pressed:
                    aux += char
                else:
                    beiju += char
        
        beiju = aux + beiju
        
        print beiju
        
    except:
        break
