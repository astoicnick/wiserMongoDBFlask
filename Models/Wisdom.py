from mongoengine import *

class Wisdom(Document):

    meta = {
        'collection': 'Wisdom'
    }
    wisdomID = ObjectIdField()
    isUpvoted = BooleanField(default=True, db_field="is_upvoted",required=True)
    content = StringField(min_length=7, required=True)
    author = StringField(min_length=1, required=True)