import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/Gempa Indonesia 2016-2026.csv', delimiter=',')

## 

plt.figure(figsize=(12, 8))
m = Basemap(projection='merc', 
            llcrnrlat=-20, urcrnrlat=15, 
            llcrnrlon=85, urcrnrlon=150, 
            resolution='i')

m.drawcoastlines(color='gray', linewidth=1.0)
m.drawcountries(color='gray', linewidth=1.0)
m.drawmapboundary(fill_color='#A6CAE6')
m.fillcontinents(color='#E5E4E2', lake_color='#A6CAE6')

x, y = m(df['longitude'].values, df['latitude'].values)

m.scatter(x, y, s=10, c='red', marker='o', alpha=0.5, label='Epicenter')

plt.title('Earthquake Epicenter Distribution Map In Indonesia', fontsize=14, fontweight='bold')
plt.legend(loc='lower left')
plt.show()
