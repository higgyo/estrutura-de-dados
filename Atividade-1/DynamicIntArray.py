class DynamicIntArray:

    def __init__(self, capacity=2):

        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")

        self.capacity = capacity
        self.size = 0
        self.data = [0] * self.capacity

    # is_empty

    def is_empty(self):

        return self.size == 0



    # get (faça validação de index fora dos limites.)

    def get(self, searched_index):
        if searched_index < 0 or searched_index >= self.size:
            IndexError("Index fora dos limites")

        return self.data[searched_index]




    # set (faça validação de index fora dos limites.)

    def set(self, index_to_set, new_value):
        if index_to_set < 0 or index_to_set >= self.size:
            IndexError("Index fora dos limites")

        self.data[index_to_set] = new_value

    def append(self, value):

        if self.size == self.capacity:
            self._resize_up(2 * self.capacity)

        self.data[self.size] = value
        self.size += 1



    def _resize_up(self, new_capacity):

        print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")

        new_data = [0] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def _resize_down_if_necessary(self):
        
        if self.size / self.capacity <= 0.25:
            
            new_capacity = self.capacity // 2

            print(f"⏬ Redimensionando de {self.capacity} para {new_capacity}")
            
            new_data = [0] * new_capacity

            for index in range(self.size):
                new_data[index] = self.data[index]

            self.data = new_data
            self.capacity = new_capacity


    # remove_at

    # remover elemento no index passado.

    # Reduzir a capacidade da Lista pela metade se 25% ou menos (<= 25%) do seu espaço estiver sendo usado

    # Exemplo, na lista de capacidade 8 com os seguintes valores [10, 99, 50],

    # ao remover um elemento sua capacidade deve cair de 8 para 4 e a lista ficar [10, 99] com capacidade 4. 

    # validar index fora dos limites.

    # retornar o valor removido.

    # Imprimir a seguinte mensagem quando for o caso: ⏬ Redimensionando de {self.capacity} para {new_capacity}

    def remove_at(self, index_to_remove):
        if index_to_remove < 0 or index_to_remove >= self.size:
            IndexError("Index fora dos limites")

        for index in range(index_to_remove, self.size):
            self.data[index] = self.data[index + 1]

        self.size -= 1

        self._resize_down_if_necessary()


    # remove

    # remove o elemento buscado caso exista.

    # mesmas regras do remove_at.

    def remove(self, value_to_remove):
        removed = False

        for index in range(self.size):
            if self.data[index] == value_to_remove and not removed:
                removed = True
                self.size -= 1
              
            if removed:
                self.data[index] = self.data[index + 1]

        self._resize_down_if_necessary()

    # insert_at

    # com os parametros de index e valor a ser inserido.

    # respeitando as regras de aumento da lista.

    # def insert_at(self, index, value):
    
    def insert_at(self, index_to_insert, value_to_insert):
        
        if index_to_insert < 0 or index_to_insert > self.size:
            raise IndexError("Index fora dos limites")
        
        new_data = self.data[:index_to_insert] + [value_to_insert] + self.data[index_to_insert:]

        self.data = new_data
        self.size += 1

        if self.size == self.capacity:
            self._resize_up(self.capacity * 2)
          


    # index_of

    # retorna o index do valor buscado ou -1 caso não exista.

    def index_of(self, searched_value):

        for index in range(self.size):
            if self.data[index] == searched_value:
                return index
            
        return -1



    # contains

    # retorna True ou False se encontrou ou não o valor buscado.

    def contains(self, searched_value):
        if self.is_empty():
            return False
        
        for index in range(self.size):
            if self.data[index] == searched_value:
                return True
            
        return False

    def __str__(self):

        return str(self.data[:self.size])
