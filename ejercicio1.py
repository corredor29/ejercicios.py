"""
Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.
2. La cantidad de espacios en la frase.


"""




frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")