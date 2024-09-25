import time
import os
import pyvisa

from Keysight_N6705C import (
    keysight_setchannel,
    keysight_turnon_channel,
    keysight_turnon_allchannels,
    keysight_read_channel,
)
from CAEN_HiVolta import caen_setchannel, caen_turnon_upslope_channel, caen_read_channel

# keysight "USB0::10893::3842::MY56006348::0::INSTR"
# Caen "ASRL/dev/ttyACM0::INSTR"

def turn_on_keysight(keysight_address):
    rm = pyvisa.ResourceManager()

    # CONFIGURATION - KEYSIGHT N6705C
    # Channel 1
    keysight_vset_ch1 = 2.4
    keysight_iset_ch1 = 0.5
    # Channel 2
    keysight_vset_ch2 = 1
    keysight_iset_ch2 = 0.15
    # Channel 3
    keysight_vset_ch3 = 2.4
    keysight_iset_ch3 = 0.15
    # Channel 4
    keysight_vset_ch4 = 3.3
    keysight_iset_ch4 = 0.05

    # Keysight N6705C setting
    keysight = rm.open_resource(keysight_address)

    # Set channel values on Keysight
    
    keysight_setchannel(2, keysight_vset_ch2, keysight_iset_ch2, keysight)
    keysight_setchannel(3, keysight_vset_ch3, keysight_iset_ch3, keysight)
    keysight_setchannel(4, keysight_vset_ch4, keysight_iset_ch4, keysight)

    # Keysight N6705C activation
    keysight_turnon_allchannels(keysight)

    ts_ch1, v1, i1 = keysight_read_channel(1, keysight, True)
    ts_ch3, v3, i3 = keysight_read_channel(3, keysight, False)
    ts_ch4, v4, i4 = keysight_read_channel(4, keysight, False)

    print(f"Keysight N6705C is ON - Ch. 1: {v1} V | {i1} A, Ch. 3: {i3} A, Ch. 4: {i4} A")

def turn_on_caen(caen_address):
    rm = pyvisa.ResourceManager()

    # CONFIGURATION - CAEN HiVolta
    caen_channel = 7
    caen_vmax = 250
    caen_imax = 200
    caen_rup = 4
    caen_rdwn = 4

    # CAEN HiVolta setting
    caen = rm.open_resource(caen_address)

    caen_setchannel(caen_channel, caen_vmax, caen_imax, caen_rup, caen_rdwn, caen)
    time.sleep(0.5)
    caen_turnon_upslope_channel(caen_channel, caen)


def startup(keysight_address, caen_address):
    rm = pyvisa.ResourceManager()

    # CONFIGURATION - KEYSIGHT N6705C
    # Channel 1
    keysight_vset_ch1 = 2.4
    keysight_iset_ch1 = 0.5
    # Channel 2
    keysight_vset_ch2 = 1
    keysight_iset_ch2 = 0.15
    # Channel 3
    keysight_vset_ch3 = 2.4
    keysight_iset_ch3 = 0.15
    # Channel 4
    keysight_vset_ch4 = 3.3
    keysight_iset_ch4 = 0.05

    # CONFIGURATION - CAEN HiVolta
    caen_channel = 7
    caen_vmax = 250
    caen_imax = 200
    caen_rup = 4
    caen_rdwn = 4

    # Keysight N6705C setting
    keysight = rm.open_resource(keysight_address)

    # Set channel values on Keysight
    keysight_setchannel(1, keysight_vset_ch1, keysight_iset_ch1, keysight)
    keysight_setchannel(2, keysight_vset_ch2, keysight_iset_ch2, keysight)
    keysight_setchannel(3, keysight_vset_ch3, keysight_iset_ch3, keysight)
    keysight_setchannel(4, keysight_vset_ch4, keysight_iset_ch4, keysight)

    # Keysight N6705C activation
    keysight_turnon_allchannels(keysight)

    # CAEN HiVolta setting
    caen = rm.open_resource(caen_address)

    time.sleep(5)

    # CAEN HiVolta activation
    time.sleep(5)
    # Interlock: check if low voltage is on
    ts_ch1, v1, i1 = keysight_read_channel(1, keysight, True)
    ts_ch3, v3, i3 = keysight_read_channel(3, keysight, False)
    ts_ch4, v4, i4 = keysight_read_channel(4, keysight, False)

    print(f"Keysight N6705C - Ch. 1: {v1} | {i1}, Ch. 3: {v3} | {i3}, Ch. 4: {v4} | {i4}")

    if (
        (v1 >= keysight_vset_ch1 * 0.8)
        & (v3 >= keysight_vset_ch3 * 0.9)
        & (v4 >= keysight_vset_ch4)
    ):
        print("Interlock status: OK")
        caen_setchannel(caen_channel, caen_vmax, caen_imax,
                        caen_rup, caen_rdwn, caen)
        time.sleep(0.5)
        caen_turnon_upslope_channel(caen_channel, caen)
    else:
        print("Interlock status: ERR")
        # caen_setchannel(caen_channel, caen_vmax, caen_imax, caen_rup, 250, caen)
        # time.sleep(0.5)
        # caen_turnon_upslope_channel(caen_channel, caen)


# Try
# startup("USB0::10893::3842::MY56006348::0::INSTR", "ASRL/dev/ttyACM0::INSTR")
