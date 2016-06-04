import requests
import hashlib
import os
from parseHtml import proccessHome, proccessSchedule # get parsers functions

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

    # cod = "2010114113"
    # passUn = "andres1082247313"
    # cod = "2010114040"
    # passUn = "jochechavez123"
    # cod = "2014115021"
    # passUn = "nacielguillermo123"
    # cod = "2010114025"
    # passUn = "93011910017abachadi"

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
    # PATH = '/res/'+cod+'/'
    # createFolder(PATH)

    result = {};

    # photo save
    # tt = s.get(URL_PHOTO+cod)
    # with open(PATH+cod+'_photo.jpg', 'wb') as f:
                # f.write(tt.content)

    # home
    tt = s.get(SITE_ROOT+'inicio.jsp')
    # saveFile(cod+'_inicio.html', tt.text, PATH)
    result['personal'] = proccessHome(tt.text, cod)

    # schedule
    tt = s.get(SITE_ROOT+'miHorario.jsp')
    # saveFile(cod+'_miHorario.html', tt.text, PATH)
    result['schedule'] = proccessSchedule(tt.text, cod)

    # # scores
    # tt = s.get(SITE_ROOT+'miNotas.jsp')
    # saveFile(cod+'_miNotas.html', tt.text, PATH)

    # # bedsheet
    # tt = s.get(SITE_ROOT+'miSabana.jsp')
    # saveFile(cod+'_miSabana.html', tt.text, PATH)

    return result
