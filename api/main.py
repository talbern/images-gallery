import requests
from flask import Flask, request

UNSPLASH_URL="https://api.unsplash.com/photos/random"
UNSPLASH_KEY="ER7s-ax3ucCu4Ubi_4S1zOcFJNIiyLnmVkdOFUBWJtY"

app = Flask(__name__)

@app.route("/new-image")
def new_image():
    word = request.args.get("query")
    
    headers = {
      "Accept-Version": "v1",
      "Authorization": "Client-ID %s" % UNSPLASH_KEY
    }
    params = {
      "query": word
    }
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return data
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)
  