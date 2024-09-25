# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:27:05 2024

@author: giorg
"""

import pyvisa
import time
import csv
import numpy

from Keysight_N6705C import (
    keysight_setchannel,
    keysight_read_channel,
    keysight_turnon_channel,
)

rm = pyvisa.ResourceManager()
keysight_address='USB0::0x2A8D::0x0F02::MY56006348::INSTR'
# Keysight N6705C setting
keysight = rm.open_resource(keysight_address)

keysight_iset_ch1=0.1

with open('data_IV_scintillatore.csv', 'w', newline='') as csvfile:
                                fieldnames = ['Voltage', 'Current']
                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                writer.writeheader()

keysight_turnon_channel(1, keysight)

for i in numpy.arange(0, 43, 1):
    if i==0:
         keysight_vset_ch1=0.015   
    else: 
        keysight_vset_ch1=i
    keysight_setchannel(1, keysight_vset_ch1, keysight_iset_ch1, keysight)
    ts_ch1, v1, i1=keysight_read_channel(1, keysight, 1)
    print(f"Keysight N6705C is ON - Ch. 1: {v1} V | {i1} A")
    with open('data_IV_scintillatore.csv', 'a', newline='') as csvfile:
                                fieldnames = ['Voltage', 'Current']
                                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                writer.writerow({'Voltage': v1, 'Current': i1})
    time.sleep(1)
