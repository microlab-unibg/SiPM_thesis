# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:27:05 2024

@author: giorg
"""

import pyvisa
import time

from Keysight_N6705C import (
    keysight_setchannel,
    keysight_turnoff_channel,
    keysight_turnon_channel,
    keysight_turnon_allchannels,
    keysight_read_channel,
)
rm = pyvisa.ResourceManager()
keysight_address='USB0::0x2A8D::0x0F02::MY56006348::INSTR'
# Keysight N6705C setting
keysight = rm.open_resource(keysight_address)

keysight_vset_ch1=1
keysight_iset_ch1=0.1

keysight_setchannel(1, keysight_vset_ch1, keysight_iset_ch1, keysight)
time.sleep(1)
keysight_turnon_channel(1, keysight)

ts_ch1, v1, i1=keysight_read_channel(1, keysight, 1)
print(f"Keysight N6705C is ON - Ch. 1: {v1} V | {i1} A")


time.sleep(1)
keysight_turnoff_channel(1, keysight)
