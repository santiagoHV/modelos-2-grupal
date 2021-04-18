from flask import Flask, render_template, url_for
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano

app = Flask(__name__)
personajes_creados = [Imperial('fUmaratto', 180, 200, 19), Breton('Hurtado', 180, 200, 19),
                      Argoniano('Santiago', 180, 200, 19)]
personaje_activo = personajes_creados[0]


@app.route('/')
def personajes():
    return render_template('personajes.html', personajes=personajes_creados, optionnav='personajes')

@app.route('/creador')
def creador():
    return render_template('creador.html', optionnav='creador')

@app.route('/ataque')
def ataque():
    return render_template('ataque.html', personaje=personaje_activo, optionnav='ataque')

if __name__ == '__main__':
    app.run(debug=True)
