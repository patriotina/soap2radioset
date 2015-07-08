__author__ = 'patriot'
from app import app
from flask import render_template
import soaprkn

@app.route('/')
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



