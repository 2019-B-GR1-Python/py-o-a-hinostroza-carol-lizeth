# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:07:15 2020

@author: User
"""

import pandas as pd
import numpy as np

path = "C://Users//User//Documents//GitHub//py-o-a-hinostroza-carol-lizeth//Proyecto Segundo Bimestre//movies_spider//movies.csv"
columnas = ['Titulo','Ranking','Duracion', 'Director','Recaudacion','Year']
moviesdf = pd.read_csv(path,encoding='latin-1',names=columnas)

recaudaciones_str = np.array(moviesdf['Recaudacion'].values)
