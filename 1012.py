# @author Matheus Alves dos Santos
# TITLE: Area
# ID: 1012

value = raw_input().split()

a = float(value[0])
b = float(value[1])
c = float(value[2])

tri = (a * c) / 2
cir = 3.14159 * c**2
tra = ((a + b) * c) / 2
qua = b**2
ret = a * b

print 'TRIANGULO: %.3f' % tri
print 'CIRCULO: %.3f' % cir
print 'TRAPEZIO: %.3f' % tra
print 'QUADRADO: %.3f' % qua
print 'RETANGULO: %.3f' % ret
