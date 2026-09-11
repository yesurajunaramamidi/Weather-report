
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pf = pd.read_csv('weather.csv')
print(pf.shape)
print(pf.columns)
print(pf.isnull().sum())
print(pf.describe())
x=pf['weather']
y=pf['temp_max']
plt.bar(x,y,color='red')
plt.savefig('weather_report.pdf')
plt.show()
pf['target']=pf.shift(-1)['temp_max']
print(pf)
pf=pf.ffill()
print(pf)
x=pf['target']
plt.plot(x)
plt.show()


