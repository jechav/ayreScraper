from bs4 import BeautifulSoup
import pprint


# HELPER FUNCTION
def g_parse(txt, sw=False):
    tmp = txt.encode("utf-8").lstrip().rstrip()
    if(sw):
        return tmp.split(':')[1].lstrip()
    return  tmp

# HOME PROCCESS
def proccessHome(html, cod):
    soup = BeautifulSoup(html, 'html.parser')
    tbs = soup.findAll('table', {'class': 'tbDatos'})

    datosPersonales = tbs[0]
    Anomalias = tbs[1]

    json_personal = {"CODEST":"-", "NOMBRES":"-", "NUMERO_DOCUMENTO":"-",
                     "SEXO":"-", "EDAD":"-", "ESTRATO":"-", "CELULAR":"-",
                     "TELEFONO":"-", "FECHA_NACIMIENTO":"-", "EMAIL":"-",
                     "EMAIL_INST":"-", "CIUDADORIGEN":"-", "CIUDADRESIDENCIA":"-",
                     "COLEGIO":"-", "DECIMO":"-", "PENSION_10":"-",
                     "UNDECIMO":"-", "PENSION_11":"-"}

    json_personal['CODEST'] = cod

    arry = datosPersonales.findAll('td', {'class': 'tbDatostd'})
    ott  = Anomalias.findAll('td', {'class': 'tbDatostd'})

    json_personal['NOMBRES'] = g_parse( arry[0].getText(), True )
    json_personal['NUMERO_DOCUMENTO'] = g_parse( arry[1].getText(), True )
    json_personal['SEXO'] = g_parse( arry[2].getText(), True )
    json_personal['EDAD'] = g_parse( arry[3].getText(), True )[:2]
    json_personal['ESTRATO'] = g_parse( arry[4].getText(), True )
    json_personal['CELULAR'] = g_parse( arry[5].getText(), True  )
    json_personal['TELEFONO'] = g_parse( arry[6].getText(), True  )
    json_personal['FECHA_NACIMIENTO'] = g_parse( arry[8].getText(), True )
    json_personal['EMAIL'] = g_parse( arry[12].getText() )
    json_personal['EMAIL_INST'] = g_parse( arry[14].getText() )
    json_personal['CIUDADORIGEN'] = g_parse( arry[16].getText() )
    json_personal['CIUDADRESIDENCIA'] = g_parse( arry[18].getText() )
    json_personal['COLEGIO'] = g_parse( arry[22].getText() )
    json_personal['DECIMO'] = g_parse( arry[23].getText(), True )
    json_personal['PENSION_10'] = g_parse( arry[24].getText(), True )
    json_personal['UNDECIMO'] = g_parse( arry[25].getText(), True )
    json_personal['PENSION_11'] = g_parse( arry[26].getText(), True )

    json_personal['ANOMALIAS'] = g_parse( ott[0].getText(), True )

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json_personal)

    return json_personal

# PROCCESS SCHEDULE

