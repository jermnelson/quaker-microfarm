from flask import abort, Flask, render_template

farm = Flask('farm')

@farm.route('/')
def default():
    return render_template('index.html')

if __name__ == '__main__':
    farm.run(
          host='0.0.0.0',
          port=9560,
          debug=True)
