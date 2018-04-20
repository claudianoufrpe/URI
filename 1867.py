# @author Matheus Alves dos Santos
# TITLE: Maior Número de Um Algarismo
# ID: 1867

while (True):
    numbers = raw_input()

    if (numbers != "0 0"):
        number1 = numbers.split(" ")[0]
        number2 = numbers.split(" ")[1]

        while (True):
            sum_n1 = 0
            
            for n in number1:
                sum_n1 += int(n)
            
            number1 = str(sum_n1)
            if sum_n1 <= 9:
                break

        while (True):
            sum_n2 = 0
            
            for n in number2:
                sum_n2 += int(n)
            number2 = str(sum_n2)
            
            if sum_n2 <= 9:
                break
                
        if sum_n1 > sum_n2:
            print "1"
        elif sum_n2 > sum_n1:
            print "2"
        else:
            print "0"

    else:
        break
