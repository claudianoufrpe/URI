# @author Matheus Alves dos Santos
# TITLE: Lanche
# ID: 1038

entrada = raw_input().split()
quantidade = int(entrada[1])

if entrada[0] == '1':
    total = quantidade * 4.0
elif entrada[0] == '2':
    total = quantidade * 4.5
elif entrada[0] == '3':
    total = quantidade * 5.0
elif entrada[0] == '4':
    total = quantidade * 2.0
else:
    total = quantidade * 1.5
    
print 'Total: R$ %.2f' % total
