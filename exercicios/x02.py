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

#3) Identifique na turma qual é o time de cada um e construa um gráfico de barras para mostrar a popularidade cada time.
plt.clf()

categorias3 = ['Vasco', 'grêmio', 'flamengo', 'internacional', 'palmeiras']
valores3 = [1, 3, 2, 2, 1]
cores = ["#030303", "#00B7FF", '#C52613', '#E5050F', '#006437']

plt.bar(categorias3, valores3, color=cores)
plt.xlabel('Timwa so campeonato')
plt.ylabel('N* de torcedores')
plt.show()
plt.savefig('./exercicios/x03.png')