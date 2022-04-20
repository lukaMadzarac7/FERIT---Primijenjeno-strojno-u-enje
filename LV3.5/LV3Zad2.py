import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')

#mtcars.groupby('cyl')['mpg'].mean().plot.bar() #prikaz potrošnje automobila s 3 razl. cilindra
#plt.show()

#mtcars.boxplot(by='cyl', column='wt') #distribucija težine automobila s 4, 6 i 8 cilindara
#plt.show()

#mtcars.groupby('am')['mpg'].mean().plot.bar() #prikaz potrošnje automobila s 2 vrste mjenjaca
#plt.show()





