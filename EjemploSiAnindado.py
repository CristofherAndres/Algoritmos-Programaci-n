# Si el monto a pagar es menor de 10 mil pagamos con efectivo
#Si el monto es entre 10 y 30 mil pagamos con debito
#Si el monto es 30 y 60 mil pagamos con cheque
# Sino pagamos con credito

monto = int(input('Ingrese el monto al pagar: '))

if (monto < 10000):
    print('Pagar con efectivo')
elif (monto >=10000 and monto<30000):
    print('Pagar con debito')
elif (monto >=30000 and monto<60000):
    print('Pagar con cheque')
else:
    print('Pagar con credito')