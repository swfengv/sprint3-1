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
