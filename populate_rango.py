import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Practica4.settings')

import django
django.setup()

from rango.models import Bar, Tapa


def populate():
    curva_bar = add_bar('La curva', "Rotonda kinépolis")

    add_tapa(curva_bar, "Lomo alioli")

    add_tapa(curva_bar, "Lomo tomate")

    add_tapa(curva_bar, "Lomo con pimientos")

    add_tapa(curva_bar, "Tortilla de patatas")

    add_tapa(curva_bar, "Aceitunas y queso")


    bella_luna_bar = add_bar("La bella luna", "Plaza Einstein")

    add_tapa(bella_luna_bar, "Trozo de pizza de un ingrediente")

    add_tapa(bella_luna_bar, "Pollo tandori")

    add_tapa(bella_luna_bar, "Queso manchego")

    parra_bar = add_bar("La parra", "Calle Gonzalo Gallas")

    add_tapa(parra_bar, "Salchichas con patatas")

    add_tapa(parra_bar, "Montadito de lomo")

    add_tapa(parra_bar, "Patatas bravas")

    # Print out what we have added to the user.
    for c in Bar.objects.all():
        for p in Tapa.objects.filter(Bar=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_tapa(Bar, nombre, votos=0):
    t = Tapa.objects.get_or_create(Bar=Bar, nombre=nombre)[0]
    t.votos=votos
    t.save()
    return t

def add_bar(nombre, direccion, num_visitas=0):
    b = Bar.objects.get_or_create(nombre=nombre, direccion=direccion)[0]
    b.num_visitas=num_visitas
    b.save()
    return b

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
