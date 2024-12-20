def selection_sort(lista): #acha o menor e vai trocando de posição
  for j in range(len(lista) - 1): #objetivo é achar 1° menor, 2° menor e...
    min_index = j #min_index vai ser o indice do menor num da lista
    for i in range(j, len(lista)): #percorre todos da lista para achar o menor
      if lista[i] < lista[min_index]:
        min_index = i #quando acha um menor, armazena o indice dele
    if lista[j] > lista[min_index]: #se o num corrente for maior que o que achamos
      lista[j], lista[min_index] = lista[min_index], lista[j] #troca de posição

lista = [7, 5, 1, 8, 3]
selection_sort(lista)
print(lista)