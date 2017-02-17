# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:28:29 2016
@author: wb
"""
#引入模块
import socket
import threading
import time
=======
#-*- coding: utf-8 -*-
from socket import *

class TcpClient:
    HOST='192.168.1.110'
    PORT=6340
    BUFSIZ=1024
    ADDR=(HOST, PORT)

    def __init__(self):
        self.client=socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.ADDR)
        print ("has conneted")

        while True:
            data=input('>')
            if not data:
                break
            #self.client.send(data.encode('utf8'))
            data=self.client.recv(self.BUFSIZ)
            if not data:
                break
            print(data.decode('utf8'))
            
if __name__ == '__main__':
    client=TcpClient()
    #add by 9
    #now change it to 9 version
    #got a new example
    #add another
