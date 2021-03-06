# -*- coding:utf-8 -*-

from configparser import ConfigParser
from Common import Log
import os


class Config(object):
    # title:
    TITLE_TEST = "env_test"
    TITLE_EMAIL = "email"

    # value:
    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SMTP_SERVER_PORT = "smtpserverport"
    VALUE_FROM = "from"
    VALUE_TO = "to"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # path
    local_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

    def __init__(self):
        self.config = ConfigParser()
        self.log = Log.Log()
        self.conf_path = os.path.join(Config.local_path, 'config.ini')
        self.xml_report_path = Config.parent_path+'/Report/xml'
        self.html_report_path = Config.parent_path+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("config file: "+self.conf_path+" not exist!!")

        self.config.read(self.conf_path, encoding='utf-8')

        self.smtpserver_email = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.smtpserverport_email = int(self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER_PORT))
        self.from_email = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_FROM)
        self.to_email = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_TO).split(';')
        self.username_email = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password_email = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        get config text
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        modify config text
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        add config text
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
