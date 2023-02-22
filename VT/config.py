#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/18 11:50 下午
# @Author  : M00yy
# @File    : config.py

import os
import yaml

__config_path = os.path.join(os.path.expanduser("~"), "PycharmProjects/virustotal")
__config_file_path = os.path.join(__config_path, "config.yml")


class __Config(object):
    def __init__(self, ini_path):
        self._file = open(ini_path)
        self._config = self._file.read()
        self._res = yaml.safe_load(self._config)

    def _get_items(self) -> object:
        self._url = self._res["VirusTotal"]["VTUrl"]
        self._api_key = self._res["VirusTotal"]["VTAPIKey"]
        return self._url, self._api_key


config_path = __Config(__config_file_path)

