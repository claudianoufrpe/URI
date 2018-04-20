# @author Matheus Alves dos Santos
# TITLE: Horas e Minutos
# ID: 1300

while True:
    try:
        angle = int(raw_input())
        if ((angle % 6) == 0):
            print "Y"
        else:
            print "N"
    except:
        break
