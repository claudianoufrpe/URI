# @author Matheus Alves dos Santos
# TITLE: Balanco de Parenteses I
# ID: 1068

while (True):
    try:
        balance = 0
        correct = True;
        expression = raw_input()
        
        for i in expression:
            if (i == "("):
                balance += 1;
            elif (i == ")"):
                balance -= 1;
            if balance < 0:
                break
        
        if (balance != 0):
            correct = False
        
        if (correct):
            print "correct"
        else:
            print "incorrect"
                
    except:
        break
