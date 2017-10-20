# @author Matheus Alves dos Santos
# TITLE: Idade em Dias
# ID: 1020

# -*- coding: utf-8 -*-

dia = int(raw_input())

mes = 0
ano = 0

if dia >= 365:
    ano = (dia / 365)
    dia -= (ano * 365)
    
if dia >= 30:
    mes = (dia / 30)
    dia -= (mes * 30)

print '%d ano(s)\n%d mes(es)\n%d dia(s)' % (ano, mes, dia)
