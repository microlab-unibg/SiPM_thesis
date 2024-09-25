from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import pyvisa
import time
import csv
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
'''
file_path = 'data\\20240429_muons_bias_44V_trig_m50mV_box_indoor\\C1coil20may00001.txt'
dataset = pd.read_csv(file_path, skiprows=4, delimiter='\t', engine='python')
print(dataset)

plt.clf()
plt.plot(dataset.iloc[:,0],dataset.iloc[:,1], color='#000000')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.show()
'''
massimi=list()

#number padding

for i in numpy.arange(1, 73, 1):
    if(i<10):
        file_path = f'data\\20240429_muons_bias_44V_trig_m50mV_box_indoor\\C1coil20may0000{i}.txt'
    else:
        file_path = f'data\\20240429_muons_bias_44V_trig_m50mV_box_indoor\\C1coil20may000{i}.txt'
    dataset = pd.read_csv(file_path, skiprows=4, delimiter='\t', engine='python')
    massimi.append(min(dataset.iloc[:,1]))

N, bins, patches = plt.hist(massimi, bins=73)
print(N, bins, patches)
fracs=N/N.max()
print(fracs)
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.hist(massimi, bins=73, density=True)
plt.show()