#-*-coding:utf-8-*-
import subprocess
import os

def adduser():
	p=subprocess.Popen('python config.py',shell=True)
	p.wait()

def deleteuserbyport(port):
	ss = 'cd shadowsocksr && python mujson_mgr.py ' + '-d ' + ' -p ' + port
	p = subprocess.Popen(ss,shell=True)
	p.wait()

def deleteuserbyusername(username):
	ss = 'cd shadowsocksr && python mujson_mgr.py ' + '-d ' + ' -u ' + username
	p = subprocess.Popen(ss,shell=True)
	p.wait()

def viewinfo(username):
	ss = 'cd shadowsocksr && python mujson_mgr.py ' + '-l -u ' + username
	p = subprocess.Popen(ss,shell=True)
	p.wait()

def viewallinfo():
	ss = 'cd shadowsocksr && python mujson_mgr.py -l'
	p = subprocess.Popen(ss,shell=True)
	p.wait()

def setzero(username):
	ss = 'cd shadowsocksr && python mujson_mgr.py -c -u ' + username
	p = subprocess.Popen(ss,shell=True)
	p.wait()

def runserver():
	p = subprocess.Popen('cd shadowsocksr && chmod +x *.sh && ./logrun.sh',shell=True)
	p.wait()

def stopserver():
	p = subprocess.Popen('cd shadowsocksr && chmod +x *.sh && ./stop.sh',shell=True)
	p.wait()

def viewlog():
	p = subprocess.Popen('cd shadowsocksr && chmod +x *.sh && ./tail.sh',shell=True)
	p.wait()

def main():
        os.system('clear')
        print
        print
        print
        print
        print
        print('''========================================
              
          autossr 一键脚本

========================================''')
        print
        print
        print('''	1. 添加用户
        2. 删除用户(端口)
        3. 删除用户(用户名)
        4. 查看用户信息
        5. 查看所有用户信息
        6. 用户使用流量清零
	
	
	7. 启动服务
	8. 关闭服务
	9. 查看日志

	0. 关闭''')

	print
	print

	select = raw_input('选择:')
	print
        if select == '1':
                adduser()
		print
                exit(0)
        elif select == '2':
                port = raw_input('请输入端口:')
		print
                deleteuserbyport(port)
                print
		exit(0)
        elif select == '3':
                username = raw_input('请输入用户名:')
		print
                deleteuserbyusername(username)
                print
		exit(0)
        elif select == '4':
                username = raw_input('请输入用户名:')
		print
                viewinfo(username)
                print
		exit(0)
        elif select == '5':
                viewallinfo()
                print
		exit(0)
        elif select == '6':
                username = raw_input('请输入用户名:')
                print
		setzero(username)
                exit(0)
	elif select == '7':
		runserver()
		print
		exit(0)
	elif select == '8':
		stopserver()
		print
		exit(0)
	elif select == '9':
		viewlog()
		print
		exit(0)
	elif select == '0':
		print
		exit(0)
	else:
		print('输入错误!')
		print
		exit(0)

if __name__ == '__main__':
	main()
