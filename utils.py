import winreg
from getmac import get_mac_address as gma
import socket
import os
from os.path import isfile, join


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def get_run_history():
    # Get the necessary HKEY
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hkey:
        sub_key = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU'
        # Go to the environment key
        with winreg.OpenKey(hkey, sub_key, 0, winreg.KEY_READ) as sub_key:
            MRUList = winreg.QueryValueEx(sub_key, 'MRUList')[0]
            MRUList = MRUList[0:min(5, len(MRUList))]
            return [(winreg.QueryValueEx(sub_key, ind)[0]) for ind in MRUList]


def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in os.listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)


def fileInAllDirectory(my_dir: str):
    for path, subdirs, files in os.walk(my_dir):
        for name in files:
            print(os.path.join(path, name))
