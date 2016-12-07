import webapp2
import jinja2
import os
import time
import datetime
import calendar
import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from user import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

def parseTxt(name):

    f = open(name,"r")
    st = f.readline()
    result = []

    while st != "":
        if st[:st.find(",")] not in result:

            uName = st[:st.find(",")].strip()

            st = st[st.find(",") + 1:]
            password = st[:st.find(",")].strip()

            st = st[st.find(",") + 1:]
            accnt = st.strip()

            user = User()
            user.name = uName
            user.password = password
            user.aType = accnt

            user.put()
            result.append(user)
            st = f.readline()

    return result
