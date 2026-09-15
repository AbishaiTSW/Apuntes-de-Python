from xml.etree.ElementTree import PI


var = True
car = False

var = 11.90
car = 10.90

print(var + car)

# Flotantes son un tipo de dato que representan números con decimales. Se utilizan para realizar cálculos matemáticos que requieren precisión decimal, como operaciones financieras o científicas. En Python, los números flotantes se pueden crear utilizando el punto decimal (.) y se pueden manipular mediante operadores aritméticos y funciones matemáticas.
# booleanos son un tipo de dato que solo puede tener dos valores: True o False. Se utilizan para representar condiciones y tomar decisiones en el código. Por ejemplo, se pueden usar en estructuras de control como if, while y for para determinar qué acciones se deben ejecutar según ciertas condiciones.
# cadenas de texto son un tipo de dato que se utilizan para representar texto. Se pueden crear utilizando comillas simples (' ') o comillas dobles (" "). Las cadenas de texto se pueden concatenar, formatear y manipular de diversas maneras en Python.

print ("El valor de la booleano var es:", var)
print ("El valor de la booleano car es:", car)


a = 3.1416
b = float (5)

print ("El valor de la flotante a es:", a)
print ("El valor de la flotante b es:", b)


numero_uno = 29
numero_dos = 60.1

print ("El valor de numero uno es entero:", numero_uno)
print ("El valor de la flotante numero dos es:", numero_dos)

print(f"El numero {numero_uno} es del tipo: {type(numero_uno)}")
print(f"El numero {numero_dos} es del tipo: {type(numero_dos)}")

cielo_morado = False

print(f"El argumento {cielo_morado} es del tipo: {type(cielo_morado)}")
print(f"El argumento {var} es del tipo: {type(var)}") 
print(f"Se comprende que var entonces es {var}")