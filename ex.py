import subprocess
from getmac import get_mac_address as gma
import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


print(gma())
print(get_ip_address())


#cmd_history = subprocess.check_output(["doskey", "/history"])
# with open("saved_commands.txt", "wb") as f:
#    f.write(cmd_history)
