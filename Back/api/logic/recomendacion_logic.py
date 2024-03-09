import pandas as pd
import uuid
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


df_matriz_item_item=pd.read_csv("item_item.csv")
item_similarities = cosine_similarity(df_matriz_item_item)
item_similarities
cosine_df=pd.DataFrame(item_similarities,index=df_matriz_item_item.index,columns=df_matriz_item_item.index)
def consultar_recomendacion_coseno(nombrepelicula):
 pelicula=cosine_df.loc[nombrepelicula]
 return pelicula.sort_values(ascending=False).head(10)
