from Intro.poo.species.Elfo import Elfo
from Intro.poo.species.Breton import Breton
from Intro.poo.species.Imperial import Imperial
from Intro.poo.species.Ogro import Ogro
from Intro.poo.species.Argoniano import Argoniano

def menu_general():
    opt = input('Opcion: ')
    print('Seleccione una opciob:')
    print('1. Crear nuevo personaje')
    print('2. Seleccionar personaje activo')
    print('3. Atacar otro personaje')

    return opt

def crear_personaje():
    print('¿Que especie desea crear?')
    print('1. Elfo')
    print('2. Ogro')
    print('3. Imperial')
    print('4. Breton')
    print('5. Argoniano')

    especie = input('Ingrese su elección: ')
    nombre = input('Ingrese el nombre: ')
    edad = input('Ingrese su edad: ')
    altura = input('Ingrese su altura:')
    peso = input('Ingrese su peso: ')

    if especie == 1:
        return Elfo(nombre, peso, altura, edad)
    elif especie == 2:
        return Ogro(nombre, peso, altura, edad)
    elif especie == 3:
        return Imperial(nombre, peso, altura, edad)
    elif especie == 4:
        return Breton(nombre, peso, altura, edad)
    elif especie == 5:
        return Argoniano(nombre, peso, altura, edad)


if __name__ == '__main__':
    personajes_creados = []
    personaje_activo = None
    optiong = 1

    while optiong != 0:
        optiong = menu_general()
        if optiong == 1:
            personajes_creados.append(crear_personaje())
            print('El numero del personaje creado es: ' + len(personajes_creados)-2)
        elif optiong == 2:
            personaje_select = input('Ingrese la posicion del personaje que desea administrar: ')
            personaje_activo = personajes_creados[1]
        elif optiong == 3:
             pass

