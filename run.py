# -*- coding:utf-8 -*-
# @Author      : FangChao
# @File        : run
# @Date        : 2021/03/06 0001
# @Description : xjrw_autotest_miner
"""
run testcase：
    python run.py
"""

import os
import pytest
import sys
sys.path.append('.')

from Common import Log
from Common import Common
from Param import Consts
from Config.Config import Config
from Common import Email
from Common import Cmd as command

if __name__ == '__main__':
    # initial
    log = Log.Log()
    config = Config()
    log.info('initialize the configuration file, path: %s' % config.conf_path)
    xml_report_path = config.xml_report_path
    html_report_path = config.html_report_path
    xml_report_path_allure = os.path.join(config.xml_report_path,
                                          'allure%s' % Common.current_time(Consts.TIME_FORMAT_FILE))
    html_report_path_allure = os.path.join(config.html_report_path,
                                           'allure%s' % Common.current_time(Consts.TIME_FORMAT_FILE))

    # run pytest
    # args_allure = ['-s', '-q', '--alluredir', xml_report_path_allure,
    #                'Testcase/test_miner_64g_gas.py::TestMiner64GTest']
    args_allure = ['-s', '-v', '--alluredir', xml_report_path_allure,
                   'Testcase/test_miner_64g_gas.py::TestMiner64GTest']
    args_pytest = ['-s', '-v', '--html=%s' % os.path.join(html_report_path,
                                                          'pytest-html%s' % Common.current_time(Consts.TIME_FORMAT_FILE),
                                                          'report.html'),
                   'Testcase/test_miner_64g_gas.py']
    pytest.main(args_allure)

    # generate allure html reports
    cmd = 'allure generate %s -o %s' % (xml_report_path_allure, html_report_path_allure)
    try:
        command = command.Cmd()
        command.run(cmd)
    except Exception:
        log.error('testcase failed to run, check environment configuration please!')
        raise

    # # send email
    # try:
    #     # email configuration
    #     qq_mail = Email.Email()
    #     qq_mail.smtp_server = config.smtpserver_email
    #     qq_mail.smtp_server_port = config.smtpserverport_email
    #     qq_mail.from_addr = config.from_email
    #     qq_mail.username = config.username_email
    #     qq_mail.to_addr = config.to_email
    #     qq_mail.password = config.password_email
    #     # do send
    #     msg = qq_mail.set_msg()
    #     qq_mail.login()
    #     qq_mail.send(msg)
    #     qq_mail.logout()
    # except Exception as e:
    #     log.error('send email failed, check email config please!')
    #     raise
