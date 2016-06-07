import requests
import hashlib
import os
import time
# get parsers functions
from parseHtml import proccessHome, proccessSchedule, proccessBedsheet, proccessScores

# GOBAL CONSTANT
SITE_ROOT = 'http://admisiones.unimagdalena.edu.co/mEstudiantes/'
URL_LOGIN = SITE_ROOT+'/ajaxPages/validarLoginEst.jsp'
URL_PHOTO = 'http://admisiones.unimagdalena.edu.co/ayreAdmin/mhe/ajaxPages/fa_downFoto.jsp?id='

# HELPER FUNCTIONS
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
def saveFile(name, content, path):
    with open(path+name, 'wf') as file_:
        file_.write(content.encode('utf8'))

# MAIN FUNCTION, LOGIN
# try login and get the session
# or return error
def main_request(cod, passUn):
    # cod = "2010114040"
    # passUn = "jochechavez123"
    # cod = "2014115021"
    # passUn = "nacielguillermo123"

    password = hashlib.md5(passUn).hexdigest().upper() #encode passs
    payload = "user="+cod+"&password="+password

    s = requests.session()
    lg = s.post(URL_LOGIN, params=payload)

    res = lg.text.strip()

    print res;
    if res != "1":
        return res
    else:
        return req_services(s, cod)

def req_services(s, cod):
    # create folder for cod
    PATH = 'res/'+cod+'/'
    createFolder(PATH)

    result = {};

    # PHOTO SAVE
    start = time.time()
    tt = s.get(URL_PHOTO+cod) # get
    print('get image: '+str(time.time() - start))

    start = time.time()
    with open(PATH+cod+'_photo.jpg', 'wb') as f: # save
                f.write(tt.content)
    print('save image: '+str(time.time() - start))

    # HOME
    start = time.time()
    tt = s.get(SITE_ROOT+'inicio.jsp') # get
    print('home get: '+str(time.time() - start))

    start = time.time()
    saveFile(cod+'_inicio.html', tt.text, PATH) # save
    print('home save: '+str(time.time() - start))

    start = time.time()
    result['personal'] = proccessHome(tt.text, cod) # append
    print('home parse: ' + str(time.time() - start))

    # SCHEDULE
    start = time.time()
    tt = s.get(SITE_ROOT+'miHorario.jsp') # get
    print('schedule get: '+str(time.time() - start))

    start = time.time()
    saveFile(cod+'_miHorario.html', tt.text, PATH) # save
    print('schedule save: '+str(time.time() - start))

    start = time.time()
    result['schedule'] = proccessSchedule(tt.text, cod) # append
    print('schedule parse: '+str(time.time() - start))

    # SCORES
    start = time.time()
    tt = s.get(SITE_ROOT+'miNotas.jsp') # get
    print('scores get: '+str(time.time() - start))

    start = time.time()
    saveFile(cod+'_miNotas.html', tt.text, PATH) # save
    print('scores save: '+str(time.time() - start))

    start = time.time()
    result['scores'] = proccessScores(tt.text, cod) # append
    print('scores parse: '+str(time.time() - start))

    # BEDSHEET
    start = time.time()
    tt = s.get(SITE_ROOT+'miSabana.jsp') # get
    print('bedsheet get: '+str(time.time() - start))

    start = time.time()
    saveFile(cod+'_miSabana.html', tt.text, PATH) # save
    print('betsheet save: '+str(time.time() - start))

    start = time.time()
    result['bedsheet'] = proccessBedsheet(tt.text, cod) # append
    print('bedsheet parse: '+str(time.time() - start))

    return result
