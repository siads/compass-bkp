# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.


import pandas as pd

atores_df = pd.read_csv('dataset/actors.csv')

freq_filmes = atores_df['#1 Movie'].value_counts().head(1)

print(freq_filmes)

