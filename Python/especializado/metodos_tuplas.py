#Metodos de tupla
#Una tupla es una coleccion ordenada e inmutable de elementos. por tanto solo podemos observar sus elementos

tupleList = (1,2,3,4)
tupleTwo = ("Uno", "Dos", "Tres")

#count(elemento): Devuelve el numero de veces que un elemento aparece en la tupla
print(f"El numero 2 aparece {tupleList.count(2)} veces en la tupla tupleList")
         
#index(): Devuelve el indice de la primera aparicion de un elemento en la tupla
print(f"El elemento 'Dos' se encuentra en el indice {tupleTwo.index('Dos')} de la tupla tupleTwo")          