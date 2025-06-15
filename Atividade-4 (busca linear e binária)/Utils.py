def generate_unordered_array():
  return [54, 91, 12, 76, 3, 45, 88, 23, 67, 99]
  # return [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

def quicksort(array):
  _quicksort(array, 0, len(array) - 1)

def _quicksort(arr, left, right):
  if left < right:
    pi = _partition(arr, left, right)
    _quicksort(arr, left, pi - 1)
    _quicksort(arr, pi + 1, right)

def _partition(arr, left, right):
  pivot = arr[right]
  i = left - 1

  for j in range(left, right):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[right] = arr[right], arr[i + 1]

  return i + 1