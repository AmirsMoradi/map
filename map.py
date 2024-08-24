import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# information
cities = np.array(['Tehran', 'Shiraz', 'Zanjan', 'Isfahan', 'Yazd', 'Semnan', 'Mashhad', 'Kerman', 'Hamadan', 'Tabriz'])

# Separate lists for coordinates and population using numpy
latitudes = np.array([35.6892, 29.5918, 36.6736, 32.6546, 31.8974, 35.5770, 36.2970, 30.2839, 34.7987, 38.0667])
longitudes = np.array([51.3890, 52.5837, 48.4787, 51.6680, 54.3569, 53.3930, 59.6062, 57.0834, 48.5150, 46.2993])
populations = np.array([8737510, 1869001, 430871, 1961260, 530965, 185129, 3001184, 738724, 554406, 1558693])

# Basemap
plt.figure(figsize=(10, 8))
m = Basemap(projection='merc', llcrnrlat=25, urcrnrlat=40, llcrnrlon=44, urcrnrlon=63, resolution='i')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgreen', lake_color='aqua')
m.drawparallels(range(25, 41, 5), labels=[1,0,0,0])
m.drawmeridians(range(44, 64, 5), labels=[0,0,0,1])

# Calculate the position of points on the map
x, y = m(longitudes, latitudes)

# Draw the points of the cities on the map
m.scatter(x, y, s=populations/10000, marker='o', color='red', alpha=0.5)

# Add city names to points
for i in range(len(cities)):
    plt.text(x[i], y[i], cities[i], fontsize=12, ha='left', va='top', color='black')

# Creating a population guide using the actual population of cities
for i in range(len(cities)):
    plt.scatter([], [], s=populations[i]/10000, color='red', alpha=0.5, label=f'{cities[i]}: {populations[i]:,} people')

# help
plt.legend(scatterpoints=1, frameon=True, labelspacing=1, loc='lower left', title="Population")

# show
plt.title('Important Cities of Iran by Population')
plt.show()
