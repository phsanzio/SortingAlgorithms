def insertion_sort(lista): #simula inserção, compara o "novo" com os anteriores
  for i in range(1, len(lista)):  #enquanto for menor, "empurra" os outros para frente
    atual = lista[i] #guarda o valor do elemento atual
    anterior = i - 1 #indice do elemento anterior
    while anterior >= 0 and lista[anterior] > atual: #enquanto o indice anterior for >= 0, vetor vai de 0..n E o elemento anterior for maior que o atual
      lista[anterior + 1] = lista[anterior] #coloca o anterior no lugar do próximo, o valor do antigo está em atual          
      anterior -= 1 #volta o indice para trás
    lista[anterior + 1] = atual #coloca no indice da frente, o elemento maior que estva guardado em atual

lista = [7, 5, 1, 8, 3]
insertion_sort(lista)
print(lista)