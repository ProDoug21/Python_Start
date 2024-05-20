import pandas as pd

# 1 - Importando Dados
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

# 2 Listando os primeiros registros
print(data.head())

# 3 Lista dos Últimos Registros
print(data.tail())

# 4 Contagem de Valores por fabricantes
print(data["Fabricante"].value_counts())