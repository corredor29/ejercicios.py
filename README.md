### ejercicios python trabajo

Ejercicio 1: Contando caracteres:

Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.

2. La cantidad de espacios en la frase.

   frase = input("Escribe una frase: ")

   creamos una variable y un input para poder escribir

   total_caracteres = len(frase)

   creamos otra variable y usamos un `len()` para contar el total de caracteres.

   espacios = frase.count(" ")

   creamos otra variable y usamos un  `count()` para contar los espacios.

   print(f"La frase tiene {total_caracteres} caracteres en total.")

   usamos print para poder imprimir el resultado de las variables y poder dar la cantidad de caracteres de la frase 

   print(f"La frase tiene {espacios} espacios.")

   usamos print para imprimir la frase y para poder dar la cantidad de espacios en la frase 

**Ejercicio 2: Validando nombres**

Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.

2. Que comience con mayúscula.

   nombre = input("Escribe tu nombre completo: ")

   creamos una variable y usamos un input para poder escribir

   if nombre.replace(" ", "").isalpha():
       if nombre.istitle():
           print("El nombre es válido.")

   usamos un if que es un bucle y un  `isalpha()` para verificar que solo hay letras.

   y un `istitle()` para verificar que las palabras comiencen con mayúscula.

   imprimimos el numero valido

       else:
           print("El nombre debe comenzar con mayúscula.")

   else:
       print("El nombre solo debe contener letras.")

   usamos else para los parametros

   **Ejercicio 3: Invirtiendo palabras**

   Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.

   palabra = input("Escribe una palabra: ")

   usamos una variable y input para imprimir 

   invertida = palabra[::-1]

   usamos la inversa y Usamos el operador de slicing `[::-1]` para invertir la cadena.

   print(f"La palabra invertida es: {invertida}")

   usamos print para imprimir 

   **Ejercicio 4: Cifrando texto**

   Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).

   frase = input("Escribe una frase: ")

   usamos un input para poder escribir la frase

   frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")*

   Usamos `replace()` repetidamente para reemplazar las vocales.

   frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

   print(f"La frase cifrada es: {frase_cifrada}")

   y luego imprimimos el valor 

   **Ejercicio 5: Contador de vocales**

   Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.

   frase = input("Escribe una frase: ")

   con input para poder escribir la frase

   a = frase.count("a") + frase.count("A")
   e = frase.count("e") + frase.count("E")
   i = frase.count("i") + frase.count("I")
   o = frase.count("o") + frase.count("O")
   u = frase.count("u") + frase.count("U")

   Usamos `count()` para contar las vocales individualmente.

   total_vocales = a + e + i + o + u

   luego sumamos todo

   print(f"La frase tiene {total_vocales} vocales.")

   y luego con print damos el resultado 

   

**Ejercicio 6: Formateando cadenas**

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

telefono = input("Escribe un número de teléfono de 10 dígitos: ")

usamos una variable y un input para poder escribir

if len(telefono) == 10 and telefono.isdigit():

Usa slicing para dividir la cadena en partes.

​    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"

 la usamos para dar formato visual a un número de teléfono

​    print(f"El número formateado es: {telefono_formateado}")

imprimimos el resultado con un print

else:
    print("El número debe tener exactamente 10 dígitos.")

y usamos else para las demas excepciones 

**Ejercicio 7: Detectando palíndromos**

Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).

palabra = input("Escribe una palabra: ").lower()

escribimos con input la variable 

invertida = palabra[::-1]

sirve para invertir una cadena de texto

if palabra == invertida:
    print("La palabra es un palíndromo.")



else:
    print("La palabra no es un palíndromo.")

y Comparamos la palabra original con su versión invertida, y verifica si son iguales. Si lo son, significa que es un palíndromo

