# @author Matheus Alves dos Santos
# TITLE: Gasto de Combustivel
# ID: 1017

tempo = int(raw_input())
velocidade = int(raw_input())

combustivel = (tempo * velocidade) / 12.

print '%.3f' % combustivel
