# @author Matheus Alves dos Santos
# TITLE: Conversão de Tempo
# ID: 1019

# -*- coding: utf-8 -*-

segundo = int(raw_input())

hora = 0
minuto = 0

if segundo >= 60:
    minuto = (segundo / 60)
    segundo -= (minuto * 60)
    
    if minuto >= 60:
        hora = (minuto / 60)
        minuto -= (hora * 60)

print '%d:%d:%d' % (hora, minuto, segundo)
