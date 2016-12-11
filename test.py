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
from login import *
from chat import *
from adminpage import *
from instructorcenter import *
from lecture import *
from logout import *
from message import *
from question import *
from studentcenter import *
from user import *
from test import *
from util import *
from faq import *

class Test(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testMessageToString(self):
        self.content = "This is a message from Alice"
        self.name = "Alice"
        self.now = datetime.datetime.now()

        self.message = Message(content=self.content, name=self.name, time=self.now)
        self.assertEqual(self.message.toString(), ("(" + self.content + "," + self.name + ","  + str(self.now) + ")"))

    def testLoginCheck(self):
        self.assertEqual(Login().checkName("?"), False)
