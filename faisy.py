import os
import platform
import subprocess
import time

subprocess.call('clear', shell=True)

print('Checking for updates...')

subprocess.call('git pull', shell=True)


permission = input('Do you want to allow permissions? (y/n): ')
if permission.lower() == 'y':
    subprocess.call('termux-setup-storage', shell=True)

try:
    import requests
except ImportError:
    subprocess.call('pip install requests', shell=True)

subprocess.call('git pull', shell=True)


bit = platform.architecture()[0]
if bit == '64bit':
    print("\nCongratulations! Your device supports this tool.")
    from FSL import menu___
    menu___()
elif bit == '32bit':
    print("\nCongratulations! Your device supports this tool.")
    from FSL32 import menu___
    menu___()
else:
    print("Jaa Bhai Maaf Kr:", bit)
