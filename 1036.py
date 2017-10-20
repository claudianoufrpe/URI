# @author Matheus Alves dos Santos
# TITLE: Fórmula de Bhaskara
# ID: 1036

# -*- coding: utf-8 -*-

import math

valores = raw_input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = b**2 - (4*a*c)

if (delta < 0 or a == 0):
    print 'Impossivel calcular'
else:
    r1 = (-b + math.sqrt(delta))/ (2 * a)
    r2 = (-b - math.sqrt(delta))/ (2 * a)
    print 'R1 = %.5f' % r1
    print 'R2 = %.5f' % r2
