print ("labas")
print (13/5)
print (13%5)
print (13//5)

print(15)
print(12)
print(89)
print(5.8)
print(78*2)
print(5+3)
print(7/2)
print(85-32)
print (round(5.2*3,2))
print(5.4*0.5)
print (9.4*0.5)
print(4.2/2)

# 4. Išveskite šių matematinių veiksmų atsakymus: 1. 7 + 2 * 3 2. (7 + 2) * 3 3. 52 + 74 + 32
#4. 87 -65 + 14 5. 79 / (5 -2)
#5. Apskaičiuokite išveskite šiuos atsakymus (naudojant ** operatorių):
# 1. skaičių 2 pakeltą 4-u laipsniu 2. skaičių 8 pakeltą 3-u laipsniu
#3. skaičių 14 pakeltą 0.5-io laipsnio

print (7+2*3)
print((7+2)*3)
print (52+74+32)
print (87-65+14)
print(round(79/(5-2),2))
print(2**4)
print(8**3)
print(round(14**0.5,2))

'''6. Raskite šių dalybų liekanas (naudojant % operatorių):
1. 2 iš 2 2. 3 iš 2 3. 11 iš 2 4. 13 iš 2 5. 10 iš 2 
7. Raskite šių dalybų liekanas (naudojant % operatorių):
1. 15 iš kiekvieno skaičiaus nuo 2 iki 9 (15 iš 2, 15 iš 3 ir pan.)'''

print(2%2)
print(3%2)
print(11%2)
print(13%2)
print(10%2)
print(15%2)
print(15%3)
print(15%4)
print(15%5)
print(15%6)
print(15%7)
print(15%8)
print(15%9)

'''8. Atlikite tokias integer dalybas (naudojant // operatorių): 1. 5 iš 2 2. 6 iš 3
3. 6 iš 4 4. 80 iš 3 5. 45 iš 4 6. 45 iš 3'''
print(5//2)
print(6//3)
print(6//4)
print(80//3)
print(45//4)
print(45//3)
'''9. Išsiaiškinkite duomenų tipus (panaudokite type) šiems atvejams:
1. jeigu yra skaičius 6 2. jeigu yra skaičius 2.5 3. jeigu yra skaičius 157 
4. jeigu yra skaičius -8.2 5. jeigu yra dalyba 2 iš 5 6. jeigu yra sudėtis 8 su 9
7. jeigu yra sudėtis 8.5 su 3'''
print(type(6))
print(type(2.5))
print(type(157))
print(type(-8.2))
print(type(2/5))
print(type(8+9))
print(type(8.5+3))

'''1.
Aprašykite ir išveskite (atskirose eilutėse) kintamuosius, saugančius šią informaciją 
apie studentą:'''

vardas = 'Kristina'
print('V - ',vardas)
pavarde = 'Sut'
print('P - ',pavarde)
amzius = '30+'
print('amzius - ', amzius)
ugis = '~170'
print('ugis - ',ugis)
svoris = ':)'
print('svoris - ',svoris)
aukstojiMokykla = 'KU'
print('AM - ',aukstojiMokykla)
akademinesGrupesKodas = '123'
print('AkGr - ',akademinesGrupesKodas)
kursas = "4"
print('kursas - ',kursas)
studijuProgramosPavadinimas = "DA"
print('SPP - ',studijuProgramosPavadinimas)
atsiskaitytuKredituSkaicius = "2"
print('AK - ',atsiskaitytuKredituSkaicius)

'''2. Aprašykite ir išveskite (atskirose eilutėse) kintamuosius, saugančius šią 
informaciją apie miestą: 1. Pavadinimas; 2. Valstybė; 3. Apskritis; 4. Įkūrimo data;
5. Meras; 6. Plotas kv. km.; 7. Gyventojų skaičius;'''
pavadinimas = 'Klaipeda'
print('pavadinimas - ',pavadinimas)
state = 'KLP'
print('State - ',state)


'''Susikurkite kintamąjį savo vardui saugoti. Išveskite į konsolę tekstą "mano vardas yra " ir turimo kintamojo reikšmę.'''

print('my name: ', 6)


#

x=5
y=15
suma = x+y
print(suma)

z=3
print(f'{x}+{y}+{z}={x+y+z}')
print(f'{x}-{y}-{z}={x-y-z}')

x1=x+5
y1=y*2

print(f'{x1} - padidintas 5 vienetais; {y1} - y padidintas 2 kartus; pradines x, y reiksmes: {x} ir {y}')

'''print('Iveskite du skaicius:')
print('Pirmas akicius (x)')
x = int(input())
print('Antras skaicius (y):')
y = int(input())
print('Liekana x/y:')
print(f'{x}/{y} liekana {x%y}')'''

'''print('Kiek gautųsi vieną skaičių pakėlus kito skaičiaus laipsniu?')
print('Pirmas akicius (a)')
a = int(input())
print('Antras skaicius (b):')
b = int(input())
print('a pakelta b:')
print(f'{a**b}')'''


'''vardas = input('Iveskite varda: ')
amzius = int( input('Iveskite amziu: ') )
ugis = int( input('Iveskite ugi (cm): '))
print('Ivesta informacija:')
print(f'Vardas:{vardas}, amzius:{amzius}m., ugis:{ugis}cm.')
print(vardas, type(vardas))
print(amzius, type(amzius))
print(ugis, type(ugis))'''

x = int(input('Iveskite x: '))
y = int(input('Iveskite y: '))
z = int(input('Iveskite z: '))

if x==y:
    print('x lygu y')

if x!=y:
    print('x ir z yra nelygūs')

if x>y:
    print('x yra didesnis už y')

if y>z**2 and y>z*2:
    print('y yra didesnis už z kvadratu ir z padauginto iš 2')

if x % 2 == 0:
    print ('x yra lyginis')

if y % 2 != 0:
    print('y yra nelyginis')

if z>0:
    print('z yra teigiamas')

if x<0:
    print('x yra neigiams')

if y % 4 == 0:
    print ('y dalinasi is 4')

if z % 8 == 0:
    print ('z dalinasi is 8')
