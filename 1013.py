# @author Matheus Alves dos Santos
# TITLE: O Maior
# ID: 1013

# -*- coding: utf-8 -*-

value = raw_input().split()

a = int(value[0])
b = int(value[1])
c = int(value[2])

maior = (a + b + abs(a - b)) / 2
maior = (maior + c + abs(maior - c)) / 2

print '%.d eh o maior' % maior
