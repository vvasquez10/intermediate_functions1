"""
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima 
el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
"""
def iterateDictionary2(clave, lista):
    for i in lista:
        for x in i:
            if clave==x:
                print(i[x])               

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary2("last_name", estudiantes)

