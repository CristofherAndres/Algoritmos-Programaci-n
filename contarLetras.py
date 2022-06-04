texto = input('Ingrese un texto: ')

#Elimina los espacios antes y despues de la frase
texto = texto.strip()

#print(texto)

#a serpara el texto según un patrón
texto =texto.split(' ')
#print(texto)


#acumulador de la suma
suma = 0
for palabra in texto:
    #print(palabra)
    suma += len(palabra)

print('La cantidad de letras es:',suma)