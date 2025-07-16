def two_sum(numeros, alvo):
  size = len(numeros)

  for i in range(size):
    for j in range(i + 1, size):
      if numeros[i] + numeros[j] == alvo:
        return [i, j]
  
  return []

if __name__ == "__main__":
  result = two_sum([2, 7, 11, 15], 9)

  print(result)