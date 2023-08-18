import os
import sys
import re
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3


def ask_url(url):
    head = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as error:
        if hasattr(error,"code"):
            print(error.code)
        if hasattr(error,"reason"):
            print(error.reason)
    return html

if __name__ == '__main__':
    ask_url("https://www.csgoob.com/goods?name=2023%E5%B9%B4%E5%B7%B4%E9%BB%8E%E9%94%A6%E6%A0%87%E8%B5%9B%E7%AB%9E%E4%BA%89%E7%BB%84%E5%8D%B0%E8%8A%B1%E8%83%B6%E5%9B%8A")