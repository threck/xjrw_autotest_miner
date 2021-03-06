# -*- coding:utf-8 -*-

import pytest
import allure
import sys
from Common import Log
from Mine.Miner import Miner


@pytest.mark.miner_64g
class TestMiner64GTest:
    def setup_function(self):
        pass

    def teardown_function(self):
        miner = Miner()
        miner.xjrw_set_gasfee(0)

    @allure.feature('64G矿机')
    @allure.story('gasfee')
    @pytest.mark.gasfee
    def test_check_default_gasfee(self):
        logger = Log.Log(sys._getframe().f_code.co_name)
        logger.info("test begining")
        # param
        expect_value = '0'
        actual_value = None

        # test
        miner = Miner()
        actual_value = miner.xjrw_get_gasfee()

        assert expect_value == actual_value, f"error -> expect: {expect_value}, actual: {actual_value}"

    @allure.feature('64G矿机')
    @allure.story('gasfee')
    @pytest.mark.gasfee
    @pytest.mark.parametrize("expect_value", ['0.000001', '0.001', '1', '10', '100', '1000', '10000', '10000000', '10000000000'])
    def test_set_gasfee(self, expect_value, init_gasfee):
        init_gasfee
        logger = Log.Log(sys._getframe().f_code.co_name)
        logger.info("test begining")

        # test
        miner = Miner()
        miner.xjrw_set_gasfee(expect_value)
        actual_value = miner.xjrw_get_gasfee()

        # assert
        assert expect_value == actual_value, f"error -> expect: {expect_value}, actual: {actual_value}"

