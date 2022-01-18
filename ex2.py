"""Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios 
de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
"""
def iterateDictionary(lista):
    for i in lista:
        for x in i:
            print(x, "-", i[x], end="")   
            if x=="first_name":
                print(",", end=" ")
        print("")


estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(estudiantes) 
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)

"""
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""