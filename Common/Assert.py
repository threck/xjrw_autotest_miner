# -*- coding:utf-8 -*-

from Common import Log
from Common import Common


class Assertions(object):
    def __init__(self):
        self.log = Log.Log('assert')

    def assert_text(self, expected_text, target_text):
        """
        check if target text is expected text
        """
        try:
            assert expected_text == target_text
            self.log.info("Case Assert success: expected_text == target_text, expect_value is: %s, target_text is: %s " %
                           (expected_text, target_text))
            return True
        except:
            self.log.error("Case Assert failed: Response text != expected_msg, expected_msg is: %s, target_text is: %s " %
                           (expected_text, target_text))
            raise

