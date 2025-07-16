def two_sum(numeros, alvo):
  indice_por_valor = {}

  for i, valor_atual in enumerate(numeros):
    valor_restante = alvo - valor_atual

    index_restante = indice_por_valor.get(valor_restante, None)

    if index_restante != None:
      return [i, index_restante]

    indice_por_valor[valor_atual] = i

if __name__ == "__main__":
  result = two_sum([2, 7, 11, 15], 9)

  print(result)