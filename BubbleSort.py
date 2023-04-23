lista_num = [9,8,7,6,5,4,3,2,1]

lista_len = len(lista_num)

def burbuja(lista):
    for i in range(0,lista_len-1):
        for j in range(0,lista_len-1):
            if lista_num[j] > lista_num[j+1]:
                lista_num[j+1], lista_num[j] = lista_num[j], lista_num[j+1]
        

print(f'lista de numeros original {lista_num}')
print("Ordenamieto Burbuja")
burbuja(lista_num)
print(f"Esta es lista ordenada {lista_num}")