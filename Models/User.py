from mongoengine import *

class User(Document):

    meta = {
        'collection': 'Users'
    }
    Virtue = BooleanField(default=True, db_field="is_upvoted",required=True)
    Name = StringField(required=True,default=None)
    Username = StringField(unique=True,required=True)
    Password = StringField(min_length=8)
