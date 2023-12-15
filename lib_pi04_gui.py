
from subM_brig.pisemi_hid import PiHid
from subM_brig.dev_i2c_spi import *

hid_bridge_ = PiHid(0x10c6, 0x8468)
pAddChip = 0x80
# pAddChip = (0x80 << 1) & 0xff

def pi04_reset():
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x01, 0x0001)

def pi04_dac_all_en():
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x03, 0x00FF)  # DAC enable all
def pi04_vdac_all_en():
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x03, 0x000f)  # vdac_all_en
def pi04_idac_all_en():
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x03, 0x00f0)  # idac_all_en
def pi04_vdac_one_en(pCh):
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x03, (1 << pCh) & 0x000f)  # pCh's VDAC enable, 0~3
def pi04_idac_one_en(pCh):
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x03, (1 << (pCh+4)) & 0x00f0)  # pCh's IDAC enable, 0~3


def pi04_vdac_cfg(pGain = 2.5, pDir = 1):
    """
    :param pGain: 2.5 stand for set 2.5V gain, other is 5V
    :param pDir: 1 stand for set positive range, other is negative range
    :return:
    """
    mask = 0x0000
    if pGain == 2.5:
        mask = mask | 0x0055
    if pDir == -1:
        mask = mask | 0x00aa

    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x01, 0x08, mask)
    return mask

def pi04_vdac_set(pCh, pCode):
    """
    :param pCh: 0~3
    :param pCode: 0x0000 to 0x0fff
    :return:
    """
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x02, 0x00 + pCh, pCode)

def pi04_idac(pCh, pCode):
    """
    :param pCh: 0~3
    :param pCode: 0x0000 to 0x0fff
    :return:
    """
    hid_bridge_.pi04_plus_i2c_write(pAddChip, 0x02, 0x04 + pCh, pCode)  # IDAC1~4


