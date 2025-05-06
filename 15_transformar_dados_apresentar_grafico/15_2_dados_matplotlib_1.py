import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Dados_Comerciais.xlsx')

#Criar subplots 3
fig, axes = plt.subplots(2, 2, figsize=(15, 7))

#Valor Total x Segmento
df_agrupado_pizza = df.groupby('Segmento')['ValorVenda'].sum()
axes[0, 0].set_title('Total  Venda x Segmento')
axes[0, 0].pie(df_agrupado_pizza.values, labels=df_agrupado_pizza.index, autopct='%1.1f%%')

#Valor Total x Categoria
df_agrupado_barra = df.groupby('Categoria')['ValorVenda'].sum()
axes[0, 1].set_title('Total Venda x Categoria')
axes[0, 1].bar(df_agrupado_barra.index, df_agrupado_barra.values, width=0.5)

#Valor Total x Fábrica
df_agrupados_barra_vertical = df.groupby('Fabricante')['ValorVenda'].sum()
axes[1, 0].set_title('Fábricas x Total Venda')
axes[1, 0].barh(df_agrupados_barra_vertical.index, df_agrupados_barra_vertical.values, height=0.6, color='green')

#Valor venda ao longo do tempo
df['Data'] = pd.to_datetime(df['Data Venda'])
df['Ano'] = df['Data'].dt.year
df_agrupado_linha = df.groupby('Data')['ValorVenda'].mean()
df_agrupado_reta = df.groupby('Ano')['ValorVenda'].mean()
axes[1, 1].set_title('Total Venda x Ano')
axes[1, 1].plot(df_agrupado_linha.index, df_agrupado_linha.values)
axes[1, 1].legend()

plt.show()
