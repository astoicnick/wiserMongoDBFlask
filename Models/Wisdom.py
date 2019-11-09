from mongoengine import *

class Wisdom(Document):

    meta = {
        'collection': 'Wisdom'
    }
    isUpvoted = BooleanField(default=True, db_field="is_upvoted",required=True)
    content = StringField(min_length=7, required=True)
    authorID = ObjectIdField(required=True)