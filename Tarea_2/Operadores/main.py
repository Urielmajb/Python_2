# Operadores
# alto = int(input("Proporcionar el alto: "))
# ancho = int(input("Proporcionar el ancho: "))
# area = alto * ancho
# perimetro = ((alto + ancho) * 2)
# print(f'El area es: {area}' + f'y el perimetro: {perimetro}')

# Incremento con reasignacion
# miVariable = 11
# print(miVariable)
# miVariable -= 2
# print(miVariable)
# miVariable += 3
# print(miVariable)

# Operaciones de comparacion
# a = int(input('Ingrese el 1er numero'))
# b= input('Ingrese el 2d0 numero')

# if a % 2 == 0:
# print('El valor de {a} es numero par')
# else:
# print('El valor de {a} es impar')
# edad=18
# edadPersona= int(input('Escribe tu edad: '))
# if edadPersona >= edad:
#   print('Eres mayor de edad')
# else:
#  print('Eres menor de edad')

# Operadores logicos
# a= True
# b= True
# resultado = a and b
# print(resultado)
# valor = int(input('Escribe el valor: '))
# valorMinimo = 0
# valorMaximo = 5
# dentroRango = valor >= valorMinimo and valor <= valorMaximo
# if dentroRango:
# print(f'El valor {valor} esta dentro de rango')
# else:
# print(f'El valor {valor} esta fuera de rango')

#vacaciones = False
#diaDescanso = False
#tieneVacaciones = not vacaciones
#if tieneVacaciones:
#print('Puede asistir al juego')
#else:
#print('No puede asistir al juego')

#edad= int(input('Ingrese la edad'))
#veintes = edad >= 20 and edad <= 30
#treintas = edad >= 30  and edad <= 40
#print(veintes, treintas)
#if veintes or treintas:
 #print('Dentro de rango (20\'s) p (30\'s) ')
  #if veintes:
   #print('Dentro de los 20s')
   #elif treintas:
    #print('Dentro de los 30s')
#else:
 #  print ("'No esta dentro de los 20's y 30's")
#numero1 = int(input('Proporciona el numero 1'))
#numero2 = int(input('Proporciona el numero 2'))
#if(numero1 > numero2):
 #print("El numero mayor es el No 1")
#else:
 #print("El numero mayor  es el No 2")

print(" ++++ Proporcione los datos del libro ++++ ")
nombreLibro = input("Proporcione el nombre del libro: ")
idLibro = int(input("Proporcione el ID de libro: "))
precioLibro = float(input("Proporcione el precio de Libro: "))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, escriba de nuevo (True/False)'

print(f'''
     Nombre: {nombreLibro}, 
     ID Libro: {idLibro},
     Precio: {precioLibro},
     Envio: {envioGratuito}
''')

