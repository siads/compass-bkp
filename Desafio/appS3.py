import boto3
import pandas as pd
from datetime import datetime

df_movies = pd.read_csv('dados/movies.csv', delimiter='|')
df_series = pd.read_csv('dados/series.csv', delimiter='|')

s3_client = boto3.client('s3')
dest_bucket = 'dw-desafio'
dest_prefix = 'Raw/Local/CSV'
especif_dado1 = 'Movies'
especif_dado2 = 'Series'
date = datetime.now().strftime('%Y/%m/%d')

s3_client.upload_file('dados/movies.csv', dest_bucket, f'{dest_prefix}/{especif_dado1}/{date}/movies.csv')

s3_client.upload_file('dados/series.csv', dest_bucket, f'{dest_prefix}/{especif_dado2}/{date}/series.csv')