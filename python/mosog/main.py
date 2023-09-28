import subprocess
import sys

try:
    import pywhatkit as pyw
except ImportError:
    print("pywhatkit not found so installing")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pywhatkit'])
    print("installed pywhatkit")
    import pywhatkit as pyw

print("imported pywhatkit")

try:
    pyw.sendwhatmsg_instantly("+919003795566", "hello world")
    print("sent message")
    pyw.playonyt('Joker bgm song (bass boosted)"')
    print("played YT video")
except Exception as e:
    print("a error")
    print(e)
input("Press enter to exit")
