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

userList = []

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
autoescape=True)

def parseUserString(string):
    subStr = string

    while subStr != "":
        userName = subStr[:subStr.find(",")].strip() # We assume that the string does not begin with a comma
        
        #if list(User.query(User.Name == userName)) != 0:
        #    return
            
        #print("Loop")

        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        accountName = userPassword = subStr[:subStr.find(",")].strip() # Get data
        
        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        userPassword = subStr[:subStr.find(",")].strip() # Get data
        
        subStr = subStr[subStr.find(",") + 1:] # Move the sub string forward
        account = subStr[:subStr.find(",")].strip() # Get data
        
        user = User() # Create the user
        
        user.Name = userName
        user.userName = accountName
        user.password = userPassword
        user.aType = account
        
        user.put() # Put to the data store
        subStr = subStr[subStr.find("\n") + 1:] # Equivalent to readline, this just moves to the next line of text

def getAccount(userName):
    user = User.query(User.Name == userName).get()
    print(user)
    
    return user
    
def getInstrAccount(uList):
    for i in range(len(uList)):
        if uList[i].aType == "i":
            return uList[i]
