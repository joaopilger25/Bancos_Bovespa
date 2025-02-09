import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#tickers dos bancos Itaú, Bradesco, Banco do Brasil, Santander e BTG Pactual
tickers = ['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA', 'SANB11.SA', 'BPAC11.SA']

#Dataframe para preencher
df = pd.DataFrame()

#Puxar os dados do Yahoo Finance e guardar o preço de fechamento das ações no Dataframe
for ticker in tickers:
    dados = yf.download(ticker, period="6mo")
    df[ticker] = dados["Close"]

#Construir o gráfico
plt.figure(figsize=(12, 6))

#incluir a informação de dentro do Dataframe de cada index no gráfico
for banco in df.columns:
    plt.plot(df.index, df[banco], label=banco)

#Personalização do gráfico
plt.xlabel("Data")
plt.ylabel("Preço de Fechamento (R$)")
plt.title("Evolução dos Preços de Fechamento dos Bancos no Último Semestre")
plt.legend(['Itaú', 'Bradesco', 'Banco do Brasil', 'Santander', 'BTG Pactual'])
plt.grid(True)
plt.xticks(rotation=45)

#Mostrar o Gráfico
plt.show()
