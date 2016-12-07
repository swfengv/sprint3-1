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
