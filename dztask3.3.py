import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])

plt.figure(figsize = (12,6))
plt.plot(df['time'],df['close'])
plt.title('Цена биткоина')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.show()