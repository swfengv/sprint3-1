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
from old import *
from question import *
from studentcenter import *
from user import *
from test import *
from util import *


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)


userList = parseTxt("accounts.csv")
app = webapp2.WSGIApplication([
	('/', Login),
    ('/studentcenter', StudentCenter),
    ('/instructorcenter', InstructorCenter),
	#('/test', Test),
	('/chat', Chat),
    ('/faq', Faq)
])

# end touples need to be fixed so they have logout and adminpage

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)

