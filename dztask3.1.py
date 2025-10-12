import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('iris_data.csv')
plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
species=df['Species'].value_counts()
plt.pie(species.values,labels=species.index,autopct='%1.1f%%')

plt.subplot(1,2,2)
species=df['Species'].value_counts()
f1=len(df[(df['PetalLengthCm']<=1.2)])
f2=len(df[((df['PetalLengthCm']>1.2) & (df['PetalLengthCm']<=1.5))])
f3=len(df[(df['PetalLengthCm']>1.5)])
sizes=[f1,f2,f3]
labels=['<=1.2','1.2 - 1.5', '>1.5']

plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('Разделение по длинам лепестков')

plt.tight_layout()
plt.show()