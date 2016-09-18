from flask import Flask, jsonify
import master
app = Flask(__name__)

@app.route("/<source>/<target>")
def find(source, target):
        res = master.main(source, target)
        print(res)
        return jsonify(**res)

if __name__ == "__main__":
        app.run()
