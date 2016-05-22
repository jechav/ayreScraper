import requests
import hashlib
from bs4 import BeautifulSoup
from parseHtml import * # get parsers functions

SITE_ROOT = 'http://admisiones.unimagdalena.edu.co/mEstudiantes/'
URL_LOGIN = SITE_ROOT+'/ajaxPages/validarLoginEst.jsp'
URL_PHOTO = 'http://admisiones.unimagdalena.edu.co/ayreAdmin/mhe/ajaxPages/fa_downFoto.jsp?id='

cod = "2010114113"
passUn = "andres1082247313"
password = hashlib.md5(passUn).hexdigest().upper() #encode passs

payload = "user="+cod+"&password="+password

s = requests.session()
lg = s.post(URL_LOGIN, params=payload)
# print lg.text

def saveFile(name, content):
    with open(name, 'wf') as file_:
        file_.write(content.encode('utf8'))

# photo
tt = s.get(URL_PHOTO+cod)
with open(cod+'_photo.jpg', 'wb') as f:
        f.write(tt.content)

# home
tt = s.get(SITE_ROOT+'inicio.jsp')
saveFile(cod+'_inicio.html', tt.text)
proccessHome(tt.text, cod)

# schedule
tt = s.get(SITE_ROOT+'miHorario.jsp')
HTML_SCHEDULE= tt.text
saveFile(cod+'_miHorario.html', HTML_SCHEDULE)

# scores
tt = s.get(SITE_ROOT+'miNotas.jsp')
HTML_SCORE = tt.text
saveFile(cod+'_miNotas.html', HTML_SCORE)

# bedsheet
tt = s.get(SITE_ROOT+'miSabana.jsp')
HTML_BEDSHEET = tt.text
saveFile(cod+'_miSabana.html', HTML_BEDSHEET)
