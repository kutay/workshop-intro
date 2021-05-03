from flask import Flask
from flask import abort, redirect, url_for, render_template
from flask import request

# https://flask.palletsprojects.com/en/1.1.x/quickstart/
app = Flask(__name__)

# Page d'accueil du site. 
# Par exemple : http://127.0.0.1:5000/
@app.route('/')
def home():
    # On ne fait rien de spécial, on va juste retourner le contenu html du template home.html
    # Voir templates/home.html
    return render_template('home.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    # On affiche dans la console le message écrit par l'utilisateur
    
    print(request.form['message'])

    # TODO extraire le message et l'enregistrer en base de données

    # Une fois le traitement terminé, on redirige vers la page d'accueil
    return redirect(url_for('home'))
