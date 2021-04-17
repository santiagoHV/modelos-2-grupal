from flask import Flask, render_template, url_for
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano

app = Flask(__name__)
personajes_creados = [Argoniano('fUmaratto', 180, 200, 19), Ogro('Hurtado', 180, 200, 19), Argoniano('Santiago', 180, 200, 19), Argoniano('Ebratt', 180, 200, 19)]
personaje_activo = personajes_creados[0]

@app.route('/')
def hello_world():
    return render_template('index.html', personajes = personajes_creados)

if __name__ == '__main__':
    app.run(debug=True)