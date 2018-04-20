# @author Matheus Alves dos Santos
# TITLE: Salario com Bonus
# ID: 1009

name = raw_input()
salary = float(raw_input())
sales = float(raw_input())

receive = salary + sales * 0.15

print "TOTAL = R$ %.2f" % receive
