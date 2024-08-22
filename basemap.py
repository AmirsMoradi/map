import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Coordinates and population of provinces
locations = {
    'Tehran': {'coords': (35.6892, 51.3890), 'population': 8737510},
    'Shiraz': {'coords': (29.5918, 52.5837), 'population': 1869001},
    'Zanjan': {'coords': (36.6736, 48.4787), 'population': 430871},
    'Isfahan': {'coords': (32.6546, 51.6680), 'population': 1961260},
    'Yazd': {'coords': (31.8974, 54.3569), 'population': 530965},
    'Semnan': {'coords': (35.5770, 53.3930), 'population': 185129},
    'Mashhad': {'coords': (36.2970, 59.6062), 'population': 3001184},
    'Kerman': {'coords': (30.2839, 57.0834), 'population': 738724},
    'Hamadan': {'coords': (34.7987, 48.5150), 'population': 554406},
    'Tabriz': {'coords': (38.0667, 46.2993), 'population': 1558693},
}

#  Basemap
plt.figure(figsize=(10, 8))
m = Basemap(projection='merc', llcrnrlat=25, urcrnrlat=40, llcrnrlon=44, urcrnrlon=63, resolution='i')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgreen', lake_color='aqua')
m.drawparallels(range(25, 41, 5), labels=[1,0,0,0])
m.drawmeridians(range(44, 64, 5), labels=[0,0,0,1])

# اAdd city points to the map
for city, data in locations.items():
    lat, lon = data['coords']
    x, y = m(lon, lat)
    m.scatter(x, y, s=data['population']/10000, marker='o', color='red', alpha=0.5, label=f"{city} ({data['population']})")
    plt.text(x, y, city, fontsize=12, ha='left', va='top', color='black')

# show
plt.title('Important Cities of Iran by Population')
plt.legend(loc='lower left', fontsize='small')
plt.show()