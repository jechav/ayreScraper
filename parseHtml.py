from bs4 import BeautifulSoup
import pprint


# HELPER FUNCTION
def g_parse(txt, sw=False):
    tmp = txt.encode("utf-8").lstrip().rstrip().replace('\xc2\xa0', '')
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

    # return json_personal

# PROCCESS SCHEDULE
def proccessSchedule(html, cod):
    json_horario = []
    pp = pprint.PrettyPrinter(indent=4)

    # debug get html from file
    # with open('res/'+cod+'/'+cod+'_miHorario.html', 'r') as f:
        # html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    # print soup.prettify()
    tbs = soup.findAll('table', {'class': 'tbHorario'})

    ftab = tbs[0].findAll('tr', {'class': 'horario1'})  #first table
    ftabP = tbs[1].findAll('tr', {'class': 'horario1'}) #second table, places
    for ind, assig in enumerate(ftab):
        tmp = {"TIPO_REGISTRO": "NORMAL",
                "LUNES": "-",
                "ASIGNATURA": "-",
                "MIERCOLES": "-",
                "SABADO": "-",
                "JUEVES": "-",
                "CODMAT": "-",
                "DOCENTE": "",
                "VIERNES": "-",
                "MARTES": "-",
                "DOMINGO": "-",
                "TIPO_ASIGNATURA": "REGULAR",
                "NUM": str(ind+1),
                "GRUPO": "-"}
        tds = assig.findAll('td')
        tdsplaces = ftabP[ind].findAll('td')
        # print tdsplaces
        for j, mat in enumerate(tds):
            if(j == 0):
                tmp["ASIGNATURA"] = g_parse(mat.getText())
                continue
            if(j == 1):
                tmp["DOCENTE"] = g_parse(mat.getText())
                continue
            if(j == 2):
                tmp["GRUPO"] = g_parse(mat.getText())
                continue
            #days
            if(j == 3):
                passed = g_parse(tdsplaces[0].getText())
                if(passed == 'vacacional'):
                    tmp["LUNES"] =  '-'
                    tmp["TIPO_REGISTRO"] = 'OTRO'
                    tmp["TIPO_ASIGNATURA"] = 'OTRO'
                else:
                    if(passed != '-'):
                        tmp["LUNES"] =  g_parse(tdsplaces[0].contents[0])+g_parse(tdsplaces[0].contents[1])
                    else:
                        tmp["LUNES"] =  passed
                continue
            if(j == 4):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["MARTES"] =  g_parse(tdsplaces[1].contents[0])+g_parse(tdsplaces[1].contents[1])
                else:
                    tmp["MARTES"] =  passed
                continue
            if(j == 5):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["MIERCOLES"] =  g_parse(tdsplaces[2].contents[0])+g_parse(tdsplaces[2].contents[1])
                else:
                    tmp["MIERCOLES"] =  passed
                continue
            if(j == 6):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["JUEVES"] =  g_parse(tdsplaces[3].contents[0])+g_parse(tdsplaces[3].contents[1])
                else:
                    tmp["JUEVES"] =  passed
                continue
            if(j == 7):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["VIERNES"] =  g_parse(tdsplaces[4].contents[0])+g_parse(tdsplaces[4].contents[1])
                else:
                    tmp["VIERNES"] =  passed
                continue
            if(j == 8):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["SABADO"] =  g_parse(tdsplaces[5].contents[0])+g_parse(tdsplaces[5].contents[1])
                else:
                    tmp["SABADO"] =  passed
                continue
            if(j == 9):
                passed = g_parse(mat.getText())
                if(passed != '-'):
                    tmp["DOMINGO"] =  g_parse(tdsplaces[6].contents[0])+g_parse(tdsplaces[6].contents[1])
                else:
                    tmp["DOMINGO"] =  passed
                continue
        json_horario.append(tmp)

    pp.pprint(json_horario)
    # return json_horario

# proccessSchedule('', '2010114113')
