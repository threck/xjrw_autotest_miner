# -*- coding:utf-8 -*-

import json
from Common.Cmd import Cmd
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
    def xjrw_set_gasfee(self):
        # nFIL
        # 1 nFIL = 1000pFIL
        # ./lotus-miner xjrw set-gasfee
        pass

    def xjrw_get_gasfee(self):
        # pFIL
        # ./lotus-miner xjrw get-gasfee
        text, value = Cmd.run(miner['xjrw_get_gasfee'])
        if value == 0:
            rt_text = text.split(' ')[-1].strip()
            if rt_text != 0:
                rt_text = text.split(' ')[-2].strip()
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

