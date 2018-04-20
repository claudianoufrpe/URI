# @author Matheus Alves dos Santos
# TITLE: Cedulas
# ID: 1018

dinheiro = int(raw_input())
print dinheiro

valores = [100, 50, 20, 10, 5, 2, 1]
resultado = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(valores)):
    if dinheiro >= valores[i]:
        resultado[i] = dinheiro / valores[i]
        dinheiro -= resultado[i] * valores[i]

for i in range(len(valores)):
    print '%d nota(s) de R$ %d,00' % (resultado[i], valores[i])
