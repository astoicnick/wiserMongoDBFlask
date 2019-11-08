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
    return str(Wisdom.objects(id = wisdomToSave.id).first().id)
@app.route('/wisdom/details', methods=['GET'])
def getSingleWisdom():
    id = request.args.get('id', type = str)
    return Wisdom.objects(id = id).first().content
@app.route('/wisdom/update', methods=['PUT'])
def updateWisdom():
    wisdomUpdateModel = request.get_json()
    wisdomToFindId = wisdomUpdateModel['id']
    Wisdom.objects(id = wisdomToFindId).update(
        content = wisdomUpdateModel['content'],
        author = wisdomUpdateModel['author']
    )
    return  Wisdom.objects(id = wisdomToFindId).first().content
if __name__ == "__main__":
    app.run(debug=True,port=8080)