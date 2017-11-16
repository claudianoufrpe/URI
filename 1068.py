# -*- coding: utf-8 -*-

# @author Matheus Alves dos Santos
# TITLE: Balanço de Parênteses I
# ID: 1068

while (True):
    try:
        balance = 0
        correct = True;
        expression = raw_input()
        
        for i in expression:
            if (i == "("):
                balance += 1;
            elif (i == ")"):
                balance -= 1;
            if balance < 0:
                break
        
        if (balance != 0):
            correct = False
        
        if (correct):
            print "correct"
        else:
            print "incorrect"
                
    except:
        break
