import pandas as pd 
import numpy as np 

pd.set_option('display.max_columns',None)

import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_theme(style ='darkgrid', rc = {'axis.titlesize': 14,
                                       'axes.labelsize': 8,
                                       'axes.titleweight' : 'bold',
                                       'axes.labelweight' : 'normal',
                                       'axes.linewidth' : 2,
                                       'axes.edgecolor' : 'black',
                                       'grid.linestyle' : '--',
                                       'grid.linewidth' : 0.5,
                                       'grid.alpha' : 0.3,
                                       'grid.color' : 'blck',
                                       'xtick.labelsize' : 8,
                                       'ytick.labelsize' : 8,})

from sklearn.preprocessing import StandardScaler, ColumnTransformer
from sklearn.linear_models import LinearRegressing 