#-*-coding: utf-8-*-
import subprocess
print
localport = str(raw_input('请输入ShadowsocksR账号端口(默认2333):'))
if localport == '':
	localport = '2333'
color_green_begin = '\033[1;32m'
color_green_end = '\033[0m'
color_red_begin = '\033[1;31m'
color_red_end = '\033[0m'
print
print(color_green_begin+' 端口: '+color_green_end+color_red_begin+localport+color_red_end)       
print
username = str(raw_input('请输入用户名:'))
print
print(color_green_begin+' 用户名: '+color_green_end+color_red_begin+username+color_red_end)
print
password = str(raw_input('请输入ShadowsocksR账号密码(默认keing):'))
if password == '':
	password = 'keing'
print
print(color_green_begin + ' 密码: ' + color_green_end + color_red_begin + password + color_red_end)
print
print('请选择ShadowsocksR加密方式:')
print('  1. none')
print('[注意] 如果使用 auth_chain_a 协议，请加密方式选择 none，混淆随意(建议 plain)')
print(''' 
  2. rc4
  3. rc4-md5
  4. rc4-md5-6
 
  5. aes-128-ctr
  6. aes-192-ctr
  7. aes-256-ctr
 
  8. aes-128-cfb
  9. aes-192-cfb
 10. aes-256-cfb
 
 11. aes-128-cfb8
 12. aes-192-cfb8
 13. aes-256-cfb8
 
 14. salsa20
 15. chacha20
 16. chacha20-ietf
 [注意] salsa20/chacha20-*系列加密方式，需要额外安装依赖 libsodium ，否则会无法启动ShadowsocksR !''')

method = raw_input('(默认: 10. aes-256-cfb):')
if method == '':
	method = 'aes-256-cfb';
elif method == '1':
	method = 'none'
elif method == '2':
	method = 'rc4'
elif method == '3':
	method = 'rc4-md5'
elif method == '4':
	method = 'rc4-md5-6'
elif method == '5':
	method = 'aes-128-ctr'
elif method == '6':
	method = 'aes-192-ctr'
elif method == '7':
	method = 'aes-256-ctr'
elif method == '8':
	method = 'aes-128-cfb'
elif method == '9':
	method = 'aes-192-cfb'
elif method == '10':
	method = 'aes-256-cfb'
elif method == '11':
	method = 'aes-128-cfb8'
elif method == '12':
	method = 'aes-192-cfb8'
elif method == '13':
	method = 'aes-256-cfb8'
elif method == '14':
	method = 'salsa20'
elif method == '15':
	method = 'chacha20'
elif method == '16':
	method = 'chacha20-ietf'
else:
	print(color_red_begin+"输入错误!"+color_red_end)
	quit()
print
print(color_green_begin + ' 加密方式: ' + color_green_end + color_red_begin + method + color_red_end)
print
print('请选择ShadowsocksR账号的协议插件:')
print
print(''' 1. origin
 2. auth_sha1_v4
 3. auth_aes128_md5
 4. auth_aes128_sha1
 5. auth_chain_a
 6. auth_chain_b
 [注意] 如果使用 auth_chain_a 协议，请加密方式选择 none，混淆随意(建议 plain)''')
print
protocol = raw_input('(默认: 3. auth_aes128_md5):')
if protocol == '':
	protocol = 'auth_aes128_md5'
elif protocol == 1:
	protocol = 'origin'
elif protocol == 2:
	protocol = 'auth_sha1_v4'
elif protocol == 3:
	protocol = 'auth_aes128_md5'
elif protocol == 4:
	protocol = 'auth_aes128_sha1'
elif protocol == 5:
	protocol = 'auth_chain_a'
elif protocol == 6:
	protocol = 'auth_chain_b'
else:
	print(color_red_begin+'输入错误!'+color_red_end)
	quit()
print
print(color_green_begin + ' 协议插件: ' + color_green_end + color_red_begin + protocol + color_red_end)
print
protocol_param = raw_input('请输入协议参数(同一时间连接设备数)(默认: 5):')
if protocol_param == '':
	protocol_param = '5';
print
print(color_green_begin+' 协议参数: '+color_green_end+color_red_begin+protocol_param+color_red_end)
print
print('''请选择要设置的ShadowsocksR账号 混淆插件
	
 1. plain
 2. http_simple
 3. http_post
 4. random_head
 5. tls1.2_ticket_auth
 [注意] 如果使用 ShadowsocksR 加速游戏，请选择 混淆兼容原版或 plain 混淆，然后客户端选择 plain，否则会增加延迟 !
 另外, 如果你选择了 tls1.2_ticket_auth，那么客户端可以选择 tls1.2_ticket_fastauth，这样即能伪装又不会增加延迟 !
 如果你是在日本、美国等热门地区搭建，那么选择 plain 混淆可能被墙几率更低 !''')
print
obfs = raw_input('(默认: 1. plain):')
if obfs == '':
	obfs = 'plain'
elif obfs == '1':
	obfs = 'plain'
elif obfs == '2':
	obfs = 'http_simple'
elif obfs == '3':
	obfs = 'http_post'
elif obfs == '4':
	obfs = 'random_head'
elif obfs == '5':
	obfs = 'tls1.2_ticket_auth'
else:
	print(color_red_begin + '输入错误!' + color_red_end)
	quit()
print
print(color_green_begin + ' 混淆插件: ' + color_green_end + color_red_begin + obfs + color_red_end)
print

transfer = raw_input('限制总使用流量,单位 GB(默认: 无限):')

svalue = raw_input('当前用户(端口)单线程限速,单位 KB/s(默认: 无限速):')

Svalue = raw_input('当前用户(端口)总限速,单位 KB/s(默认: 无限速):')
print
if transfer != '':
	print(color_green_begin+' 总流量: '+color_green_end+color_red_begin+transfer+color_red_end)
else:
	print(color_green_begin+' 总流量: '+color_green_end+color_red_begin+'无限'+color_red_end)
if svalue != '':
	print(color_green_begin+' 单线程限速: '+color_green_end+color_red_begin+svalue+color_red_end)
else:
	print(color_green_begin+' 单线程限速: '+color_green_end+color_red_begin+'无限速'+color_red_end)
if Svalue != '':
	print(color_green_begin+' 总限速: '+color_green_end+color_red_begin+Svalue+color_red_end)
else:
	print(color_green_begin+' 总限速: '+color_green_end+color_red_begin+'无限速'+color_red_end)
print

ss = 'cd shadowsocksr && python mujson_mgr.py -a -u '+ username + ' -p ' + localport + ' -k ' + password + ' -m ' + method + ' -O ' + protocol + ' -o ' + obfs + ' -G ' + protocol_param
if transfer != '':
	ss = ss + ' -t ' + transfer
if svalue != '':
	ss = ss + ' -s ' + svalue
if Svalue != '':
	ss = ss + ' -S ' + Svalue
p=subprocess.Popen(ss,shell=True)
p.wait()
