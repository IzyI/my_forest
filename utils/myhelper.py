import os, sys
import yaml

import time
import subprocess


def search_pid(tun):
    cmd = "ps aux|grep '" + str(tun) + "'|grep -v grep |awk '{print $2}'"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, _ = p.communicate()
    if p.returncode == 1:  # no matches found tyrs = []
        return None
    elif p.returncode == 0:  # matches found tyrs = output.split('\n')
        return output.decode('utf-8').split('\n')
    else:  # error, do something with it
        return None


def kill_process(pppd):
    try:
        os.system(" kill -9 " + str(pppd))
    except:
        ...


def open_yaml(path):
    with open(path, 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError as exc:
            print(exc)


def remove_files(path):
    files = os.listdir(path)
    for file in files:
        try:
            os.remove(path + file)
        except:
            continue


def split_array(array, n):
    k, m = divmod(len(array), n)
    return (array[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def print_args(function):
    def wrapper(*args, **kwargs):
        print('Аргументы функции: ', args, kwargs)
        if function(*args, **kwargs):
            print('Yees')
            return True
        else:
            print("NOOO")
            return False

    return wrapper


def repeater_false(lim=3, rest=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(lim):
                result_func = func(*args, **kwargs)
                if result_func == False:
                    time.sleep(rest)
                    continue
                else:
                    return result_func
            return False

        return wrapper

    return decorator
