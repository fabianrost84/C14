import scipy as sp
from scipy import interpolate
import pandas as pd

tlag = 1.0
c14_data_file = '/home/fabian/ownCloud/C14/c14_data/c14_csv_to_pandas/spalding_2013_data.pkl'

c14_data = pd.read_pickle(c14_data_file)

last_c14 = c14_data['d14C'].loc[c14_data['year'].argmax()]
extrapolate_value =[2020.0, last_c14]

c14_data.loc['extrapolate_value'] = extrapolate_value

c14_data = c14_data.sort('year')
c14_data['d14C'] /= 1000.0

def interpolate(xp, fp):
  return lambda x: sp.interp(x, xp, fp)


K = interpolate(c14_data['year'], c14_data['d14C'])
K.__doc__ ='Interpolation function for the atmospheric C14 data extracted from Spalding et al., 2013.' 


Klag = interpolate(c14_data['year'] + tlag, c14_data['d14C'])
Klag.__doc__ ='Interpolation function for the atmospheric C14 data extracted from Spalding et al., 2013., shifted by tlag' 