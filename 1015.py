# @author Matheus Alves dos Santos
# TITLE: Distancia Entre Dois Pontos
# ID: 1015

import math

p1 = raw_input().split()
p2 = raw_input().split()

dist = math.sqrt((float(p1[0]) - float(p2[0]))**2 + (float(p1[1]) - float(p2[1]))**2)

print '%.4f' % dist

