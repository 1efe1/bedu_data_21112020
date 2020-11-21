#script que calcula la tambla de multiplicar de un número

numero = input('que numero quieres multiplicar?')
# el dato ingresado por el usuario es una cdena "<str>"
# Se debe convertir a numero "<int>" para poder multiplicar 
numero=int(numero)

for n in range(10):
    r = numero * (n + 1)
    print(r)
    

