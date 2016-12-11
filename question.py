# Library imports
import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

# Project imports
from message import *

class Question(ndb.Model):
    student = ndb.StringProperty()
    topic = ndb.StringProperty()
    lec = ndb.StringProperty()
    time = datetime.datetime.now()
    #messageList = ndb.StructuredProperty(Message, Repeated=True)

    def toString(self):
        s = (("(")+ self.topic + (",") + self.lec  + (",") + self.time  + (",") + ("{") )
                    # str = str.append(self.content)
                    #        str.append(,)
                    # str.append(self.topic)
                    #str.append(,)
                    # str.append(self.student)
                    #str.append(,)
                    # str.append(self.lec)
                    # str.append(,)
                    # str.append(self.time)
                    #str.append(,)
                    # str.append({)
        for i in self.MessageList.length():
            s.append(i.toString())
            s.append(";")
        s.append("}")
        s.append(")")
        return s