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

class Lecture(ndb.Model):
    name=ndb.StringProperty()

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

class Question(ndb.Model):
    """stuff here"""

class User(ndb.Model):
    Name = ndb.StringProperty()
    userName = ndb.StringProperty()
    password = ndb.StringProperty()
    aType = ndb.StringProperty()
    #lectures = ndb.StructuredProperty(Lecture, Repeated=True) # Breaks because we don't have Lecture yet

    #def createUser(self):
    #    """stuff here"""
    #def toString(self):
    #    """stuff here"""

class Test(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testTxtName(self):
        self.assertEqual(parseTxt("accounts.txt"), None)

    def testMessageToString(self):
        self.content = "This is a message from Alice"
        self.name = "Alice"
        self.now = datetime.datetime.now()

        self.message = Message(content=self.content, name=self.name, time=self.now)
        self.assertEqual(self.message.toString(), ("(" + self.content + "," + self.name + ","  + str(self.now) + ")"))

    def testLoginCheck(self):
        self.assertEqual(Login.checkName("?"))

class Login(webapp2.RequestHandler):
    def get(self):
        error = ""
        uNm = self.request.cookies.get("CurrentUser")
        uPwd = self.request.get('uPass')
        if self.request.cookies.get("CurrentUser") == None:
            uNm = self.request.get('uName')
        if uNm == "":
            template = JINJA_ENVIRONMENT.get_template('login.html')
            template_values = {
                "user": uNm,
                "error": error
            }
            self.response.write(template.render(template_values))
        else:
            if User.query(User.name == uNm).get().aType == 's':
                self.redirect('/studentcenter')
            else:
                self.redirect('/instructorcenter')

    def post(self):
        validAcc = False
        uNm = self.request.get("uName")
        uPwd = self.request.get('uPass')
        for item in userList:
            if item.getName() == uNm and item.getPwd() == uPwd:
                validAcc = True
        if validAcc == False:
            self.redirect("/")
        if validAcc == True:
            self.response.set_cookie("CurrentUser", uNm, max_age=100, path="/")
            if (getAccount(uNm, userList).getaType() == 's'):
                self.redirect("/studentcenter")
            else:
                self.redirect("/instructorcenter")
        else:
            error = "enter a valid username and password"

    def checkName(self, name):
        if "?" in name or "&" in name or "+" in name:
            return False

        return True

class InstructorCenter(webapp2.RequestHandler):
    def get(self):
        uNm = self.request.cookies.get('CurrentUser')
        instructor = User.query(User.name == uNm).get()
        QL = []
        QL.append(Question.query(Question.lec == 'cs361').fetch())
        template = JINJA_ENVIRONMENT.get_template('insc.html')
        uNm = self.request.get("CurrentUser")#probably pointless
        template_values = {
            "CurrentUser": uNm,
            'QL': QL,
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

class StudentCenter(webapp2.RequestHandler):
   def get(self):
       uNm = self.request.cookies.get("CurrentUser")
       #unm is null
       template = JINJA_ENVIRONMENT.get_template('stdc.html')
       QL = []
       QL.append((list)(Question.query(Question.owner==uNm).fetch()))

       template_values = {
           "uNm" : uNm,
           "QL" : QL,
       }

       self.response.write(template.render(template_values))

   def post(self):
      question = Question()
      question.owner= self.request.cookies.get("CurrentUser")
      question.topic = self.request.get("topic")
      question.content = self.request.get("content")
      question.lec = self.request.get("class")
      print(self.request.get("class"))
      question.time = datetime.datetime.now()
      question.answered= False
      question.message=[]

      question.put()
      self.redirect("/studentcenter")

class Logout(webapp2.RequestHandler):
    """stuff here"""

class FAQ(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('faq.html')
        user = self.request.cookies.get("CurrentUser")

        faqs = list(questionAnswer.query().order(questionAnswer.heading, -questionAnswer.heading))

        template_values = {
            "user": getAccount(user, userList),
            "faqs": faqs
        }

        self.response.write(template.render(template_values))

    def post(self):

        if self.request.get("heading") == "" or self.request.get("question") == "" or self.request.get("answer") == "":
            user = self.request.cookies.get("CurrentUser")
            self.redirect("/messcenter?user=" + user)

        else:

            qa = questionAnswer(heading=self.request.get("heading"), question=self.request.get("question"), answer=self.request.get("answer"))
            qa.put()

            user = self.request.cookies.get("CurrentUser")
            self.redirect("/messcenter?user=" + user)

class AdminPage(webapp2.RequestHandler):
    """stuff here"""

class Chat(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('chat.html')

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
