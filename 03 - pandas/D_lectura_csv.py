# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:23:33 2019

@author: USRBET
"""

import pandas as pd
import os

#1) JSON CSV HTML XML
#2) Binary

path = "C://Users//USRBET//Documents//GitHub//py-o-a-hinostroza-carol-lizeth//03 - pandas//data//artwork_data.csv"

df1 = pd.read_csv(path,nrows=10)

columnas = ['id','artist', 'title','medium','year','acquisitionYear', 'height','width','units']

df2 = pd.read_csv(path,nrows=10,usecols=columnas)

df3 = pd.read_csv(path,nrows=10,usecols=columnas,index_col='id')


path_guardado = "C://Users//USRBET//Documents//GitHub//py-o-a-hinostroza-carol-lizeth//03 - pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_csv(path)

#hacer binario

path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-o-a-hinostroza-carol-lizeth//03 - pandas//data//artwork_data_completo.pickle"

df4.to_pickle(path_guardado_bin)

df5 = pd.read_pickle(path_guardado)