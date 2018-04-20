# @author Matheus Alves dos Santos
# TITLE: Multiplos
# ID: 1044

a, b = map(int, raw_input().split())

if ((a % b) == 0) or ((b % a) == 0):
    print "Sao Multiplos"
else:
    print "Nao sao Multiplos"
