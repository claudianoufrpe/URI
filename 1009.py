# @author Matheus Alves dos Santos
# TITLE: Salário com Bônus
# ID: 1009

# -*- coding: utf-8 -*-

name = raw_input()
salary = float(raw_input())
sales = float(raw_input())

receive = salary + sales * 0.15

print "TOTAL = R$ %.2f" % receive
