#!/home/studentb08/.local/share/virtualenvs/sprawozdanie-5D_5EEiY/bin/python
import os
import pandas as pd
import numpy as np
os.remove('zad2a.csv')

mu=4
sigma=2
zbior_danych = np.random.normal(mu, sigma, 100)
print(zbior_danych)

DF = pd.DataFrame(zbior_danych, columns=["Wartosc"])
DF.to_csv("zad2a.csv", index=False)