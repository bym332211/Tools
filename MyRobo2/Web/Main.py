# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import http.cookiejar
import urllib
import time
from tornado.options import define, options
from Opener import ArkOpener
define("port", default=9999, help="run on the given port", type=int)

opener = ArkOpener.opener()


class Hello(tornado.web.RequestHandler):
    def get(self):
        time.sleep(30)
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', world!')

class FindIpPwd(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument('ip', '')
        if ip:
            self.write('ip:' + ip)
            self.write('<br>')
            # ip = '10.201.3.164'
            pwd = opener.findByIp(ip)
            self.write('pwd:' + pwd)
            # sp = ArkSpider.spider(opener, cj)
            # sp.login()
            # sp.findByIp(ip)
            # if sp.vmid:
            #     sp.addTempProject()
            #     pwd = sp.parsePwd(ip)
            #     sp.delApp()
            #
        else :
            self.write('please input ip')



if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", Hello),
        (r"/ip", FindIpPwd)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()