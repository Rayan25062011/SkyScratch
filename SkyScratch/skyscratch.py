#!/usr/bin/env python3

import os
import sys
import subprocess
import signal
import requests
import random
import socket
from subprocess import check_output

class SkyScratch(object):
    def start(*args):
        try:
            headers = {
                'Strict-Transport-Security': 'status_code'
            }
            ip = {
                "https": 'https://158.177.252.170:3128',
                "http": 'https://158.177.252.170:3128'
            }
            ip2 = {
                "https": "https://135.181.146.187:80",
                "http": "http://135.181.146.187:80"
            }
            ip3 = {
                "https": "https://52.194.231.209:8080",
                "http": "http://52.194.231.209:8080"
            }
            
            ip4 = {
                "https": "https://202.61.204.51:80",
                "http": "http://202.61.204.51:80"
            }

            ip5 = {
                "https": "https://190.61.84.166:9812",
                "http": "http://190.61.84.166:9812"
            }

            ip6 = {
                "https": "https://46.105.87.167:53281",
                "http": "http://46.105.87.167:53281"
            }

            ip7 = {
                "https": "https://144.76.42.215:8118",
                "http": "http://144.76.42.215:8118"
            }

            ip8 = {
                "https": "https://80.106.247.145:53410",
                "http": "http://80.106.247.145:53410"
            }
            list_ = [ip, ip2, ip3, ip4, ip5, ip6, ip7, ip8]
            randip = random.choice(list_)
            if randip == ip2:
                print("CONNECTION Finland")
                print("<DUISGUISE: 135.181.146.187>") 

            if randip == ip3:
                print("<CONNECTION Japan>")
                print("<DUISGUISE: 52.194.231.209>")

            if randip == ip4:
               print("<CONNECTION Austria>") 
               print("<DUISGUISE: 202.61.204.51>")

            if randip == ip5:
                print("<CONNECTION Costa Rica>")
                print("<DUISGUISE: 190.61.84.166>")

            if randip == ip6:
                print("<CONNECTION France>")
                print("<DUISGUISE: 190.61.84.166>")

            if randip == ip7:
                print("<CONNECTION Germany>")
                print("<DUISGUISE: 144.76.42.215>")

            if randip == ip8:
                print("<CONNECTION Greece>")
                print("<DUISGUISE: 80.106.247.145>")

            if randip == ip:
                print("<CONNECTION North America>")
                print("<DUISGUISE: 158.177.252.170>")
            trick = {
                "origin": f"{randip}"
            }
            requests.put("http://localhost:8000", trick)
            r = requests.get('http://localhost:8000', proxies=randip, timeout=None)
            try:
                if r:
                    pass
                else:
                    pass
            except KeyboardInterrupt:
                exit()	
                
        except Exception as e:
            print(e)
            print("An error occured")
            input("Press any key to continue...")
            exit()
