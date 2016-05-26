#!flask/bin/python
from flask import Flask, jsonify, request, make_response
from requestAyre import main_request # get parsers functions

app = Flask(__name__)

def r_error(err):
    if err == 400:
        return make_response(jsonify({'error': 'No found'}), err)
    else:
        return make_response(jsonify({'error': 'Bad request'}), err)

@app.route('/')
def index():
    return "Ayre Scraper"+" make request to '/ayre/api/v1/auth/' with params cod, password"

@app.route('/ayre/api/v1/auth/', methods=['POST'])
def auth():
    if not request.form or not 'cod' in request.form or not 'password' in request.form:
        return r_error(500)
    else:
        return jsonify({'student': main_request(request.form['cod'], request.form['password'])})
        # return 'Valid  request: '+request.form['cod']+' pass: '+request.form['password']



# @app.route('/ayre/api/v1/task/', methods=['GET'])
# def getTasks():
    # return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
