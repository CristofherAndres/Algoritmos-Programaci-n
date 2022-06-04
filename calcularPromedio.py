#contador del ciclo
i = 0

#Acumulador de la suma
suma = 0

while(i<3):
    nota = float(input('Ingrese la nota '+str(i+1)+': '))
    suma+=nota # suma = suma + nota
    i+=1

promedio = suma/3

print('El promedio es:',promedio)