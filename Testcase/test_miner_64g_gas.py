# -*- coding:utf-8 -*-

import pytest
import allure
import sys
from Common import Log
from Mine.Miner import Miner


@pytest.mark.miner_64g
class TestMiner64GTest:

    @allure.feature('64G矿机')
    @allure.story('gasfee')
    @pytest.mark.miner_64G
    @pytest.mark.gasfee
    def test_check_default_gasfee(self):
        logger = Log.Log(sys._getframe().f_code.co_name)
        logger.info("test begining")

        miner = Miner()
        gasfee = miner.xjrw_get_gasfee()

        assert gasfee == 0, f"error -> actual: {gasfee}, expect: 0"

