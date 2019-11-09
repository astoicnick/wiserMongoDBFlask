from datetime import datetime

from mongoengine import *

class Author(Document):

    meta = {
        'collection': 'Authors'
    }
    Virtue = IntField(required=True, default=0)
    DateCreated = DateTimeField(required=True, default=datetime.now())
    Name = StringField(min_length=1, required=True)
    Wisdom = ListField(required=True,default={})