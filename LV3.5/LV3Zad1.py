import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
#print(len(mtcars))

print(mtcars.sort_values(by=['mpg'], ascending=True).head(5)['car']) #najveca potrosnja
print(mtcars[mtcars.cyl==8].sort_values(by=['mpg'], ascending=False).tail(3)['car']) #najveca potrosnja 3 automobila s 8 cilindara
print(mtcars[mtcars.cyl==6].mpg.mean()) #srednja potrosnja automobila sa 6 cilindara
print(mtcars[(mtcars.cyl==4)&(mtcars.wt>2.0)&(mtcars.wt<2.2)].mpg.mean()) #srednja potrosnja automobila sa 6 cilindara
print(mtcars.groupby('am').count().car[0]) #koliko ih ima s automatskim mjenjacem
print(mtcars.groupby('am').count().car[1]) #koliko ih ima s rucnim mjenjacem
print(len(mtcars[mtcars.am=='1'] & mtcars[mtcars.hp>100])) #koliko ih ima s automatskim mjenjacem i konjskom snagom vecom od 100
mtcars['bg'] = mtcars['wt']*1000*0.453 #novi stupac sa svim masama automobila
print(mtcars) #printanje mtcars s novim stupcem


