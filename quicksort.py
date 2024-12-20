def quicksort(lista, start = 0, ends = None):
  if ends is None:
    ends = len(lista) - 1
  if start < ends:
    pivot = partition(lista, start, ends)
    quicksort(lista, start, pivot - 1)
    quicksort(lista, pivot + 1, ends) 

def partition(lista, start, ends):
  pivot = lista[ends]
  i = start
  for j in range(start, ends):
    if lista[j] <= pivot:
      lista[j], lista[i] = lista[i], lista[j]
      i += 1
  lista[i], lista[ends] = lista[ends], lista[i]
  return i


lista = [7, 5, 4, 2 ,1, 8, 3]
quicksort(lista)
print(lista)