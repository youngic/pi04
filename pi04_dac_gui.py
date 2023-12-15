import datetime
import time
import pyvisa
from lib_pi04_gui import *          # select matched .hex
from subM_inst.pi_instrument import dmm_gwinstek_9061
from subM_inst.pi_instrument import pi_instr_id

rm = pyvisa.ResourceManager()
print(rm.list_resources())  # list connected instrument ID
ins_meas_ = dmm_gwinstek_9061.DmmGwinstek9061(rm, pi_instr_id.dmm_9061_num3_id)

list = [0x0000, 0x0200, 0x0400, 0x0800, 0x0c00, 0x0fff]
pi04_reset()
time.sleep(1)


if __name__ == "__main__":
    cuurent_time = datetime.datetime.now()
    timestamp = cuurent_time.strftime("%Y%m%d%H")
    file_path = 'D:\\N\\{}_orgin.txt'.format(timestamp)

    channel = 2         # config one DAC channel

    with open(file_path, 'a') as file:
        file.write(f'----\t\n')
        pi04_vdac_all_en()
        pi04_vdac_cfg(2.5, 1)
        for i in list:
            ins_meas_.volt_meter_initial()
            pi04_vdac_set(channel, i)
            meas_v = ins_meas_.measure_data()
            mod = round(float(meas_v), 3)
            file.write(f'{mod}\t')
            print(mod, "\t", end='')
            time.sleep(1)

        print("toggle meas...\n")
        file.write(f'----\t\n')

        pi04_idac_all_en()
        for i in list:
            ins_meas_.current_meter_initial()
            pi04_idac(channel, i)
            meas_i = ins_meas_.measure_data()
            mod = round(float(meas_i)*1000, 3)
            file.write(f'{mod}\t')
            print(mod, "\t", end='')
            time.sleep(1)

    pi04_reset()
