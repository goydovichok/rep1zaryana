import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('iris_data.csv')
cups=('PetalLengthCm','PetalWidthCm','SepalLengthCm','SepalWidthCm')
fig, axes = plt.subplots(2,3,figsize=(15,10))

combs=[(cups[0],cups[1]),(cups[0],cups[2]),(cups[0],cups[3]),(cups[1],cups[1]),(cups[2],cups[3]),(cups[2],cups[3])]
for i in range(6):
    x_feat, y_feat=combs[i]
    ax=axes[i//3,i%3]

    for species in df['Species'].unique():
        data=df[df['Species']==species]
        ax.scatter(data[x_feat],data[y_feat],label=species)

        x=data[x_feat]
        y=data[y_feat]

        ax.set_xlabel(x_feat)
        ax.set_ylabel(y_feat)
        ax.legend()

plt.tight_layout()
plt.show()