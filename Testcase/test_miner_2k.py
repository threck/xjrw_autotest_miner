# -*- coding:utf-8 -*-

import pytest
import allure


@pytest.mark.miner_2k
class TestMiner2KTest:

    @allure.feature('2k环境测试')
    @allure.story('环境监测')
    def test_check_miner_process(self):
        pass


