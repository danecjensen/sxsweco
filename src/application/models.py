"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb, db


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class Sign(db.Model):
  home = db.IntegerProperty()
  date = db.IntegerProperty()
  refrigerator1 = db.StringProperty()
  use = db.StringProperty()
  air1 = db.StringProperty()
  bathroom1 = db.StringProperty()
  bedroom1 = db.StringProperty()
  dishwasher1 = db.StringProperty()
  microwave1 = db.StringProperty()
  gen = db.StringProperty()
  livingroom1 = db.StringProperty()
  oven1 = db.StringProperty()
