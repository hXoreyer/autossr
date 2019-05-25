#-*-coding:utf-8-*-
import json
import urllib2
import re
import base64
import getip

def openjson():
    f = open('./shadowsocksr/mudb.json','r')
    data = json.load(f)
    return data

def getuserfromname(user_name):
    vjson = openjson()
    for value in vjson:
        if value['user'] == user_name:
            return value
    return False

def formatinfo(user_name, port, method, passwd, protocol, protocol_param, obfs, transfer, up, down, link, con, usr):
    color_green  = '\033[1;32m'
    color_red = '\033[1;31m'
    color_end = '\033[0m'
    infostr = '''===============================

        信息查看

===============================


    '''+ color_green+ '''用 户 名: '''+ color_end+ color_red+ user_name+ color_end+ '''

    '''+ color_green+ '''用    口: '''+ color_end+ color_red+ port+ color_end+ '''

    '''+ color_green+ '''加密方式: '''+ color_end+ color_red+ method+ color_end+ '''

    '''+ color_green+ '''密    码: '''+ color_end+ color_red+ passwd+ color_end+ '''

    '''+ color_green+ '''协    议: '''+ color_end+ color_red+ protocol+ color_end+ '''

    '''+ color_green+ '''协议参数: '''+ color_end+ color_red+ protocol_param+ color_end+ '''

    '''+ color_green+ '''混    肴: '''+ color_end+ color_red+ obfs+ color_end+ '''

    '''+ color_green+ '''最大流量: '''+ color_end+ color_red+ transfer+ color_end+ '''

    '''+ color_green+ '''上    传: '''+ color_end+ color_red+ up+ color_end+ '''

    '''+ color_green+ '''下    载: '''+ color_end+ color_red+ down+ color_end+ '''

    '''+ color_green+ '''上传限速: '''+ color_end+ color_red+ con+ color_end+ '''

    '''+ color_green+ '''下载限速: '''+ color_end+ color_red+ usr+ color_end+ '''

    '''+ color_green+ '''链    接: '''+ color_end+ color_red+ link+ color_end+ '''
    '''
    return infostr

def getinfofromuser(name):
    user = getuserfromname(name)
    if user == False:
        return False
    user_name = str(user['user'])
    port = str(user['port'])
    method = str(user['method'])
    passwd = str(user['passwd'])
    protocol = str(user['protocol'])
    protocol_param = str(user['protocol_param'])
    obfs = str(user['obfs'])
    transfer = user['transfer_enable']
    transfer = str(transfer / (1024**3)) + ' GB'
    up = str(user['u'] / (1024**2)) + ' MB/s'
    down = str(user['d'] / (1024**2)) + ' MB/s'
    ip = getip.getip()
    password_base64 = base64.b64encode(passwd)
    link = ip[0] + ':' + str(info_dict['server_port']) + ':' + str(info_dict['protocol']) + ':' + str(info_dict['method']) + ':plain:'+ str(password_base64[0:-1]) + '/?' + 'obfsparam='
    link = 'ssr://' + base64.b64encode(link)
    con = None
    if 'speed_limit_per_con' in user:
        con = user['speed_limit_per_con']
        con = str(con)+ ' KB/s'
    else:
        con = '无限速'
    usr = None
    if 'speed_limit_per_user' in user:
        usr = user['speed_limit_per_user']
        usr = str(usr)+ ' KB/s'
    else:
        usr = '无限速'
   
    ret = formatinfo(user_name, port, method, passwd, protocol, protocol_param, obfs, transfer, up, down, link, con, usr)
    if ret != False:
        print(ret)
        return True
    return False
