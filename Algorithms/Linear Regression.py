"""Basic example of using linear regression on a data set, hopefully"""
import numpy as np
import pandas as pd
import os, pylab
from matplotlib import pyplot as plt
from pathlib import Path
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

os.chdir('Algorithms')

pipe_lr = Pipeline([('scl', StandardScaler()), ('lr', LinearRegression())])

df = pd.read_csv(Path('SampleData', 'cruise_ship_info.csv'))

print(df.head())