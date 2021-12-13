from os import system, name
import datetime


#määritellään boolean peli-muuttuja while-looppia varten 
peli = True

#sanavaihtoehdot
ammattilista = ["insinööri", "muurari", "sairaanhoitaja", "nuohooja", "kirurgi", "lääkäri", "maalari", "maanviljelijä"]
hedelmälista = ["banaani", "kiiwi", "persimon", "päärynä", "avokado", "appelsiini", "mandariini"]
ajoneuvolista = ["lentokone", "helikopteri", "moottoripyörä", "panssarivaunu"]

#kategoriat, joista pelinjohtaja valitsee sanan
kategoria = {"ammatit" : ammattilista, "hedelmät" : hedelmälista, "ajoneuvot" : ajoneuvolista}

#muita globaaleja muuttujia peliä varten
arvaukset = int(5)
väärät_kirjaimet = []
pelaajalista = []
johtaja = ""


#tällä funktiolla käyttäjä voi tarkastella aikaisemmin pelattuja pelejä
def lokinavaus():
    with open("tulosseuranta.txt", "r") as tiedosto:
        print("Loki aiemmista peleistä:")
        for rivi in tiedosto:
            print(rivi)

#tyhjennetään terminaali ennen pelin alkamista, jotta arvaajat eivät nää valittua sanaa eivätkä sanavaihtoehtoja
def terminaalintyhjennys():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

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

#funktio, jolla valitaan hirsipuuhun sana
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

#käydään läpi hirsipuuhun valittua sanaa ja verrataan käyttäjän syöttämää kirjainta
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

#funktio, joka lisää väärät kirjaimet listaan
def väärä_arvaus(x):
    väärät_kirjaimet.append(x)

#funktio, jolla pyydetään pelinjohtajan nimi, joka keksii arvattavan sanan.
def pelinjohtaja():
    global johtaja
    johtaja = input("Syötä nimimerkki: ")
    print("Tervetuloa pelinjohtaja:", johtaja)

#funktio, jolla kysytään sanan arvaajat. Maksimi mmäärä arvaajia on kolme.
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

#aloitetaan pelaaminen syöttämällä pelaajat
pelinjohtaja()
arvaajat()

valittu_sana = sanavalinta()
piilotettu_sana = str(len(valittu_sana)*'_')

terminaalintyhjennys()

print("Tervetuloa pelaamaan hirsipuuta")
hirsipuu()


#jatkuva peli-loop
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

    if arvaukset == -1:
        hirsipuu()
        print("Hävisit pelin", "(° ͜ʖ͡°)╭∩╮")
        print(johtaja,"oli teitä parempi. Haahaa!")
        break

    elif piilotettu_sana == valittu_sana:
        print("Voititte pelin <3")
        print("Hienoa työtä:")
        for pelaaja in pelaajalista:
            print(pelaaja)
        break


#loki peleistä
with open("tulosseuranta.txt", "a") as tiedosto:
    if piilotettu_sana == valittu_sana or arvaus == valittu_sana:
        tiedosto.write(f"\n {pelaajalista} voittivat pelin. Päivämäärä: {datetime.datetime.now()}")

    elif arvaukset == -1:
        tiedosto.write(f"\n {johtaja} voitti pelin. Päivämäärä: {datetime.datetime.now()}")

print("Haluatko tarkastella lokia aikaisemmista peleistä?")
print("Jos haluat kirjoita y ja paina ENTER")

vastaus = input("Haluatko lukea lokia?: ")
if vastaus == "y":
    lokinavaus()