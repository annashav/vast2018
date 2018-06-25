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
FILE_PATH = 'metadata\\AllBirds_quad.csv'
dataframe = pd.read_csv(FILE_PATH)
#dataframe.set_index('Vocalization_type', inplace=True)

y, x = dataframe["Year"], dataframe["Quadrant"].astype("int64")

fig, ax = plt.subplots(tight_layout=False)

#plt.top = 0.1
hist = ax.hist2d(x, y, bins=(range(1, 6), range(1983, 2020)))
plt.colorbar(hist[3], ax=ax)
plt.xlabel("Quadrant")
plt.ylabel("Year")
plt.suptitle("Histogram of Year and Quadrant of Recordings", y=0.95)
plt.show()

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(dataframe["mean_x"], dataframe["mean_y"], dataframe["year"])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Year')
ax.set_title("Average Position Over Time")

plt.xlim(0, 200)
plt.ylim(0, 200)
plt.show()
"""

"""
freq = dataframe[["Year", "Quadrant"]].values

fig, ax = plt.subplots()
im = ax.imshow(freq, cmap="jet")

# We want to show all ticks...
ax.set_xticks(np.arange(0, 35, 2))
ax.set_yticks(np.arange(4))
# ... and label them with the respective list entries
ax.set_xticklabels(range(1983, 2019, 2))
ax.set_yticklabels(np.arange(1, 5))

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_title("Histogram of Year and Vocalization Type")
plt.xlabel("Year")
plt.ylabel("Quadrant")

plt.colorbar(im, ax=ax)

fig.tight_layout()
plt.show()
"""

