def subCadena(texto,inicio,fin):
    resultado = ''
    if inicio <= fin and inicio < len(texto) and fin < len(texto):
        while inicio <= fin :
            resultado += texto[inicio]
            inicio += 1
    return resultado
    #QUE PASA TIO
<<<<<<< HEAD
#Comentario DIEGOOOOOO
#Comentario Albertoooooo
=======
<<<<<<< HEAD
<<<<<<< HEAD
#SEXTA MODIFICACIÓN DIEGOOOOOOOOOOOOOO
=======
#Intento de fusión
>>>>>>> prueba-diego
=======
#Comentario DIEGOOOOOO - FUSIÓNNNNNNNNNNN 2
# Fusion 3
=======
#SEXTA MODIFICACIÓN DIEGOOOOOOOOOOOOOO
>>>>>>> 8a95eb3203d2a87df135ea75dcc4719b9ad226a7
>>>>>>> e4b434b552eb78edb563acd0260b62ae5f8ad11c
>>>>>>> 3445cc41a2ae9508c78f51d6b9ca933dae02b7f2
def posCadena(texto,subtexto):
    i = 0
    while i+len(subtexto) <= len(texto) :
        if subCadena(texto,i,i+len(subtexto)-1) == subtexto:
            return i
        else:
            i+=1
    return -1

def estaEnArray(array,valor):
    i = 0
    while i<= len(array)-1 :
        if array[i] == valor :
            return True
        else :
            i += 1
    return False

print("Este programa lee una cadena de texto y devuelve la misma cadena intercambiando cada vocal por la siguiente\n")
texto_prueba = input("Introduce el texto\n")

vocales = "aeiouaáéíóúáAEIOUAÁÉÍÓÚÁ"
Auxiliar = ""
i = 0

while i < len(texto_prueba):
    if estaEnArray(vocales,texto_prueba[i]) == True:
        Auxiliar += vocales[posCadena(vocales,texto_prueba[i])+1]
        i+=1
    else:
        Auxiliar += texto_prueba[i]
        i+=1


print(Auxiliar)