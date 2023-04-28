#Apresente a média da coluna contendo o número de filmes.


import pandas as pd

ator_df = pd.read_csv('dataset/actors.csv')

media_filmes = ator_df['Number of Movies'].mean()

print(media_filmes)