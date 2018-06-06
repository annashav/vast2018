from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

SPECIES = [
    "BEN","BLU","BOM","BRO","CAN","CAR",
    "DAR","EAS","GRE","LES","ORA","ORD",
    "PIN","PUR","QAX","QUE","ROS","SCR",
    "VER",
]

VOCALS = ["Call", "Song", "Call and Song", "Bill-Snapping", "Drumming", "Scold"]
FILE_PATH = 'metadata\\freq_vocal_year.csv'
dataframe = pd.read_csv(FILE_PATH)
dataframe.set_index('Vocalization_type', inplace=True)

"""
y, x = dataframe["Year"], dataframe["Month"].astype("int64")

fig, ax = plt.subplots(tight_layout=False)

plt.top = 0.1
hist = ax.hist2d(x, y, bins=(range(1, 14), range(1983, 2020)), cmap="jet")
plt.colorbar(hist[3], ax=ax)
plt.xlabel("Month")
plt.ylabel("Year")
plt.suptitle("Histogram of Year and Month of Recordings", y=0.95)
plt.show()
"""

freq = dataframe.values#np.random.rand(19, 35)

fig, ax = plt.subplots()
im = ax.imshow(freq, cmap="jet")

# We want to show all ticks...
ax.set_xticks(np.arange(0, 35, 2))
ax.set_yticks(np.arange(6))
# ... and label them with the respective list entries
ax.set_xticklabels(range(1983, 2019, 2))
ax.set_yticklabels(VOCALS)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_title("Histogram of Year and Vocalization Type")
plt.xlabel("Year")
plt.ylabel("Vocalization Type")

plt.colorbar(im, ax=ax)

fig.tight_layout()
plt.show()

