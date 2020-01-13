from flask import Flask
from flask import jsonify
from flask import render_template
from .modules import test_module

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    test_module.test_func('abc')
    return jsonify({
    "message": "テスト"
    })


@app.route(('/template'))
@app.route(('/template/<username>'))
def template(username=None):
    return render_template('base.html', username=username)

def main():
    app.debug = True
    app.run(host='0.0.0.0', port=5500)
    # app.run()

if __name__ == '__main__':
    main()
