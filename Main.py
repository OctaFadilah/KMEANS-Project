import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = df = pd.read_csv('/content/Gempa Indonesia 2016-2026.csv', delimiter=',')
df2 = df[['depth', 'latitude', 'longitude', 'mag']]

