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
from questionanswer import *


# end touples need to be fixed so they have logout and adminpage
#userList = parseTxt("accounts.csv")
app = webapp2.WSGIApplication([
	('/', Login),
    ('/studentcenter', StudentCenter),
    ('/instructorcenter', InstructorCenter),
	('/chat', Chat),
	('/faq', FAQ)
])

# Unit tests
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)
