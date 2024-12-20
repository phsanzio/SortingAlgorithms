def bubble_sort(lista): #compara com o próximo e troca se necessário
  for j in range(len(lista) - 1): #roda todos os nums, menos o último porque não tem nenhum depois
    for i in range(len(lista) - 1 - j): #rodar o próximo elemento
      if lista[i + 1] < lista[i]: #pega o primeiro e o próximo
        lista[i], lista[i + 1] = lista[i + 1], lista[i] #se o próximo for menor troca os dois de lugar
      

lista = [7, 5, 1, 8, 3]
bubble_sort(lista)
print(lista)