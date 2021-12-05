import random
import os

#määritellään boolean peli muutuja while looppia varten 
peli = True


#sanat
ammattilista = ["insinööri", "muurari", "sairaanhoitaja", "nuohooja", "kirurgi", "lääkäri", "maalari", "maanviljelijä"]
hedelmälista = ["banaani", "kiiwi", "persimon", "päärynä", "avokado", "appelsiini", "mandariini"]
ajoneuvolista = ["lentokone", "helikopteri", "moottoripyörä", "panssarivaunu"]

kategoria = {"ammatit" : ammattilista, "hedelmät" : hedelmälista, "ajoneuvot" : ajoneuvolista}

arvaukset = int(5)
väärät_kirjaimet = []

#määritellään pelaajalista arvaajien keräämistä varten
pelaajalista = []


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

#Käydään läpi hirsipuuhun valittua sanaa ja verrataan käyttäjän syöttämää kirjainta
def arvaaminen():
    if arvaus == valittu_sana:
        print("Voititte pelin <3")
        print("Hienoa työtä:")
        for pelaaja in pelaajalista:
            print(pelaaja)
        global peli
        peli = False

    for indeksi, kirjain in enumerate(valittu_sana):
        if kirjain == arvaus:
            global piilotettu_sana
            piilotettu_sana = piilotettu_sana[:indeksi] + kirjain + piilotettu_sana[indeksi+1:]
        elif kirjain != arvaus:
            continue
    if arvaus not in valittu_sana:
        väärä_arvaus(arvaus)
        global arvaukset
        arvaukset -= 1


def väärä_arvaus(x):
    väärät_kirjaimet.append(x)


#Funktio, jolla pyydetään pelinjohtajan nimi, joka keksii arvattavan sanan.
def pelinjohtaja():
    pelinjohtaja = input("Syötä nimimerkki: ")
    print("Tervetuloa pelinjohtaja:", pelinjohtaja)

#Funktio, jolla kysytään sanan arvaajat. Maksimi mmäärä arvaajia on kolme.
def arvaajat():    
    laskuri = 0
    global pelaajalista
    while True:
        pelaajat = input("Syötä nimimerkki: ")
        if pelaajat == "-1":
            print("Arvaajat syötetty. Voitte aloittaa arvaamaan")
            break
        elif laskuri < 3:            
            pelaajalista.append(pelaajat)
            laskuri += 1
        else:
            print("Maksimi määrä arvaajia. Voitte aloittaa arvaamaan.")
            break
    print(pelaajalista)

        
pelinjohtaja()
arvaajat()
valittu_sana = sanavalinta()
piilotettu_sana = str(len(valittu_sana)*'_')


print("Tervetuloa pelaamaan hirsipuuta", os.getlogin())
hirsipuu()


#peli-loop
while peli == True:

    print("Arvaa ammatti!")
    print(piilotettu_sana)
    print("Arvauksia jäljellä:")
    print(arvaukset)

    hirsipuu()

    arvaus = str(input())

    arvaaminen()
 
    print("Väärät kirjaimet:")
    print(väärät_kirjaimet)

    #Pelin lopetus
    if arvaukset == -1:
        hirsipuu()
        print("Hävisit pelin", "(° ͜ʖ͡°)╭∩╮")
        print(pelinjohtaja,"oli teitä parempi. Haahaa!")
        break
    elif piilotettu_sana == valittu_sana:
        print("Voititte pelin <3")
        print("Hienoa työtä:")
        for pelaaja in pelaajalista:
            print(pelaaja)
        break

