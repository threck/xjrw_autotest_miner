# -*- coding:utf-8 -*-

import subprocess


class Cmd:
    @staticmethod
    def run(cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
        p.wait()
        rt_text = p.communicate()[0]
        rt_value = p.communicate()[1]
        return rt_text, rt_value
