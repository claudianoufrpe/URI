# @author Matheus Alves dos Santos
# TITLE: Notas e Moedas
# ID: 1021

dinheiro = int(float(raw_input()) * 100)

valores = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
resultado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(valores)):
    if dinheiro >= valores[i]:
        resultado[i] = dinheiro / valores[i]
        dinheiro -= resultado[i] * valores[i]

print 'NOTAS:'

for i in range(0, 6):
    print '%d nota(s) de R$ %.2f' % (resultado[i], float(valores[i])/100)

print 'MOEDAS:'

for i in range(6, 12):
    print '%d moeda(s) de R$ %.2f' % (resultado[i], float(valores[i])/100)
