# -*- coding:utf-8 -*-

import pytest
import allure
import sys
from Common import Log
from Common import Assert
from Mine.Miner import Miner

test = Assert.Assertions()

@pytest.mark.miner_64g
class TestMiner64GTest:
    def setup_function(self):
        pass

    def teardown_function(self):
        miner = Miner()
        miner.xjrw_set_gasfee_by_cmd(0)

    @allure.feature('挖矿')
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

        # assert
        assert test.assert_text(expect_value, actual_value)

    @allure.feature('挖矿')
    @allure.story('gasfee')
    @pytest.mark.gasfee
    @pytest.mark.parametrize("expect_value", ['0.000001', '0.001', '1', '10', '100', '1000', '10000', '10000000', '10000000000'])
    def test_set_gasfee_by_cmd(self, expect_value, init_gasfee):
        init_gasfee
        logger = Log.Log(sys._getframe().f_code.co_name)
        logger.info("test begining")

        # test
        miner = Miner()
        miner.xjrw_set_gasfee_by_cmd(expect_value)
        actual_value = miner.xjrw_get_gasfee()

        # assert
        assert test.assert_text(expect_value, actual_value)

    @allure.feature('挖矿')
    @allure.story('gasfee')
    @pytest.mark.gasfee
    @pytest.mark.parametrize("expect_value", ['0.000001', '0.001', '1', '10', '100', '1000', '10000', '10000000', '10000000000'])
    def test_set_gasfee_by_config_file(self, expect_value, init_gasfee):
        init_gasfee
        logger = Log.Log(sys._getframe().f_code.co_name)
        logger.info("test begining")

        # test
        miner = Miner()
        miner.xjrw_set_gasfee_by_config_file(expect_value)
        miner.restart()
        actual_value = miner.xjrw_get_gasfee()

        # assert
        assert test.assert_text(expect_value, actual_value)
