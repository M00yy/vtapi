#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 11:31 下午
# @Author  : M00yy
# @File    : operation.py

import requests
import urllib3
from .config import __config_file_path, __Config
from VT.parse.parse_file import *
from VT.parse.write_file import *

urllib3.disable_warnings()
__url, __headers = __Config(__config_file_path)._get_items()
_headers = {"x-apikey": __headers}


def SearchFile(query):
    url = __url + f"intelligence/search?query={query}"
    r = requests.get(url=url, headers=_headers)
    if r.status_code == 200:
        res = parse_file_struct(r.content)
        return res['data'][0]['attributes']
    # TODO: judge err type from return r.status_code
    else:
        print(f"[!] Code is {r.status_code}")


def SearchIP(query):
    url = __url + f"ip_addresses/{query}"
    response = requests.get(url=url, headers=_headers)
    if response.status_code == 200:
        print(response.content)
    else:
        print(f"[!] Code is {response.status_code}")


def DownloadFile(_hash):
    url = __url + f"files/{_hash}/download"
    r = requests.get(url=url, headers=_headers)
    if r.status_code == 200:
        write_file(r.content, _hash)
        print("[*] Success Download!")
    else:
        print(f"[!] Code is {r.status_code}.")


def GetLiveHunt(op="print"):
    """
    :param op: default "print" out by console; w2f, write to file -> rule.txt.
    :return: void
    """
    url = __url + f"intelligence/hunting_rulesets"
    r = requests.get(url=url, headers=_headers)
    if r.status_code == 200:
        if op == "print":
            parse_rules(data=r.content)
        elif op == "w2f":
            write_rules(r.content)
        # print(res)
    # TODO: judge err type from return r.status_code
    else:
        print(f"[!] Code is {r.status_code}")


def GetRetrohunt_jobs():
    """
    :return: void
    """
    url = __url + f"intelligence/retrohunt_jobs?limit=10"
    response = requests.get(url=url, headers=_headers)
    if response.status_code == 200:
        print(response.content)
    else:
        print(f"[!] Code is {response.status_code}")
