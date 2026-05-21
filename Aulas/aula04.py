import pandas as pd

# Criação do DataFrame
df = pd.DataFrame({
    "idade": [20, 22, 20, 23, 24]
})

# Descreve dados estatísticos do dataframe
print(df['idade'].describe())

# Média
print('Média: ' + str(df['idade'].mean()))

# Mediana
print('Mediana: ' + str(df['idade'].median()))

# Moda
print('Moda: ' + str(df['idade'].mode().iloc[0]))
