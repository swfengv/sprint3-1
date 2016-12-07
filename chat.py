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

class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('Html/chat.html')

        student = self.request.get("student")
        user = self.request.cookies.get("CurrentUser")

        if student == "":
            student = getInstrAccount(userList).getName()

        self.response.set_cookie("receiver", student, max_age=360, path="/")
        messages = list(Message.query().order(Message.time, -Message.time))

        template_values = {
            "user": user,
            "student": student,
            "messages": messages,
            "size": len(messages)
        }

        self.response.write(template.render(template_values))

    def post(self):

        if self.request.get("message").strip() == "":
            user = self.request.cookies.get("CurrentUser")
            self.redirect("/chat")

        else:
            user = self.request.cookies.get("CurrentUser")

            message = Message(time=datetime.datetime.now(),
            content=self.request.get("message"),
            sender=getAccount(user, userList),
            receiver=getAccount(self.request.cookies.get("receiver"),
            userList))

            message.put()
            time.sleep(1)
            self.redirect("/chat")
