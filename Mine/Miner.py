# -*- coding:utf-8 -*-

import json
from Common.Cmd import Cmd
from Common import Coin
from Param.MineCmd import miner


class Miner(object):
    # service
    def start(self):
        # nohup ./lotus-miner run &> ${log} &
        # bash start_miner.sh ${config_file}
        pass

    def start_nosync(self):
        # nohup ./lotus-miner run --nosync &> ${log} &
        # bash stop_miner.sh ${config_file}
        pass

    def stop(self):
        # bash stop_miner.sh
        pass

    def restart(self):
        # bash restart_miner.sh ${config_file}
        pass

    # information
    def sealing_jobs(self):
        # ./lotus-miner sealing jobs
        pass

    def sealing_workers(self):
        # ./lotus-miner sealing workers
        pass

    def info(self):
        # ./lotus-miner info
        pass

    # sectors
    def sectors_pledge(self):
        # ./lotus-miner sectors pledge
        pass

    def sectors_list(self):
        # ./lotus-miner sectors list
        pass

    # storage
    def storage_cleanup(self):
        # ./lotus-miner storage cleanup
        pass

    def storage_list(self):
        # ./lotus-miner storage list
        pass

    def storage_find(self):
        # ./lotus-miner storage find ${sector_id}
        pass

    # xjrw command
    def xjrw_set_gasfee(self, fee):
        # nFIL
        # 1 nFIL = 1000pFIL
        # ./lotus-miner xjrw set-gasfee
        rt_text, value = Cmd.run(f"{miner['xjrw_set_gasfee']} {fee}")
        return rt_text, value

    def xjrw_get_gasfee(self):
        # pFIL
        # ./lotus-miner xjrw get-gasfee
        text, value = Cmd.run(miner['xjrw_get_gasfee'])
        if value == 0:
            rt_text = text.split(' ')[-1].strip()
            print(f'rt_text:{rt_text}')
            if rt_text != '0':
                unit = text.split(' ')[-1].strip()
                count = text.split(' ')[-2].strip()
                print(f'unit:{unit}')
                print(f'count:{count}')
                rt_text, unit = Coin.to_nfil(int(count), unit)
                print(f'rt_text:{rt_text}')
                print(f'unit:{unit}')
        else:
            rt_text = text
        return rt_text

    def set_config_json(self):
        # vim /root/config.json
        pass

    def xjrw_reload_config(self):
        # ./lotus-miner xjrw reload
        pass

    def xjrw_windowspost(self):
        # ./lotus-miner xjrw windowspost
        pass

    def xjrw_winningpost(self):
        # ./lotus-miner xjrw winningpost
        pass

