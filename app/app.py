#!flask/bin/python
from flask import Flask, jsonify, request, make_response, render_template
from requestAyre import main_request # get parsers functions

application = Flask(__name__)
application.debug = True

def r_error(err):
    if err == 400:
        return make_response(jsonify({'error': 'No found'}), err)
    else:
        return make_response(jsonify({'error': 'Bad request'}), err)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not request.form or not 'cod' in request.form or not 'password' in request.form:
            return r_error(500)
        else:
            return jsonify({'student': main_request(request.form['cod'], request.form['password'])})
            # return 'Valid  request: '+request.form['cod']+' pass: '+request.form['password']
    else:
        return render_template('index.html');

# @application.route('/ayre/api/v1/task/', methods=['GET'])
# def getTasks():
    # return jsonify({'tasks': tasks})

if __name__ == '__main__':
    application.run(host='0.0.0.0')
