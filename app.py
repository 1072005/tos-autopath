import os
import time

while True:
    os.system('python screen.py')
    os.system('python search.py')
    os.system('python rewrite_txt.py')
    os.system('python move.py')

    # 等待5秒
    time.sleep(15)
