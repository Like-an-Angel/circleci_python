from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import requests
import unmock

def fetchSpotifyArtist():
    opts = unmock.init(ignore=["headers", "story"])
    # opts.save = True # For saving mocked response to local
    response = requests.get("https://api.spotify.com/v1/browse/featured-playlists")  # will be mocked
    unmock.reset()
    return response.json()

app = Flask(__name__)
api = Api(app)

class Artists(Resource):
    def get(self):
        response = fetchSpotifyArtist()
        print(type(response))
        print(response)
        return jsonify(response)

class Tracks(Resource):
    def get(self):
        pass
        response = fetchSpotifyArtist()
        return jsonify(response)

class Artist_Name(Resource):
    def get(self, artist_id):
        pass
        response = fetchSpotifyArtist()
        return jsonify(response)

api.add_resource(Artists, '/artists')
api.add_resource(Tracks, '/tracks')
api.add_resource(Artist_Name, '/artists/<artist_id>')

if __name__=="__main__":
    app.run(port="5000")
