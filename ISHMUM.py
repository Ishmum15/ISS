import os,platform
os.system('git pull')
#exit('\n Update Soon...!')
ISHMUM=platform.architecture()[0]
if ISHMUM=="32bit":__import__("ISHMUM32")
elif ISHMUM=="64bit":__import__("ISHMUM")
