# -*- coding: utf-8 -*-

import paramiko
import os

override_flg = False
def sshclient_execmd(hostname, port, username, password):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)

    # exec(s, "cd /opt")
    file = open('./InputFiles/jdbc_list.txt')
    for line in file.readlines():
        line = line.replace('\n','').replace('\r','')
        tmplist = line.split("/")
        len = tmplist.__len__()
        fileName = tmplist[len - 1]
        filePath = ''
        for i in range(len - 1):
            filePath = filePath + '/' + tmplist[i]
            print('filePath:', filePath, "filename:", fileName)
            if override_flg:
                exec(s, "mkdir " + "/opt/zoo_jdbc" + filePath)


        filePath = filePath + '/'
        if override_flg:
            exec(s, "cp /opt/settings" + filePath + fileName +" /opt/zoo_jdbc" + filePath)
            exec(s, "cd /opt/zoo_jdbc" + filePath + ";ls |egrep -v " + fileName + "*|xargs rm -rf")
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/jdbc:mysql:.*[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+:[0-9]\+/jdbc:mysql:\/\/10.200.6.32:3310/g'  " + fileName)
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/oracle:thin:@[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+:[0-9]\+:lvmamadb[0-9]/oracle:thin:@10.201.3.20:1521:lvmamadb/g'  " + fileName)
        # lvmama_super
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/oU7Reu3nLh/AneihpJ924hQ/g'  " + fileName)
        # lvmama_pet
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/hJn4B90rPO/dmgb7hSUKKuk/g'  " + fileName)
        # lvmama_ver
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/ibvXQArO/C9BXjBHpLeB6/g'  " + fileName)
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/nPH3g7yVgn/C9BXjBHpLeB6/g'  " + fileName)
        # lvmama_ord
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/lvmama_ord/PNQA9Sy9d38h/g'  " + fileName)
        # mysql
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/username=mycat/username=admin/g'  " + fileName)
        exec(s, "cd /opt/zoo_jdbc" + filePath + ";sed -i 's/password=365bitlvmama/password=gavRr*Pb27lPHI/g'  " + fileName)

    # exec(s, "ll")
    # exec(s, "ls |egrep -v jdbc*|xargs rm -rf")

    s.close()

def exec(s, cmd):
    stdin, stdout, stderr = s.exec_command(cmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    # print(stdout.read())

def main():
    hostname = '10.201.3.145'
    port = 22
    username = 'root'
    password = 'LEp9jo9M1cY7'
    execmd = "cd /opt"
    sshclient_execmd(hostname, port, username, password)


if __name__ == "__main__":
    main()