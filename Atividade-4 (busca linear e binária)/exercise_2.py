import Utils

array = Utils.generate_unordered_array()
Utils.quicksort(array)

# Calcular o índice h usando *busca linear*

def calc_h_index_with_linear_search(array):
  h_index = 0

  for index in range(len(array) - 1, -1, -1):
    index_value = array[index]

    if index_value > h_index:
      h_index += 1
    else:
      break
    
  return h_index

print(f"O valor índice h é {calc_h_index_with_linear_search(array)}\n")

# Encontrar a posição de um valor -- ou onde ele deve ser inserido -- usando *busca binária*

def calc_h_index_with_binary_search(array):
  n = len(array)
  
  left, right = 0, n - 1
  h_index = 0

  while left <= right:
    mid = (left + right) // 2
    h = n - mid
    if array[mid] >= h:
      h_index = h
      right = mid - 1
    else:
      left = mid + 1

  return h_index

print(f"O índice h é {calc_h_index_with_binary_search(array)}")