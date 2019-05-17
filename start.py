#-*-coding:utf-8-*-
import os
import subprocess
def download():
	p=subprocess.Popen('git clone https://github.com/Ssrbackup/shadowsocksr.git',shell=True)
	p.wait()
def init():
	p=subprocess.Popen('cd shadowsocksr && chmod +x initcfg.sh && bash initcfg.sh',shell=True)
	p.wait()
def isroot():
	if os.geteuid() != 0:
		return False
	return True
def writeconfig():
	p=subprocess.Popen('''cd shadowsocksr && sed -i "s/API_INTERFACE = 'sspanelv2'/API_INTERFACE = 'mudbjson'/" userapiconfig.py''',shell=True)
	p.wait()
def main():

	if isroot() == False:
		print('需要使用root用户!')
		exit(0)
	download()
	init()
	writeconfig()
	p = subprocess.Popen('python main.py',shell=True)
	p.wait()

if __name__ == '__main__':
	main()
