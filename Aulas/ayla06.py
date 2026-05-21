import matplotlib.pyplot as plt
import pandas as pd

# Análise qualitativa

frutas = [
    "maça", "banana", "maça",
    "laranja", "banana", "banana",
    "maça", "uva", "laranja"
]

serie = pd.series (frutas)
frequencia = serie.value_counts()

print(frequencia)

#criando grafico de b
frequencia.plot(kind="bar")

plt.title("frutas prefereidas dos alunos")
plt.xlabel("frutas")
plt.ylabel("frequencia")

plt.show()
plt.savefig("aula06-qualitativo")