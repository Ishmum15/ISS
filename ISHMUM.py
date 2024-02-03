#coding=utf-8
import os, sys, platform
 
os.system('rm -rf ISHMUM.so ISHMUM32.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf ISHMUM.so ISHMUM32.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ISHMUM.so'):
        os.system('https://github.com/Ishmum15/ISS/blob/main/ISHMUM.cpython-311.so) 
        import ISHMUM
    else:
        import ISHMUM
 
elif bit == '32bit':
    if not os.path.isfile('ISHMUM32.so'):
        os.system('https://github.com/Ishmum15/ISS/blob/main/ISHMUM32.cpython-311.so') 
        import ISHMUM32
    else:
        import ISHMUM32
