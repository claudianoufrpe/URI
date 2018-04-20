# @author Matheus Alves dos Santos
# TITLE: Gasto de Combustivel
# ID: 1010

piece1 = raw_input().split()
piece2 = raw_input().split()

total = (int(piece1[1]) * float(piece1[2])) + (int(piece2[1]) * float(piece2[2]))

print "VALOR A PAGAR: R$ %.2f" % total
