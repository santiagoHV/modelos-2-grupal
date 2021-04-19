from flask import Flask, render_template, request, redirect, url_for
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano
from intro.poo.decorators.armour_decorator import ArmourDecorator
from intro.poo.decorators.helmet_decorator import HelmetDecorator
from intro.poo.decorators.hammer_decorator import HammerDecorator

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
    personajes_creados[id_aed].is_attacked(personajes_creados[id_atk].attack)
    return redirect(f'/ataque/{id_atk}')


@app.route('/decorar/<decorador>/<int:id_decorado>')
def decorar(decorador, id_decorado):
    if decorador == 'armadura':
        personajes_creados[id_decorado] = ArmourDecorator(personajes_creados[id_decorado]).character
    elif decorador == 'martillo':
        personajes_creados[id_decorado] = HammerDecorator(personajes_creados[id_decorado]).character
    elif decorador == 'casco':
        personajes_creados[id_decorado] = HelmetDecorator(personajes_creados[id_decorado]).character

    return redirect(f'/ataque/{id_decorado}')


@app.route('/selected', methods=['POST'])
def select():
    return redirect('/' + request.json['id'])


if __name__ == '__main__':
    app.run(debug=True)
