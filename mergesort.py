def mergesort(lista, start = 0, ends = None): #divide até ficar com um item e depois vai olhando cada parte e juntando ordenademente
  if ends is None: #start e end = indice que começa e termina                 #compara topo com topo e ordena
    ends = len(lista)
  if (ends - start) > 1: #enquanto for maior que 1
    middle = (ends + start) // 2 #divisão exata achar o indice do meio mesmo se for ímpar
    mergesort(lista, start, middle) #repassa toda a lista para ser dividida
    mergesort(lista, middle, ends)
    merge(lista, start, middle, ends) #junta todas as partes

def merge(lista, start, middle, ends):
    part1 = lista[start:middle] 
    part2 = lista[middle:ends]
    top1, top2 = 0, 0 #o indice do primeiro elemento de cada parte
    for n in range(start, ends): #percorre os nums de cada parte do inicio ao fim
      if top1 >= len(part1): #se o valor do indice for maior que o tamanho da lista, já olhou todos
        lista[n] = part2[top2] #então coloca o da outra parte
        top2 += 1
      elif top2 >= len(part2):
        lista[n] = part1[top1]
        top1 += 1
      elif part1[top1] < part2[top2]: #verifica o menor das duas partes e coloca na lista
        lista[n] = part1[top1]
        top1 += 1
      else:
        lista[n] = part2[top2]
        top2 += 1

lista = [7, 5, 1, 8, 3]
mergesort(lista)
print(lista)