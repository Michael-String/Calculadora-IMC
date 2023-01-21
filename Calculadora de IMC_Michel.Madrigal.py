# Proyecto 1: Calculadora de I.M.C.
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5

while True:

           nombre = input("Hola, ¿cómo se encuentra hoy?, ingrese de favor su nombre(s): ")
           if not nombre.__str__():
              print("Este campo es obligatorio, favor de llenarlo")
              continue
           break 
while True:

           apellidoPaterno = input("Ingrese de favor su apellido paterno: ")
           if not apellidoPaterno.isalpha():
              print("Este campo es obligatorio, favor de llenarlo")
              continue
           break 
        
while True:

           apellidoMaterno = input("Ingrese de favor su apellido materno: ")
           if not apellidoMaterno.isalpha():
              print("Este campo es obligatorio, favor de llenarlo")
              continue
           break 
         

while True:
    try:
         edad = int(input("¿Cuál es su edad?: "))
    except ValueError:
        print("Debe ingresar una cifra por favor")
        continue
    break
while True:
    try:
         peso = float(input("¿Cuál es su peso?: "))
    except ValueError:
        print("Debe ingresar una cifra por favor")
        continue
    break
while True:
    try:
         estatura = float(input("¿Cuánto mide?: "))
    except ValueError:
        print("Debe ingresar una cifra por favor")
        continue
    break

tamaño = estatura
IMC= peso/tamaño**2

print("Nombre(s): " + nombre)
print("Apellido Paterno: " + apellidoPaterno)
print("Apellido Materno: " + apellidoMaterno)
print("Tengo: " + str(edad) + " años")
print("Peso: " + str(peso) + " Kg")
print("Mido: " + str(estatura) + " m") 
print("Su IMC es de: " + str(IMC)) 

if IMC < 18.5:
    print("Cuidado, su peso es muy bajo, se recomienda dieta")
elif 18.5 <= IMC and IMC < 25:
    print("¡Felicidades, está en tu peso ideal, siga así!")
elif 25 <= IMC and IMC < 30:
    print("Cuidado, presenta sobrepeso, se recomienda dieta")
else:
    print("¡Atención, presenta obesidad, acuda con un especialista!")