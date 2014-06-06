import json
from flask import abort, Flask, render_template


farm = Flask('farm')

@farm.route('/')
def default():
    beds = [json.load(open("data/2014/bed-one.json")),
            json.load(open("data/2014/bed-two.json"))]
    return render_template('index.html',
                           beds=beds)

if __name__ == '__main__':
    farm.run(
          host='0.0.0.0',
          port=9560,
          debug=True)
