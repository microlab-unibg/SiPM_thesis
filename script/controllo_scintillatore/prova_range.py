import pyvisa
from Keysight_N6705C import (
    keysight_turnon_range_channel,
)

rm = pyvisa.ResourceManager()
keysight_address='USB0::0x2A8D::0x0F02::MY56006348::INSTR'
# Keysight N6705C setting
keysight = rm.open_resource(keysight_address)
keysight_iset_ch1=0.1

keysight_turnon_range_channel(1, keysight, False)