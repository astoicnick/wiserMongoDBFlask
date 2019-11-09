from datetime import datetime

import flask
from mongoengine import *

from flask import Flask, request, jsonify

from Models.Author import Author
from Models.Wisdom import Wisdom

import requests

connect('Wiser')

app = Flask(__name__)
# Create
@app.route('/wisdom/create', methods=['POST'])
def createWisdom():
    wisdomAsJson = request.get_json()
    wisdomToSave = Wisdom()
    wisdomToSave.content = wisdomAsJson['content']
    wisdomToSave.authorID = wisdomAsJson['authorID']
    wisdomToSave.save()
    wisdomToSave.save()
    return str(Wisdom.objects(id = wisdomToSave.id).first().id)
# Read - Detail
@app.route('/wisdom/details', methods=['GET'])
def getSingleWisdom():
    id = request.args.get('id', type = str)
    return Wisdom.objects(id = id).first().content

# Read - List
@app.route('/wisdom/list', methods=['GET'])
def getAllWisdom():
    # res = flask.Response()
    # res.headers['Content-Type:'] = "json"
    # res.set_data(Wisdom.objects.to_json())
    return Wisdom.objects.to_json()
 # Mudkip - used for comparison with .NET Core
@app.route('/mudkip')
def getMudkip():
    return requests.get("https://pokeapi.co/api/v2/pokemon/mudkip").json()
# Update
@app.route('/wisdom/update', methods=['PUT'])
def updateWisdom():
    wisdomUpdateModel = request.get_json()
    wisdomToFindId = wisdomUpdateModel['id']
    Wisdom.objects(id = wisdomToFindId).update(
        content = wisdomUpdateModel['content'],
        author = wisdomUpdateModel['author']
    )
    return  Wisdom.objects(id = wisdomToFindId).first().content
# Delete
@app.route('/wisdom/delete', methods=['DELETE'])
def deleteWisdom():
    idToSearchBy = request.args.get('id')
    wisdomToDelete = Wisdom.objects(id = idToSearchBy).delete()
    return "Your document was deleted"

###
###
###

# Create
@app.route('/author/create', methods=['POST'])
def createAuthor():
    jsonAuthorToSave = request.get_json()
    authorToSave = Author()
    authorToSave.Name = jsonAuthorToSave['Name']
    # authorToSave.Virtue = 0
    # authorToSave.DateCreated = datetime.now()
    authorToSave.save()
    return str(Author.objects(Name= authorToSave.Name).first().id)
# Read - Detail
@app.route('/author/detail', methods=['GET'])
def getSingleAuthor():
    id = request.args.get('id', type = str)
    return Author.objects(id = id).first().to_json()
# Read - List
@app.route('/author/list', methods=['GET'])
def getAllAuthors():
    return Author.objects.to_json()
# Link - Wisdom to Author
@app.route('/author/wisdom', methods=['GET'])
def getAuthorsWisdom():
    return Wisdom.objects(authorID=request.args.get('id', type=str)).first().to_json()
# Update
@app.route('/author/update', methods=['PUT'])
def updateAuthor():
    jsonAuthorToUpdate = request.get_json()
    authorID = jsonAuthorToUpdate['id']
    Author.objects(id = authorID).update(
        Name = jsonAuthorToUpdate['Name']
    )
    return  Author.objects(id = authorID).to_json()
# Delete
@app.route('/author/delete', methods=['DELETE'])
def deleteAuthor():
    return str(Author.objects(id = request.args.get('id', type = str)).delete())

if __name__ == "__main__":
    app.run(debug=True,port=8080)