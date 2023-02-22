#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 9:45 PM
# @Author  : M00yy
# @File    : write_file.py

import json


def write_file(data, filename):
    with open(f"{filename}", "wb") as f:
        f.write(data)


def write_rules(data):
    rule = json.loads(data)
    with open("rule.txt", "w") as f:
        for i in range(len(rule['data'])):
            f.write(rule['data'][i]['attributes']['rules'])
