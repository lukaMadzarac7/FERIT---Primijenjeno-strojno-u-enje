import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
#print(df.info())

print(df.sort_values(by=['selling_price']).head(3)) #3 najjeftinijih autobobila
print(df.sort_values(by=['selling_price']).tail(3)) #3 najskupljih automobila
print(sum(df['year']==2012)) #auti proizvedeni 2015.
print(df.sort_values(by=['km_driven']).tail(1)) #najmanje prijedeno kilometara
print(df.sort_values(by=['km_driven']).head(1)) #najvise prijedenih kilometara
