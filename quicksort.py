def quicksort(lista, start = 0, ends = None):
  if ends is None:
    ends = len(lista) - 1
  if start < ends: #se o começo for menor que o final
    pivot = partition(lista, start, ends) #acha o pivo
    quicksort(lista, start, pivot - 1) #roda denovo para as outras partes, começo até um antes do pivo
    quicksort(lista, pivot + 1, ends) #um depois do pivo até o final

def partition(lista, start, ends):
  pivot = lista[ends] #elemento pivo vai ser o ultimo item
  i = start #i = ao indice de onde está começando
  for j in range(start, ends): #roda para todos os números (começo ao final)
    if lista[j] <= pivot: #se o elemento for menor ou igual ao pivo
      lista[j], lista[i] = lista[i], lista[j] #troca o elemento de posição com o pivo
      i += 1 #aumenta o indice
  lista[i], lista[ends] = lista[ends], lista[i] 
  return i


lista = [7, 5, 4, 2 ,1, 8, 3, 6]
quicksort(lista)
print(lista)