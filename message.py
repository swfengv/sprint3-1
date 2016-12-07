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

class Message(ndb.Model):
    content = ndb.StringProperty()
    name = ndb.StringProperty()
    time = ndb.DateTimeProperty()

    def contains(self, str): # Not needed in the final design, but it might be helpful for debug
        if content.contains(str) or name.contains(str):
            return True

        else:
            return False

    def toString(self):
        return ("(" + self.content + "," + self.name + "," + str(self.time) + ")")

    def timeSince(self): # Again, probably not needed for the application, but it might be useful if we want to look at the time between messages sent
        pass
