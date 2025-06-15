import Utils

array = Utils.generate_unordered_array()
Utils.quicksort(array)

# Encontrar a posição de um valor -- ou onde ele deve ser inserido -- usando *busca linear*

def find_index_with_linear_search(array, value):
  for index in range(len(array)):
    index_value = array[index]

    if index_value >= value:
      return index
    
  return len(array)

searched_value = int(input("Informe o valor que deseja buscar: "))

print(f"O valor está, ou deve ser inserido, no índice {find_index_with_linear_search(array, searched_value)}\n")

# Encontrar a posição de um valor -- ou onde ele deve ser inserido -- usando *busca binária*

def find_index_with_binary_search(array, value):
  left, right = 0, len(array) - 1

  while left <= right:
    mid = (left + right) // 2

    if array[mid] >= value:
      right = mid - 1
    else:
      left = mid + 1

  return left

searched_value = int(input("Informe o valor que deseja buscar: "))

print(f"O valor está, ou deve ser inserido, no índice {find_index_with_binary_search(array, searched_value)}")