import pandas
import matplotlib.pyplot as plt

df = pandas.read_excel('autompg.xlsx')


x = df['cylindres']
y = df["puissance"]

plt.bar(x, y, color='black' ) 
#plt.plot(x.iloc[0:215],y.iloc[0:215] ,"ro")
plt.xlabel('cylindres')
plt.ylabel('puissance')


#plt.plot(x.iloc[0:215],y.iloc[0:215] ,"ro")
