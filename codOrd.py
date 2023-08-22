# Função para contar as operações fundamentais
def count_operations(func):
    def wrapper(arr):
        global operations
        operations = 0
        sorted_arr = func(arr)
        print("Número de operações fundamentais:", operations)
        return sorted_arr
    return wrapper

# Implementação do Insertion Sort
@count_operations
def insertion_sort(arr):
    global operations
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            operations += 2  # Contabiliza comparação e troca
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        operations += 1  # Contabiliza a atribuição
    return arr

# Implementação do Merge Sort
@count_operations
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            operations += 2  # Contabiliza comparação e atribuição

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            operations += 1  # Contabiliza a atribuição

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            operations += 1  # Contabiliza a atribuição

        return arr

# Exemplo de uso
arr = [12, 11, 13, 5, 6]
print("Array original:", arr)
sorted_arr_insertion = insertion_sort(arr.copy())
sorted_arr_merge = merge_sort(arr.copy())
print("Insertion Sort:", sorted_arr_insertion)
print("Merge Sort:", sorted_arr_merge)
