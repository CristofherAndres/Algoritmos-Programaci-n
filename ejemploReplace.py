# función replace -> remplazar un valor string

animal = 'pollo'
frase = 'El '+animal+' dice guau guau cuando esta enojado'
print(frase)

corregir = 'pollo'

while (corregir != 'perro'):
    animal = corregir
    corregir = input('¿Que debe decir en lugar de '+animal+'? ')
    frase = frase.replace(animal,corregir)
    print(frase)

#frase = frase.replace('pollo',corregir)
#print(frase)