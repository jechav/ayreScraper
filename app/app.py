#!flask/bin/python
from flask import Flask, jsonify, request, make_response, render_template
from requestAyre import main_request # get parsers functions

application = Flask(__name__)
application.debug = True

def r_error(err):
        return make_response(jsonify({'error': err}), 400)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.form or not 'cod' in request.form or not 'password' in request.form:
            return r_error('Bad request')
        else:
            res = main_request(request.form['cod'], request.form['password'])
            if isinstance(res, dict):
                return jsonify( res )
            else:
                return r_error(res);

    else:
        return render_template('index.html');


if __name__ == '__main__':
    application.run(host='0.0.0.0')
