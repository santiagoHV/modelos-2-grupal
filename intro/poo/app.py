from flask import Flask, render_template, request, redirect, url_for
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano

app = Flask(__name__)
personajes_creados = [Imperial('fUmaratto', 180, 200, 19), Breton('Hurtado', 180, 200, 19),
                      Argoniano('Santiago', 180, 200, 19), Elfo('otrohpta',180,200,50)]


@app.route('/<int:idx>')
def personajes(idx):
    return render_template('personajes.html', personajes=personajes_creados, optionnav='personajes', idx=idx)


@app.route('/creador/<int:idx>')
def creador(idx):
    return render_template('creador.html', optionnav='creador', idx=idx)


@app.route('/ataque/<int:idx>')
def ataque(idx):
    return render_template('ataque.html', optionnav='ataque', personajes=personajes_creados, idx = idx)


@app.route('/ataque/<int:id_atk>/<int:id_aed>')
def atacar_personaje(id_atk, id_aed):
    print(type(id_aed))
    personajes_creados[id_aed].is_attacked(personajes_creados[id_atk].attack)

    return redirect(f'/ataque/{id_atk}')


@app.route('/selected', methods=['POST'])
def select():
    return redirect('/' + request.json['id'])


if __name__ == '__main__':
    app.run(debug=True)
