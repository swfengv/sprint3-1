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
from user import *
from util import *

class InstructorCenter(webapp2.RequestHandler):
    def get(self):
        uNm = getAccount(self.request.cookies.get('CurrentUser'))
        instructor = User.query(User.Name == uNm.userName).get()
        QL = []
        #QL.append(Question.query(Question.lec == 'cs361').fetch())
        for lec in instructor.lectures():
            for Q in lec.QL:
                QL.append(Q)
        SL = []
        for lec in instructor.lectures():
            for username in lec.userNames:
                if not SL.contains(username):
                    SL.append(username)
        template = JINJA_ENVIRONMENT.get_template('Html/insc.html')

        
        template_values = {
            "CurrentUser": uNm.userName,
            'QL': QL,
            'SL': SL
        }
        self.response.write(template.render(template_values))

    def post(self):
        q = Question()
        q.time = datetime.datetime.now()
        q.owner = self.request.get('student')
        q.topic = self.request.get('topic')
        q.content = self.request.get('content')
        q.answered = False
        q.lec = self.request.get('class')
        q.put()
        self.redirect('/insc')

    def goToChat(self):
        id = self.request.get('Quest')

        template_values = {
             'user'
        }