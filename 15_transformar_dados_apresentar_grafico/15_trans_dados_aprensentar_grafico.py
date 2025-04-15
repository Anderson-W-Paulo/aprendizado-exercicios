import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Dados_Comerciais.xlsx')

#plt.bar() -> gráfico barra
# plt.pie() -> pizza
# plt.plot() -> linha


#Agrupando por segmento e somando com valores

plt.figure(figsize=(6, 5))
df_agrupados = df.groupby('Segmento')['ValorVenda'].sum() # tem que ser o somatório dos valores em venda
plt.title('Total Vendido por Segmento')
plt.pie(df_agrupados.values, labels=df_agrupados.index, autopct='%1.1f%%', startangle=1)
#valor, tamanho das fatias / define as etiquetas, divisão / valores percentuais(número com uma casa decimal) / rotaciona o gráfico, ( 1 graus)


#Agrupando Valor Total por Categoria

plt.figure(figsize=(7, 6))
df_agrupados_barra = df.groupby('Categoria')['ValorVenda'].sum()
plt.title('Total Vendido por Categoria')
plt.ylabel('Total Vendido')
plt.xlabel('Categoria')
plt.bar(df_agrupados_barra.index, df_agrupados_barra.values, width=0.8)
#posição das barras no eixo x / altura das barras / largura da barra

#Agrupando Valor Total por Fabricante
plt.figure(figsize=(7, 6))
df_agrupados_barra_deitada = df.groupby('Fabricante')['ValorVenda'].sum()
plt.title('Total vendidos por Fabricante')
plt.ylabel('Fabricantes')
plt.xlabel('Total Vendido')
plt.barh(df_agrupados_barra_deitada.index, df_agrupados_barra_deitada.values, height=0.5, color='green')

plt.show()
