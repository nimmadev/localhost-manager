from flask import Flask, url_for
from flask import render_template
import yaml

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("config.yaml", "r") as stream:
        try:
            aa = yaml.safe_load(stream)['SITES']
        except yaml.YAMLError as exc:
            return "Fix ur Config"
    return render_template('index.html', data=aa)

app.run(host='0.0.0.0', port=9991)