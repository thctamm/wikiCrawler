from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import master
import articlesearch as AS
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/wiki/<source>/<target>")
@cross_origin()
def wiki(source, target):
    res = master.main(source, target)
    print("wiki: " + str(res))
    return jsonify(**res)

@app.route("/views/")
@cross_origin()
def views():
    res = {}
    res["hillary"] = hillaryViews()
    res["trump"] = trumpViews()
    print("views: " + str(res))
    return jsonify(**res)

@app.route("/articles/<source>")
@cross_origin()
def articles(source):
    res = {}
    res["hillary"] = hillaryArticles(source)
    res["trump"] = trumpArticles(source)
    print("articles: " + str(res))
    return jsonify(**res)

if __name__ == "__main__":
    app.run()
