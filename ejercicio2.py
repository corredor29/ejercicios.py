"""
Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.
2. Que comience con mayúscula.<<<<<<<<<<

"""



nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")