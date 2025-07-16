def quicksort(array):
  _quicksort(array, 0, len(array) - 1)

def _quicksort(array, left, right):
  if left < right:
    pi = partition(array, left, right)
    _quicksort(array, left, pi - 1)
    _quicksort(array, pi + 1, right)

def partition(array, left, right):
  pivot = array[right]
  i = left - 1
  for j in range(left, right):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
  array[i + 1], array[right] = array[right], array[i + 1]
  return i + 1

def two_sum(numeros, alvo):
  quicksort(numeros)

  size = len(numeros)

  i, j = 0, size - 1

  while i < j:
    sum_result = numeros[i] + numeros[j]

    if sum_result < alvo:
      i += 1
    elif sum_result > alvo:
      j -= 1
    else:
      return [i, j]

  return []

if __name__ == "__main__":
  result = two_sum([2, 7, 11, 15], 9)

  print(result)