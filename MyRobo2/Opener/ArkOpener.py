# -*- coding: utf-8 -*-

import http.cookiejar
import urllib
from Spider import ArkSpider
import memcache

class opener:
    def __init__(self):
        self.mc = memcache.Client(['10.201.3.148:11211'], debug=True)
        cj_str = self.mc.get('cookie')
        if not cj_str:
            self.cj = http.cookiejar.LWPCookieJar('tmp_cookie.txt')
            # self.cj.load('tmp_cookie.txt', ignore_discard=True, ignore_expires=True)
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        else :
            self.cj = http.cookiejar.LWPCookieJar()
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))


        # ip = '10.201.3.164'
        self.sp = ArkSpider.spider(opener, self.cj)

    def login(self):
        self.sp.login()

    def isLogined(self):
        return self.sp.isLogined()

    def findByIp(self, ip):
        pwd = self.mc.get(ip)
        if not pwd:
            if not self.isLogined():
                self.login()
                self.cj.save('tmp_cookie.txt',ignore_discard=True, ignore_expires=True)
                # self.mc.set('cookie', self.cj)
            self.sp.findByIp(ip)
            if self.sp.vmid:
                self.sp.addTempProject()
                pwd = self.sp.parsePwd(ip)
                self.sp.delApp()
                self.mc.set(ip, pwd)
        return pwd