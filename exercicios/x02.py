import matplotlib.pyplot as plt

#1) Construa um gráfico de barras que compare a nota de popularidade de séries em 2025:

categorias = ['Stranger Things', 'It', 'Game of Thrones', 'Friends']
valores = [5, 4.5, 4.3, 4.1]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercicios/x01.png')

#2) Construa um gráfico de barras que compare os celulares mais vendidos em 2026:
plt.clf()

categorias2 = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valores2 = [ 200.000, 320.000, 500.000]

plt.bar(categorias2, valores2)
plt.show()
plt.savefig('./exercicios/x02.png')