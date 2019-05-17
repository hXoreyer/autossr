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
def dogetip():
	p = subprocess.Popen('cp getip.py shadowsocksr/getip.py',shell=True)
	p.wait()
	p = subprocess.Popen('''cd shadowsocksr && sed -i "s/import base64/import base64\\nimport getip/" mujson_mgr.py''',shell=True)
	p.wait()
	p = subprocess.Popen('''cd shadowsocksr && sed -i "s/self.server_addr = self.getipaddr()/self.server_addr = getip.getip()/" mujson_mgr.py''',shell=True)
	p.wait()
def main():

	if isroot() == False:
		print('需要使用root用户!')
		exit(0)
	if os.path.exists('shadowsocksr/userapiconfig.py') == True:
		print('已经初始化过，请运行 main.py ')
		exit(0)
	download()
	init()
	writeconfig()
	dogetip()
	p = subprocess.Popen('python main.py',shell=True)
	p.wait()
	os.system('systemctl stop firewalld.service')
	os.system('systemctl disable firewalld.service')

if __name__ == '__main__':
	main()
