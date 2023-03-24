import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi


df = pd.read_excel('Datos_Rosa_de_Vientos.xlsx')
df['velocidad_x'] = df['VELOCIDAD'] * np.sin(df['DIRECCION'] * pi / 180.0)
df['velocidad_y'] = df['VELOCIDAD'] * np.cos(df['DIRECCION'] * pi / 180.0)
fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
df.plot(kind='scatter', x='velocidad_x', y='velocidad_y', alpha=0.35, ax=ax)
plt.show()