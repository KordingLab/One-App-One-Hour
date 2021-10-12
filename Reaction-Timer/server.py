
from flask import Flask, jsonify, request, render_template
import json
import time
import glob

App = Flask(__name__)

@App.route("/stats")
def stats():
    data_files = glob.glob("results/data-*.json")
    data = [json.load(open(d, 'r')) for d in data_files]
    return jsonify({"data": data})


@App.route("/upload-data", methods=["POST"])
def upload_data():
    json.dump(
        request.json,
        open(f"results/data-{time.time()}.json", 'w')
    )
    return jsonify({
        "successful": "yes!"
    })


@App.route("/")
def homepage():
    return render_template("index.html")



App.run(debug=True)
