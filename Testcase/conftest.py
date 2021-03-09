# -*- coding:utf-8 -*-

import pytest
from Mine.Miner import Miner


@pytest.fixture()
def init_gasfee():
    yield
    miner = Miner()
    miner.xjrw_set_gasfee(0)

