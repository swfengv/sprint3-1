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
