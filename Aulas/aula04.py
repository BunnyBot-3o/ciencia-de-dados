import pandas as pd

# Criação do DataFrame
df = pd.DataFrame({
    #Cria uma coluna com definição de valores
    "idade": [20, 22, 20, 23, 24]
})

#Descreve dados estatíisticos do dataframe
print(df['idade'].describe())

print('Media:' + str(df]['idade'].mean()))
print('mediana:' + str(df['idade'].median))
print('moda:' + str(df['idade'].mode().iloc[0]))