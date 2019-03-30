''' (c) exlab247@gmail.com 
sudo su -
crontab -e
# paste line to the end, press ctrl + X, Y. Then reboot Pi
@reboot sudo python3 /home/pi/../run_assistant.py
'''

import subprocess as s
import time, os
top_path = os.path.dirname(os.path.abspath(__file__))
main_file = os.path.join(top_path, "main.py")
time.sleep(90)
cmd = "sudo python3 " + main_file
s.Popen(cmd, shell = True)
