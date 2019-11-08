from mongoengine import *
from flask import Flask, request

from Models.Wisdom import Wisdom

connect('Wiser')

app = Flask(__name__)

@app.route('/wisdom/create', methods=['POST'])
def createWisdom():
    wisdomAsJson = request.get_json()
    wisdomToSave = Wisdom()
    wisdomToSave.content = wisdomAsJson['content']
    wisdomToSave.author = wisdomAsJson['author']
    wisdomToSave.save()
    wisdomToSave.isUpvoted = True
    wisdomToSave.save()
    return str(len(Wisdom.objects(id = wisdomToSave.id)))

if __name__ == "__main__":
    app.run(debug=True,port=8080)