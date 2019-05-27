from flask import Flask
import requests
import unmock

def fetchSpotifyArtist():
    # opts = unmock.init(ignore=["headers", "story"])
    # opts.save = True # For saving mocked response to local
    response = requests.get("https://api.spotify.com/v1/artists")  # will be mocked
    # unmock.reset()
    return response

app = Flask(__name__)

if __name__=="__main__":
    app.run()

@app.route("/", methods=['GET','POST'])
def api_inner_get():
    response = fetchSpotifyArtist()
    print(type(response.text))
    return response.text
# 
# @app.route("/", methods=['POST'])
# def api_inner_post():
#     pass
