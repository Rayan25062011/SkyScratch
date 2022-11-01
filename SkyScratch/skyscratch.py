#!/usr/bin/env python3

import os
import sys
import subprocess
import signal
import socket
import requests
import threading
from subprocess import check_output


class vpn(object):
    def set_restrictions(*args):
        try:
            headers = {
                'Strict-Transport-Security': 'status_code'
            }
            os.environ['HTTPS_PROXY'] = '127.0.0.1'
            r = requests.get('http://127.0.0.1:8000', headers=headers)
            try:
                if r:
                    pass
                else:
                    pass
            except KeyboardInterrupt:
                exit()	
        except Exception as e:
            print("An error accured")
            input("Press any key to continue...")
