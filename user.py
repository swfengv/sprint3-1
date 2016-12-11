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
from lecture import *

class User(ndb.Model):
    Name = ndb.StringProperty()
    userName = ndb.StringProperty()
    password = ndb.StringProperty()
    aType = ndb.StringProperty()
    lectures = ndb.StringProperty(repeated=True)
    #lectures = ndb.StructuredProperty(Lecture, repeated=True)

    def toString(self):
        s= ("("+self.name + (",") + self.userName + (",") + self.password + (",") + self.aType + (",") + ("{") )

        # Old version
        #for i in self.Lectures.length():
        #    s.append(i.Name)
        #    s.append(";")

        # To be tested
        #s.append(str(Lectures))
        s.append("}")
        s.append(")")
        return s