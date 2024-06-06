from flask import render_template,session,redirect,request
from models.scrapStagiaires import scrap
from models.scrapMAStage import MAStage
from views import app_views

@app_views.route('/stagiaire',strict_slashes=False)
@app_views.route('/stagiaire/<numPg>',strict_slashes=False)
def stagiaire(numPg=None):
    if 'logged' in session:
        if session['logged']:
            if numPg:
                scr=scrap()
                demandes=scr.demandes(numPage=numPg)
                session['stagiaires']=demandes
                session['fields']=['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']
        return render_template("pages/stagiaire.html",Stagiaires=session['stagiaires'])
    return 'unauthorized'

@app_views.route('/chercher/<site>',methods=['POST'],strict_slashes=False)
def chercherStagiaires(site):
    numPage=request.form.get('pages')
    return redirect('/'+site+'/'+str(numPage))

@app_views.route('/marocAnnonces',strict_slashes=False)
@app_views.route('/marocAnnonces/<numPg>',strict_slashes=False)
def marocAnnonces(numPg=None):
    if 'logged' in session:
        if session['logged']:
            if numPg:
                scr=MAStage()
                demandes=scr.scrapData(numPage=numPg)
                session['marocAnnonces']=demandes
                session['fields']=['Titre', 'Domaine', 'Duree', 'Niveau', 'Lien']
        return render_template("pages/marocAnnonces.html",MarocAnnonces=session['marocAnnonces'])
    return 'unauthorized'