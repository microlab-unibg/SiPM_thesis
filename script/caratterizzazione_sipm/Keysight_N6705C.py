import datetime
import time
from pyvisa import util
import numpy as np


def keysight_setchannel(channel, voltage, curr_max, keysight):
    keysight.write(
        f"VOLTage:LEVel {voltage},(@{channel});:CURRent:LEVel {curr_max},(@{channel})")
    print(
        f"Keysight N6705C on channel {channel} is set at {voltage}V and {curr_max}A")


def keysight_turnon_channel(channel, keysight):
    keysight.write(f"OUTP ON,(@{channel})")
    print(f"keysight N6705C channel {channel} is ON")


def keysight_turnoff_channel(channel, keysight):
    keysight.write(f"OUTP OFF,(@{channel})")
    print(f"keysight N6705C channel {channel} is OFF")


def keysight_turnon_allchannels(keysight):
    keysight.write("OUTP ON,(@1,2,3,4)")
    print(f"keysight N6705C channel 1, 2, 3, 4 are ON")


def keysight_turnoff_allchannels(keysight):
    keysight.write("OUTP OFF,(@1,2,3,4)")
    print(f"keysight N6705C channel 1, 2, 3, 4 are OFF")


def keysight_read_channel(channel, keysight, curr_flag):
    keysight.write("FORM REAL")
    if curr_flag:
        keysight.write(f"SENS:ELOG:FUNC:CURR ON,(@{channel})")
    else:
        keysight.write(f"SENS:ELOG:FUNC:VOLT ON,(@{channel})")
    keysight.write(f"SENS:ELOG:PER 0.001,(@{channel})")
    keysight.write(f"SENS:ELOG:PER? (@{channel})")
    keysight.write(f"TRIG:TRAN:SOUR BUS,(@{channel})")
    keysight.write(f"INIT:ELOG (@{channel})")
    time.sleep(0.1)
    keysight.write(f"TRIG:ELOG (@{channel})")
    keysight.write("SYST:ERR?")
    time.sleep(0.1)
    time_stamp = datetime.datetime.fromtimestamp(time.time())
    keysight.write(f"FETC:ELOG? 10000, (@{channel})")
    lv_data_real = keysight.read_raw()
    lv_data_ascii = util.from_ieee_block(
        lv_data_real, datatype='f', is_big_endian=True)

    if (len(lv_data_ascii) != 0):
        lv_voltage = np.mean(lv_data_ascii[1::2])
        lv_current = np.mean(lv_data_ascii[0::2])

    return time_stamp, lv_voltage, lv_current