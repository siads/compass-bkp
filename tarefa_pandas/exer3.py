# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

atores_df = pd.read_csv('dataset/actors.csv')

media_filme = atores_df.loc[atores_df['Average per Movie'].idxmax()]

ator_media_filme = media_filme['Actor']

max_media_filme = media_filme['Average per Movie']

print(ator_media_filme, max_media_filme)

