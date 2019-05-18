#-*-coding:utf-8-*-
import sys
import os
import shutil
f = open('atcfg.bk','r')
str = f.read()

path = sys.path[0] + '/'
run_path = path + 'shadowsocksr/logrun.sh'
stop_path = path + 'shadowsocksr/stop.sh'

s = str.replace('run_path',run_path)
s = s.replace('stop_path',stop_path)

fo = open('autossr.service','w')
fo.write(s)
f.close()
fo.close()
shutil.move('autossr.service','/usr/lib/systemd/system/autossr.service')
os.system('systemctl start autossr.service')
os.system('systemctl enable autossr.service')
