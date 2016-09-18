from flask import Flask, jsonify
from flask.ext.cors import CORS, cross_origin
import master
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/<source>/<target>")
@cross_origin()
def find(source, target):
        res = master.main(source, target)
        print(res)
        return jsonify(**res)

if __name__ == "__main__":
        app.run()
