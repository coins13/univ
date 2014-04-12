import os
import random
import socket

def shake_hands (host):
    """ 3-way handshake をしてみて、繋がったら生きてるとみなす """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((host, 22))
    except socket.error:
        return False
    s.close()
    return True


def search_for_ssh_server ():
    """ 生きてるiMacを探す """

    # ~/.ssh/known_hostsにあるやつから試す
    try:
        with open(os.path.expanduser("~/.ssh/known_hosts")) as f:
            for l in f.readlines():
                host = l.split(",")[0]
                if host.endswith("coins.tsukuba.ac.jp") and shake_hands(host):
                    return host
    except IndexError:
        pass

    hosts = ["borage%02d" % a for a in range(1, 50) ]

    # 5つ試す
    for i in range(0, 5):
        host = random.choice(["borage%02d" % a for a in range(1, 50) ]) + \
               ".coins.tsukuba.ac.jp"
        if shake_hands(host):
            return host
    return ""
