from os import system

from intro.poo.species.Elfo import Elfo
from intro.poo.species.Breton import Breton
from intro.poo.species.Imperial import Imperial
from intro.poo.species.Ogro import Ogro
from intro.poo.species.Argoniano import Argoniano

personajes_creados = [Argoniano('fUmaratto', 180, 200, 19)]
personaje_activo = personajes_creados[0]


def menu_general():
    print('Seleccione una opcion:')
    print('1. Crear nuevo personaje')
    print('2. Seleccionar personaje activo')
    print('3. Atacar otro personaje')
    print('4. Añadir aliado')
    print('0. Salir')
    opt = int(input('(Personaje activo: ' + personaje_activo.name.title() + ') \nOpcion: '))
    return opt


def crear_personaje():
    print('¿Que especie desea crear?')
    print('1. Elfo')
    print('2. Ogro')
    print('3. Imperial')
    print('4. Breton')
    print('5. Argoniano')

    especie = int(input('Ingrese su elección: '))
    nombre = input('Ingrese el nombre: ')
    edad = int(input('Ingrese su edad: '))
    altura = float(input('Ingrese su altura:'))
    peso = int(input('Ingrese su peso: '))

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


def menu_opcion_1():
    personaje_nuevo = crear_personaje()
    personajes_creados.append(personaje_nuevo)
    print('El numero del personaje creado es: ' + str(len(personajes_creados)))
    input("PRESIONA ENTER PARA CONTINUAR.")
    print('-------------------------------')
    system('cls')


def menu_opcion_2():
    number = 0
    print('Personajes disponibles: ')
    for personaje in personajes_creados:
        number += 1
        print(str(number) + '. ' + personaje.name.title())
    personaje_select = int(input('Ingrese el numero del personaje que desea administrar: '))
    if (personaje_select > len(personajes_creados)):
        print('Ingrese una posicion que exista imbecil')
    else:
        personaje_activo = personajes_creados[personaje_select - 1]
        print('Personaje activo: ' + personaje_activo.name)
    input("PRESIONA ENTER PARA CONTINUAR.")
    print('-------------------------------')
    system('cls')


def menu_opcion_3():
    atacara = int(input('Ingresa el numero del personaje que deseas atacar: '))
    personajes_creados[atacara - 1].is_attacked(personaje_activo.attack)
    print('Vida restante: ' + str(personajes_creados[atacara - 1].live))


def menu_opcion_4():
    pass


if __name__ == '__main__':
    optiong = 5
    while optiong != 0:
        optiong = menu_general()
        if optiong == 1:
            menu_opcion_1()
        elif optiong == 2:
            menu_opcion_2()
        elif optiong == 3:
            menu_opcion_3()
