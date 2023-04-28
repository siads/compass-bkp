#Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.



import pandas as pd

ator_df = pd.read_csv('dataset/actors.csv')

ator_filmes = (ator_df.loc[ator_df['Number of Movies'].idxmax()])

print(ator_filmes[['Actor', 'Number of Movies']])





