from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import requests
import unmock

def fetchSpotifyArtist():
    opts = unmock.init(ignore=["headers", "story"])
    # opts.save = True # For saving mocked response to local
    response = requests.get("https://api.spotify.com/v1/artists")  # will be mocked
    unmock.reset()
    return response

def fetchSpotifyTracks():
    opts = unmock.init(ignore=["headers", "story"])
    # opts.save = True # For saving mocked response to local
    response = requests.get("https://api.spotify.com/v1/tracks")  # will be mocked
    unmock.reset()
    return response

def fetchSpotifyPlaylists():
    opts = unmock.init(ignore=["headers", "story"])
    # opts.save = True # For saving mocked response to local
    response = requests.get("https://api.spotify.com/v1/browse/featured-playlists")  # will be mocked
    unmock.reset()
    return response

app = Flask(__name__)
api = Api(app)

class Artists(Resource):
    def get(self):
        response = fetchSpotifyArtist()
        return response.json()

class Tracks(Resource):
    def get(self):
        response = fetchSpotifyTracks()
        return response.json()

class Playlists(Resource):
    def get(self):
        response = fetchSpotifyPlaylists()
        return response.json()

api.add_resource(Artists, '/artists')
api.add_resource(Tracks, '/tracks')
api.add_resource(Playlists, '/playlists')

if __name__=="__main__":
    app.run(port="5000")
