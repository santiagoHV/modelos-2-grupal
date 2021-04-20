from flask import Flask, render_template, request, redirect, url_for, flash
from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano
from intro.poo.decorators.armour_decorator import ArmourDecorator
from intro.poo.decorators.helmet_decorator import HelmetDecorator
from intro.poo.decorators.hammer_decorator import HammerDecorator

from intro.poo.factory.fabricas import FabricaPersonaje

app = Flask(__name__)
personajes_creados = [Imperial('fUmaratto', 180, 200, 19), Breton('Hurtado', 180, 200, 19),
                      Argoniano('Santiago', 180, 200, 19)]


app.config['SECRET_KEY'] = 'sdasfasf'

def aliarse_grupo(p1, p2):
    p1.add_aliado(p2)
    p2.add_aliado(p1)
    for aliado in p2.aliados:
        if (aliado not in p1.aliados):
            aliarse_grupo(p1, aliado)
    for aliado in p1.aliados:
        if (aliado not in p2.aliados):
            aliarse_grupo(p2, aliado)

def romper_alianza_grupo(p2, p1):
    p1.remove_aliado(p2)
    p2.remove_aliado(p1)
    for aliado in p2.aliados:
        if (aliado in p1.aliados):
            romper_alianza_grupo(aliado, p1)
    for aliado in p1.aliados:
        if (aliado in p2.aliados):
            romper_alianza_grupo(aliado, p2)

@app.route('/<int:idx>')
def personajes(idx):
    return render_template('personajes.html', personajes=personajes_creados, optionnav='personajes', idx=idx)


@app.route('/creador/<int:idx>', methods=['GET', 'POST'])
def creador(idx):
    if request.method == 'POST':
        if not request.form.get('raza_personaje'):
            flash('Raza no ingresada, por favor revisa la información ingresada', category='error')
        elif not request.form.get('nombre_personaje'):
            flash('Nombre no ingresado, por favor revisa la información ingresada', category='error')
        elif not request.form.get('tam_personaje'):
            flash('Tamaño no ingresado, por favor revisa la información ingresada', category='error')
        elif not request.form.get('altura_personaje'):
            flash('Altura no ingresada, por favor revisa la información ingresada', category='error')
        elif not request.form.get('edad_personaje'):
            flash('Edad no ingresada, por favor revisa la información ingresada', category='error')
        else:
            flash('Personaje creado con éxito ✌', category='success')
            personaje_creado = FabricaPersonaje(request.form.get('raza_personaje'),
                                                request.form.get('nombre_personaje'),
                                                request.form.get('tam_personaje'),
                                                request.form.get('altura_personaje'),
                                                request.form.get('edad_personaje')).personaje
            personajes_creados.append(personaje_creado)

    return render_template('creador.html', optionnav='creador', idx=idx)


@app.route('/ataque/<int:idx>')
def ataque(idx):
    return render_template('ataque.html', optionnav='ataque', personajes=personajes_creados, idx=idx)


@app.route('/ataque/<int:id_atk>/<int:id_aed>')
def atacar_personaje(id_atk, id_aed):
    personajes_creados[id_aed].is_attacked(personajes_creados[id_atk].attack)
    return redirect(f'/ataque/{id_atk}')


@app.route('/aliarse/<int:id_atk>/<int:id_aed>')
def aliarPersonaje(id_atk, id_aed):

    if (personajes_creados[id_atk] in personajes_creados[id_aed].aliados):
        romper_alianza_grupo(personajes_creados[id_aed], personajes_creados[id_atk])
    else:
        aliarse_grupo(personajes_creados[id_aed], personajes_creados[id_atk])
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
