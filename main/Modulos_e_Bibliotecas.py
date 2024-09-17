# como utilizar modulos
# primeiro modo
import math

math.sqrt(25)
math.log2(1024)
math.cos(45)
print(math.sqrt(25))

#sugundo modo
import math as m

m.sqrt(25)
m.log2(1024)
m.cos(45)

#terceiro modo
from math import sqrt, log2, cos
sqrt(25)
log2(1024)
cos(45)


import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [4,3,5,1,2]

plt.bar(x,y)
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')
plt.title('Exemplo de grafico')

plt.show()

#ATIVIDADE PRÁTICA;
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

plt.bar(meses, vendas, color='blue')
plt.title ("Vendas mensais")
plt.show()