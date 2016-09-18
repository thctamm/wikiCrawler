from flask import Flask
import master
app = Flask(__name__)

@app.route("/<source>/<target>")
def find(source, target):
        return master.main(source, target)

if __name__ == "__main__":
        app.run()
