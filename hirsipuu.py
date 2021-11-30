import random
import os


#sanat
ammattilista = ["insinööri", "muurari", "sairaanhoitaja", "nuohooja", "kirurgi", "lääkäri", "maalari", "maanviljelijä"]
hedelmälista = ["banaani", "kiiwi", "persimon", "päärynä"]
ajoneuvolista = ["lentokone", "helikopteri", "moottoripyörä", "panssarivaunu"]
kategoria = {"ammatit" : ammattilista, "hedelmät" : hedelmälista, "ajoneuvot" : ajoneuvolista}

arvaukset = int(5)

#hirsipuu
def hirsipuu():
    if arvaukset == -1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('/|\  |')
        print('/ \  |')
        print('     |   ')
        print('=========')
    elif arvaukset == 0:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('/ \  |')
        print('     |   ')
        print('=========')
    elif arvaukset == 1:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print(' |   |')
        print('/    |')
        print('     |   ')
        print('=========')
    elif arvaukset == 2:
        print(' +---+')
        print(' |   |')
        print(' O   |')
        print('     |')
        print('     |')
        print('     |   ')
        print('=========')
    elif arvaukset == 3:
        print('     |')
        print('     |')
        print('     |')
        print('     |   ')
        print('=========')
    elif arvaukset == 4:
        print('     |   ')
        print('=========')

def sanavalinta():
    for x in kategoria:
        print(x)
    kategoriavalinta = str(input("Valitse sanakategoria: "))
    if kategoriavalinta == kategoria.keys():
        print(kategoria[kategoriavalinta])
    for z in kategoria[kategoriavalinta]:
        print(z)
    valittu_sana = str(input("Valitse sana: "))

    return valittu_sana

print("Tervetuloa pelaamaan hirsipuuta", os.getlogin())

valittu_sana = sanavalinta()
piilotettu_sana = str(len(valittu_sana)*'_')

hirsipuu()

#peli-loop
while arvaukset >= 0:

    print("Arvaa ammatti!")
    print(piilotettu_sana)
    print("Arvauksia jäljellä:")
    print(arvaukset)

    hirsipuu()

    arvaus = str(input())

    for indeksi, kirjain in enumerate(valittu_sana):
        if kirjain == arvaus:
            piilotettu_sana = piilotettu_sana[:indeksi] + kirjain + piilotettu_sana[indeksi+1:]
        elif kirjain != arvaus:
            continue
    
    if arvaus not in valittu_sana:
        arvaukset -= 1

    if arvaukset == -1:
        hirsipuu()
        print("Hävisit pelin", "(° ͜ʖ͡°)╭∩╮")
        break

