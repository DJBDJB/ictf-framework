# -*- coding: utf-8 -*-
import socket
import cPickle
import base64
import marshal
import random
import time
import datetime

class Benign():

  def execute(self,ip,port,flag_id='',token=''):

    error = -1
    error_msg = ''
    flag_id = datetime.datetime.fromtimestamp(random.randint(1,int(time.time()))).strftime("%Y/%m/%d")

    token = cities[random.randint(0,len(cities)-1)]

    try:

      s = socket.socket()
      s.connect((ip,port))

      s.recv(1024)
      s.send("1")
      msg = s.recv(1024)
      s.send(flag_id)
      msg = s.recv(1024)
      s.send(token)
      self.flag = s.recv(1024)
      error = 0

    except Exception as e:
      error = 42
      error_msg = str(e)

    self.flag_id = flag_id
    self.token = token
    self.error = error
    self.error_msg = error_msg
  
  def result(self):
    return {'FLAG_ID' : self.flag_id,
	    'TOKEN' : self.token,
	    'FLAG' : self.flag,
	    'ERROR' : self.error,
	    'ERROR_MSG' : self.error_msg,
	    }