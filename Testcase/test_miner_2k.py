# -*- coding:utf-8 -*-

import pytest
import allure


@pytest.mark.websocket
class TestMiner2KTest:

    @allure.feature('2k环境测试')
    @allure.story('环境监测')
    @pytest.mark.miner_2k
    def test_check_miner_process(self):
        pass


