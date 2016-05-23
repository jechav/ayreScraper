import requests
import hashlib
import os
from parseHtml import proccessHome, proccessSchedule # get parsers functions

SITE_ROOT = 'http://admisiones.unimagdalena.edu.co/mEstudiantes/'
URL_LOGIN = SITE_ROOT+'/ajaxPages/validarLoginEst.jsp'
URL_PHOTO = 'http://admisiones.unimagdalena.edu.co/ayreAdmin/mhe/ajaxPages/fa_downFoto.jsp?id='

# cod = "2010114113"
# passUn = "andres1082247313"
# cod = "2010114040"
# passUn = "jochechavez123"
# cod = "2014115021"
# passUn = "nacielguillermo123"
cod = "2010114025"
passUn = "93011910017abachadi"

password = hashlib.md5(passUn).hexdigest().upper() #encode passs
payload = "user="+cod+"&password="+password

s = requests.session()
lg = s.post(URL_LOGIN, params=payload)
print lg.text


# create folder
def createFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)

PATH = 'res/'+cod+'/'
createFolder(PATH)


def saveFile(name, content):
    with open(PATH+name, 'wf') as file_:
        file_.write(content.encode('utf8'))

# photo
tt = s.get(URL_PHOTO+cod)
with open(PATH+cod+'_photo.jpg', 'wb') as f:
        f.write(tt.content)

# home
tt = s.get(SITE_ROOT+'inicio.jsp')
saveFile(cod+'_inicio.html', tt.text)
proccessHome(tt.text, cod)

# schedule
tt = s.get(SITE_ROOT+'miHorario.jsp')
HTML_SCHEDULE= tt.text
saveFile(cod+'_miHorario.html', HTML_SCHEDULE)
proccessSchedule(tt.text, cod)

# scores
tt = s.get(SITE_ROOT+'miNotas.jsp')
HTML_SCORE = tt.text
saveFile(cod+'_miNotas.html', HTML_SCORE)

# bedsheet
tt = s.get(SITE_ROOT+'miSabana.jsp')
HTML_BEDSHEET = tt.text
saveFile(cod+'_miSabana.html', HTML_BEDSHEET)
