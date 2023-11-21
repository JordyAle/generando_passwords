import string
import secrets
import os

os.system("cls")

def contiene_mayusculas(password)->bool:
    for letra in password:
        if letra.isupper():
            return True
    return False

def contiene_simbolos(password)->bool:
    for letra in password:
        if letra in string.punctuation:
            return True
    return False

def generar_password(longitud, tiene_simbolos, tiene_mayusculas)->str:
    combinacion = string.ascii_lowercase + string.digits
    print(combinacion)
    #Simbolos
    if tiene_simbolos:
        combinacion += string.punctuation
        
    #Mayusulas
    if tiene_mayusculas:
        combinacion += string.ascii_uppercase
        
    longitud_combinacion = len(combinacion)
    
    nuevo_password = ""
    
   for _ in range (longitud):
       

if __name__ == "__main__":
    generar_password(longitud=2, tiene_simbolos=True, tiene_mayusculas=True)
    tiene_mayusculas = True
