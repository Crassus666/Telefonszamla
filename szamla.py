bekert_telefon = input("Adjon meg egy telefonszámot: ")

elso_ketto_szamjegy = bekert_telefon.split()[0][0] + bekert_telefon.split()[0][1]

if elso_ketto_szamjegy == "41" or elso_ketto_szamjegy == "39" or elso_ketto_szamjegy == "71":
    print("Ez a szám mobil szám.")

else:
    print("Ez egy vezetékes telefon száma.")

#2. feladat

kezdet = input("Hívás kezdte szóközökkel elválasztva (óra, perc, mp): ")
veg = input("Hívás vége szóközökkel elválasztva(óra, perc, mp): ")

hivas_hossz = int(veg.split(" ")[0])*60 - int(kezdet.split(" ")[0])*60 + int(veg.split(" ")[1]) - int(kezdet.split(" ")[1])

print(f"A hívás hossza {hivas_hossz} perc volt.")

#3. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\HIVASOK.txt', 'r')
fajl = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\percek.txt', 'w')

sor = txt.readline()

while sor != "":
    szamlazott_perc = int(sor.split(" ")[3])*60 - int(sor.split(" ")[0])*60 + int(sor.split(" ")[4]) - int(sor.split(" ")[1])
    sor = txt.readline()
    fajl.writelines(f'{szamlazott_perc}, {sor}')
    sor = txt.readline()

txt.close()
fajl.close()

#4. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\HIVASOK.txt', 'r')
sor = txt.readline()
csucsido = 0
hivasok_szama = 0

while sor != "":
    if 18 > int(sor.split(" ")[0]) >= 7:
        csucsido += 1

    sor = txt.readline()
    sor = txt.readline()
    hivasok_szama += 1

print(f" Csúcsidős hívások: {csucsido}, Nem csúcsidősek: {hivasok_szama-csucsido}")
txt.close()

#5. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\HIVASOK.txt', 'r')
sor = txt.readline()


mobillal = 0
vezetekessel = 0
adott_sor_perc = 0


while sor != "":
    adott_sor_perc = int(sor.split(" ")[3])*60 - int(sor.split(" ")[0])*60 + int(sor.split(" ")[4]) - int(sor.split(" ")[1])

    sor = txt.readline()
    if (sor.split()[0][0] + sor.split()[0][1]) == "41" or (sor.split()[0][0] + sor.split()[0][1]) == "39" or (sor.split()[0][0] + sor.split()[0][1]) == "71":

        vezetekessel += adott_sor_perc
        adott_sor_perc = 0

    else:
        mobillal += adott_sor_perc
        adott_sor_perc = 0

    sor = txt.readline()

print(f"Percek száma mobillal: {mobillal} és vezetékessel: {vezetekessel}.")
txt.close()

#6. feladat

txt = open(r'C:\Users\User\.PyCharmCE2019.1\config\scratches\HIVASOK.txt', 'r')
sor = txt.readline()


mobillal = 0
vezetekessel = 0
adott_sor_perc = 0


while sor != "":
    adott_sor_perc = int(sor.split(" ")[3])*60 - int(sor.split(" ")[0])*60 + int(sor.split(" ")[4]) - int(sor.split(" ")[1])

    if 18 > int(sor.split(" ")[0]) >= 7:
        sor = txt.readline()
        if (sor.split()[0][0] + sor.split()[0][1]) == "41" or (sor.split()[0][0] + sor.split()[0][1]) == "39" or (sor.split()[0][0] + sor.split()[0][1]) == "71":
            vezetekessel += adott_sor_perc
            adott_sor_perc = 0

    else:
        mobillal += adott_sor_perc
        adott_sor_perc = 0
        sor = txt.readline()


    sor = txt.readline()

print(f'{int(vezetekessel*30+mobillal*69.175)} forintot kell fizetnie a felhasználónak. ')
txt.close()