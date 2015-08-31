__author__ = 'patriot'
from app import app
from flask import render_template
import soaprkn

@app.route('/')
@app.route('/index2')
def index2():
    return render_template("index2.html")

@app.route('/index')
def index():
    user = {'nickname': 'Patriot'}
    dicetskind = soaprkn.getDicETSKind()
    dicetstype = soaprkn.getDicETSType()
    dicrsnparts = soaprkn.getDicRSNParts()
    dicsectortype = soaprkn.getDicSectorType()
    poltypelist = soaprkn.getDicPolarization()
    dicradclass = soaprkn.getDicRadClass()
    return render_template("index.html",
                           title = 'SOAP MF',
                           user = user,
                           etskindlist = dicetskind[0],
                           dicetstype = dicetstype[0][0],
                           dicrsnparts = dicrsnparts[0],
                           dicsectortype = dicsectortype[0],
                           poltypelist = poltypelist[0],
                           dicradclass = dicradclass[0])

@app.route('/dic-ets')
def dicEts():
    user = {'nickname': 'Patriot'}
    dicetskind = soaprkn.getDicETSKind()
    return render_template("dic-ets.html",
                           title = 'SOAP MF',
                           user = user,
                           etskindlist = dicetskind[0])

@app.route('/dic-etstype')
def dicEtsType():
    user = {'nickname': 'Patriot'}
    dicetstype = soaprkn.getDicETSType()
    return render_template("dic-etstype.html",
                           title = 'SOAP MF',
                           user = user,
                           dicetstype = dicetstype[0][0])

@app.route('/dic-rsnparts')
def dicRsnParts():
    user = {'nickname': 'Patriot'}
    dicrsnparts = soaprkn.getDicRSNParts()
    return render_template("dic-rsnparts.html",
                           title = 'SOAP MF',
                           user = user,
                           dicrsnparts = dicrsnparts[0])

@app.route('/dic-sectortype')
def dicSetorType():
    user = {'nickname': 'Patriot'}
    dicsectortype = soaprkn.getDicSectorType()
    return render_template("dic-sectortype.html",
                           title = 'SOAP MF',
                           user = user,
                           dicsectortype = dicsectortype[0])

@app.route('/dic-polartype')
def dicPolarType():
    user = {'nickname': 'Patriot'}
    poltypelist = soaprkn.getDicPolarization()
    return render_template("dic-polartype.html",
                           title = 'SOAP MF',
                           user = user,
                           poltypelist = poltypelist[0])

@app.route('/dic-radclass')
def dicRadClass():
    user = {'nickname': 'Patriot'}
    dicradclass = soaprkn.getDicRadClass()
    return render_template("dic-radclass.html",
                           title = 'SOAP MF',
                           user = user,
                           dicradclass = dicradclass[0])

@app.route('/registration')
def regform():
    dicetskind = soaprkn.getDicETSKind()
    dicetstype = soaprkn.getDicETSType()
    dicrsnparts = soaprkn.getDicRSNParts()
    dicsectortype = soaprkn.getDicSectorType()
    poltypelist = soaprkn.getDicPolarization()
    dicradclass = soaprkn.getDicRadClass()
    return render_template("registration.html",
                           title = 'SOAP MF',
                           user = user,
                           etskindlist = dicetskind[0],
                           dicetstype = dicetstype[0][0],
                           dicrsnparts = dicrsnparts[0],
                           dicsectortype = dicsectortype[0],
                           poltypelist = poltypelist[0],
                           dicradclass = dicradclass[0])