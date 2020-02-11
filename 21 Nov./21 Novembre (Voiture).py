import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("autompg.xlsx", sep='\t', header= 0)
plt.figure(figsize=(9, 10))

y=df['année de modèle'].head()
x=df['mpg'].head()
plt.xlim(0, 2)
plt.plot([x,y,])
plt.xlabel('Cylindres')
plt.ylabel('Poids')

