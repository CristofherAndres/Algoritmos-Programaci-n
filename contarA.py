#Contar todas las vocales de una frase que ingrese un usuario

frase = input('Ingrese una frase: ')

frase = frase.strip().lower()

i=0
vocalA = 0

while (i<len(frase)):
    if (frase[i]=='a'):
        vocalA += 1
    i+=1

print('Las letras a son:',vocalA)
