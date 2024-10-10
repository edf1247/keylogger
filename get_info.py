import socket
import os
import platform
import win32clipboard

def get_sys_info():
    ip = socket.gethostbyname(socket.gethostname())
    _os = os.name
    _platform = platform.system()
    return ip, _os, _platform


