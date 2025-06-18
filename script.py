# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def filtrar_impares(lista):
    return [numero for numero in lista if numero % 2 != 0]

numeros = [1, 2, 3, 4, 5, 6, 7]
resultado = filtrar_impares(numeros)
print(resultado)


# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_na_lista(lista):
    return [num for num in lista if eh_primo(num)]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = primos_na_lista(numeros)
print(resultado)  


# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def exclusivos(lista1, lista2):
    return list(set(lista1).symmetric_difference(set(lista2)))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(exclusivos(a, b)) 


# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista. 

def segundo_maior(lista):
    lista_unica = list(set(lista))  # Remove duplicatas
    if len(lista_unica) < 2:
        return None  # Não há segundo maior
    lista_ordenada = sorted(lista_unica, reverse=True)
    return lista_ordenada[1]

numeros = [10, 5, 20, 8, 20, 5]
print(segundo_maior(numeros))


# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista_de_pessoas):
    return sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])

pessoas = [("Carlos", 30), ("Ana", 25), ("Beatriz", 22), ("Daniel", 28)]
resultado = ordenar_por_nome(pessoas)
print(resultado)
# Saída: [('Ana', 25), ('Beatriz', 22), ('Carlos', 30), ('Daniel', 28)]


# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

""" Outliers são valores extremos que se destacam dos demais dados. Podem ser detectados com desvio padrão (valores além de 3 desvios da média) ou com quartis (valores fora do intervalo) """

import pandas as pd

def remover_outliers_std(df, coluna):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    limite_inferior = media - 3 * desvio
    limite_superior = media + 3 * desvio
    return df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]

def remover_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]


# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

""" Usa-se pd.concat() com axis=0 para empilhar linhas ou axis=1 para juntar colunas. Se as colunas não coincidirem, pandas preenche os campos ausentes com NaN. """

import pandas as pd

df1 = pd.DataFrame({'nome': ['Ana', 'Bruno'], 'idade': [25, 30]})
df2 = pd.DataFrame({'nome': ['Carlos'], 'idade': [28], 'cidade': ['SP']})

df_linhas = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_linhas)


# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas? 

""" Utiliza-se pd.read_csv('arquivo.csv') para carregar o arquivo em um DataFrame. Em seguida, df.head() exibe as primeiras linhas, facilitando a inspeção inicial. """

import pandas as pd

df = pd.read_csv('caminho/do/arquivo.csv')
print(df.head())


# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição? 

""" Para acessar uma coluna: df['coluna']. Para filtrar linhas: df[condição], como df[df['idade'] > 30]. Combinações são feitas com operadores lógicos e parênteses. """

df[df['idade'] > 30]


# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame? 

""" Pode-se identificar com isna() ou isnull(). Para tratar: usa-se dropna() para remover ou fillna() para preencher com valores fixos ou estatísticas como média ou mediana. """

df.isna()  # Mostra True onde há NaN
df.isnull().sum()  # Conta quantos NaN existem por coluna
df_sem_na = df.dropna()  # Remover linhas com qualquer NaN
df_sem_colunas_na = df.dropna(axis=1)  # Remover colunas com NaN
df_preenchido = df.fillna(0)  # Ou outro valor, como 'desconhecido'
