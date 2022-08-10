import os
from utils import *
import time


def runHistory():
    dump_str = "the last 5 run comands:\n"
    dump_str += ('\n'.join(str('    '+e[:-2]) for e in get_run_history()))
    dump_str += '\n\n\n'
    return dump_str


def ipAndMacAddress():
    dump_str = f'ip address: {get_ip_address()}\n'
    dump_str += f'mac address: {gma()}'
    dump_str += '\n\n\n'
    return dump_str


def system32():
    dump_str = ('file names in System32:\n')
    dir = "C:\Windows\System32"
    files = fileInDirectory(dir)
    dump_str += '\n'.join(str('    '+e) for e in files)
    dump_str += '\n\n\n'
    return dump_str


def ex_1():
    with open("dumpyfile_1.txt", "a") as f:
        f.truncate(0)
        f.write(runHistory())
        f.write(ipAndMacAddress())
        f.write(system32())


def ex_2(sleep_time: int):
    my_dir = 'C:\whattodo'
    run_dict = {'last_commands': runHistory,
                'net': ipAndMacAddress,
                'dir': system32}
    while True:
        FileList = fileInDirectory(my_dir)
        if FileList:
            FileList = [file for file in FileList if file in (run_dict.keys())]
            out = ''.join([run_dict[name]() for name in FileList])
            with open("dumpyfile_2.txt", "a") as file1:
                file1.write(out)
            [os.remove(f'{my_dir}\{file}') for file in FileList]
        time.sleep(sleep_time)


if __name__ == '__main__':
    ex_1()
    ex_2(0.25)
