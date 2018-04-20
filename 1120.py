# @author Matheus Alves dos Santos
# TITLE: Revisao de Contrato
# ID: 1120

while True:
    number, answer = raw_input().split()
    if ((number == "0") and (answer == "0")):
        break
    
    answer = list(answer.replace(number, ""))
    for i in range(len(answer)):
        if (answer[i] == "0"):
            answer[i] = ""
        else:
            break
    
    answer = "".join(answer)    
        
    if (answer != ""):
        print answer
    else:
        print 0
