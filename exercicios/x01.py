import matplotlib.pyplot as plt

categorias = ['grupo A', 'grupo B', 'grupo C']
valores = [30, 45, 20]

plt.bar(categorias, valores)
plt.show()
plt.savefig('aula01.png')