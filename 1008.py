# @author Matheus Alves dos Santos
# TITLE: Salário
# ID: 1008

# -*- coding: utf-8 -*-

number = int(raw_input())
hours = int(raw_input())
perhour = float(raw_input())

salary = hours * perhour

print "NUMBER = %d\nSALARY = U$ %.2f" %(number, salary)
