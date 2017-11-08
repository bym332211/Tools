# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
from selenium import webdriver
import re
import datetime
import http.cookiejar
import urllib
import json
import time


class spider:
    browser_path = 'C:\\Program Files\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'

    def __init__(self, opener, cj):
        self.opener = opener
        self.cj = cj



    def login(self):
        print("Starting Login")
        back_url = "http://192.168.0.84:8080/theone-web/admin/index"
        login_url = "http://192.168.0.84:8080/theone-web/login?logout=1"
        user = 'bym2211'
        pwd = '123456'
        post = {
            "BackURL":back_url,
            "password":pwd,
            "username":user

        }
        header = {
            "Accept":"*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "accept-encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host":"192.168.0.84:8080",
            "Origin":"http://192.168.0.84:8080",
            "Upgrade-Insecure-Requests":"1",
            "Referer":"http://192.168.0.84:8080/theone-web/login?logout=1"
        }

        postData = urllib.parse.urlencode(post)
        postData = postData.encode('utf-8')
        req = urllib.request.Request(login_url, postData, header)
        # res = urllib.request.urlopen(req)
        # self.cj = http.cookiejar.CookieJar()
        # self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        self.cj.add_cookie_header(req)
        res = self.opener.open(req)
        content = res.read().decode('utf-8')
        if res.url.startswith('http://192.168.0.84:8080/theone-web/admin/index'):
            print("Login Succes")
        # print(content)

    def isLogined(self):
        url = 'http://192.168.0.84:8080/theone-web/admin/index'
        res = self.opener.open(url)
        if res.url.startswith('http://192.168.0.84:8080/theone-web/admin/index'):
            print("Login Succes")
            return True


    def getAllVm(self):
        url = 'http://192.168.0.84:8080/theone-web/machine/getAllVm'
        res = self.opener.open(url)
        content = res.read().decode('utf-8')
        self.vms = json.loads(content)

    def findByIp(self, ip):
        self.getAllVm()
        for vm in self.vms:
            if ip == vm["ip"]:
                self.vmid = str(vm['vmid'])
                print('hit![' + self.vmid + "]:" + ip)

    def addTempProject(self):
        url = 'http://192.168.0.84:8080/theone-web/app/add?has_config=2&project_id=149&name=pagea&version_type=1&version_url=test&config_url=&instance_count=1&root_pom=pom.xml&goal_option=clean%20install%20-Dmaven.test.skip=true&type=1&build_order=0&ip_allocat_type=1&ips=' + self.vmid
        try :
            self.opener.open(url)
        except Exception as e:
            print('Add test app')

    def parsePwd(self, ip):
        time.sleep(15)
        url = 'http://192.168.0.84:8080/theone-web/app/allby_projectid?project_id=149'
        res = self.opener.open(url)
        content = res.read().decode('utf-8')
        appInfos = json.loads(content)
        # for info in appInfos:
        #     print(info)
        for app in appInfos['apps']:
            if app['name'] == 'pagea':
                deploys = app['deploys']
                for deploy in deploys:
                    self.appId = str(deploy['appId'])
                    for link in deploy['linkList']:
                        if link['linkName'] == 'SSH':
                            self.sshUrl = link['linkUrl']
        print(self.sshUrl)
        pwd = self.sshUrl[11:].replace('@' + ip, '')
        print(pwd)
        return pwd

    def delApp(self):
        if self.appId:
            url = 'http://192.168.0.84:8080/theone-web/app/del?id=' + str(self.appId)
            res = self.opener.open(url)




