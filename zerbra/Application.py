#coding=utf8
import itchat, time, random, re
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # msg['Text'](msg['FileName'])
    # return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
    with open(msg['FileName'], 'wb') as f:
        f.write(msg['Text']())
        print(msg['Text'])
    print(123)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register([TEXT, PICTURE], isGroupChat=True)
def text_reply(msg):
    print('robo revived:',msg['Content'], 'from', msg['ActualNickName'])
    if msg['isAt']:
        robo_replyGroupMsg(msg)


def robo_replyGroupMsg(msg):
    content = str(msg['Content'])
    pattern = re.compile(r'#[0-9]+')
    match = pattern.search(content)
    if content.__contains__("#add"):
        issueNo = random.randint(1,100)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        updateContent = "[%s][Updated by %s@Wechat]: %s" %(currentTime, msg['ActualNickName'], msg['Content'])
        itchat.send(u'@%s\u2005已为您创建Issue[%s]。\r\n创建内容：%s。\\r\n您可以在这里找到它：http://ipm.lvmama.com/index.php' % (msg['ActualNickName'], str(issueNo), updateContent), msg['FromUserName'])
    elif match:
        issueNo = match.group()
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        updateContent = "[%s][Updated by %s@Wechat]: %s" %(currentTime, msg['ActualNickName'], msg['Content'])
        reply = u'@%s\u2005已为您更新Issue[%s]。\r\n更新内容：%s。\r\n您可以在这里找到它：http://ipm.lvmama.com/index.php' % (msg['ActualNickName'], str(issueNo), updateContent)
        itchat.send(reply, msg['FromUserName'])
    else:
        itchat.send("目前系统仅只支持\r\n#add ：加issue命令。\r\n#issueno ：更改或者添加附件命令。\r\n如需帮助请@管理员。", msg['FromUserName'])


itchat.auto_login(enableCmdQR=True)
itchat.run()