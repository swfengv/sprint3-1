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

# Project imports
from question import *

class Lecture(ndb.Model):
    name = ndb.StringProperty()
    userNames = ndb.StringProperty(repeated=True)
    QL = ndb.StringProperty(repeated=True)

    def enroll(self, User):
        self.userNames.append(User.userName)
        User.lectures.append(self.name)

    def toString(self):
        #str = str.append({)
        #str.append(self.name)
        #str.append(,)
        #str.append([)
        s = (("(") + self.name + (",") + self.userNames.amount() + (",") + ("[") )
        #for i in self.UserNames.length():
        #    s.append(i.Username)
            #s.append(;)
        s.append("]")
        s.append(",")
        s.append("{")
        #for q in self.QL.length():
        #    s.append(q.toString())
        #    s.append(;)
        s.append("}")
        #str.append(,)
        #str.append(self.QL.amount())
        s.append(")")
        return s

    def inclass(self, User):
        #for i in userNames:
        #   if i is User.userName:
        #       return false
        #   else return true

        if User.userName in userNames:
            return false

        else:
            return true