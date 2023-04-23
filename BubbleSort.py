lista_num = [9,8,7,6,5,4,3,2,1] # Lista de numeros desordenados

lista_len = len(lista_num) # Usamos len para saber el largo de la lista

# Funcion burbuja
def burbuja(lista):  
    for i in range(0,lista_len-1): # restamos uno a lista_len para que no pase del rango.
        for j in range(0,lista_len-1): # lo mismo para el siguiente for
            if lista_num[j] > lista_num[j+1]: # hacemos una comparación entre indices
                lista_num[j+1], lista_num[j] = lista_num[j], lista_num[j+1] # hacemos el intercambio si se cumple la condición. 
        
     
print("Método Burbuja".center(52, "#")) # Titulo
print(f'lista de numeros original {lista_num}') # Imprimimos la lista original
burbuja(lista_num) # Llamamos la función y como parámetro pasamos la lista original
print(f"lista ordenada {lista_num}") # Imprimimos lista ordenada