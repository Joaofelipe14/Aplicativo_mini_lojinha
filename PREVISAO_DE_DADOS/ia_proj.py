#IMPORTANDO BLIBLIOCETAS PADROES 
import numpy as np
import pandas as pd


#IMPORTANDO BLIBLIOTECAS PARA GERAÇÃO DO GRAFICO
import matplotlib.pyplot as plt


#IMPORTANDO BLIBLIOTECAS PARA O APRENDIZADO DE MAQUINA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor


#LENDO O ARQUIVO EM EXCEL
df = pd.read_excel(r'C:\Users\jaofe\AppData\Local\Programs\Python\Python39\Ia_p3\Real_Estate_Valuation.xlsx',sheet_name = 'data', index_col = 'No')
# print(df) 

df.rename(
    columns={
        "X1 transaction date": "Data_transacao", 
        "X2 house age": "idade_casa", 
        "X3 distance to the nearest MRT station": "distancia",
        "X4 number of convenience stores": "Numero_loja",
        "X5 latitude": "Latitude",
        "X6 longitude": "Longitude",
        "Y house price of unit area": "preco_area",
    },
    inplace = True
)

print(df) 

##print(df.describe())

# plt.scatter(x=df['distancia'], y=df['preco_area'])
# plt.xlabel('Distancia em metros')
# plt.ylabel('Preço por unidade de área"')
# plt.title('Real Estate Valuation')
# plt.show()


X = np.array(df['distancia']).reshape(-1,1)
Y = np.array(df['preco_area']).reshape(-1,1)

#NORMALIZAÇÃO  DO DADOS 
escala = StandardScaler() 
escala.fit(X)

X_norm = escala.transform(X)

#Dividir  em conjunto de treinamento e teste 
X_norm_train, X_norm_test, Y_train, Y_test = train_test_split(X_norm, Y,  test_size=0.5, random_state=1)

# TREINANDO PARA RADON FLOREST
forest = RandomForestRegressor(200)
print(forest.fit(X_norm_train,Y_train))


# TREINANDO PARA REGRESSÃO LINEAR
reglinear = SGDRegressor(max_iter=2000,
                          tol = 0.0000001,
                         eta0= 0.1,
                         learning_rate="constant",
                         verbose=2
                        )

print(reglinear.fit(X_norm_train, Y_train))

#Previssão do conjunto de teste
pd_previsao = forest.predict(X_norm_test) # PREVISAO PRA O RADOM FLOREST
Y_rl_previsao = reglinear.predict(X_norm_test)  # PREVISAO PRA O REGRESSÃO LINAR 

# CALCULO DO R QUADRADO
r2_rna = r2_score(Y_test,pd_previsao)
r2_rl = r2_score(Y_test,Y_rl_previsao)

print("R2 RANDOM FLOREST:", r2_rna)
print("R2 RL:", r2_rl)

#GRAFICO  QUE MOSTRA A PREVISÃO DO REAL EM RELAÇÃO QUE VAI SER PRESVITO PELO ALGORITMO
# X_test = escala.inverse_transform(X_norm_test)
# plt.scatter(X_test, Y_test, alpha = 0.5, label="Reais")
# plt.scatter(X_test, pd_previsao, alpha = 0.5, label="Florest")
# plt.scatter(X_test, Y_rl_previsao, alpha = 0.5, label="Reg linear")
# plt.xlabel("Distancia em metros")
# plt.ylabel("Preço por unidade de área")
# plt.title ("Comparação dos algoritmos previsto")
# plt.legend(loc=1)
# plt.show()

# PREVER UM NOVO DADO PARA A COMPRAÇÃO 
X_futuro= np.array([[205]])  # ALTERA O VALOR DA VARIEL
X_futuro_norm = escala.transform(X_futuro.T)

y_forest = forest.predict(X_futuro_norm)
y_reglinear_prev_futuro = reglinear.predict(X_futuro_norm)

# Preço de area previsto...
print("  Preço de area previsto FOREST: ",y_forest)
print("  Preço de area previsto Reg Linear: ",y_reglinear_prev_futuro)
