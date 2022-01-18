"""
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave
junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. 
"""

def printInfo(dic):
    for i in dojo:
        print(len(dojo[i]), i)
        for x in dojo[i]:            
            print(x)
        print("\n")

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)