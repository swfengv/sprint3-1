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


suite = unittest.TestLoader().loadTestsFromTestCase(Test)
unittest.TextTestRunner().run(suite)

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
