import heapq

def merge_k_lists(lists)->list:
    """ Злиття k відсортованих списків """
    
    # Створюємо купу
    min_heap = []

    # Додаємо перший елемент кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            # Додаємо кортеж (значення, індекс списку, індекс елемента)
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []

    # Витягуємо мінімальний елемент і додаємо наступний елемент із того ж списку
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # Додаємо наступний елемент із того ж списку, якщо він існує
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return result

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Списки перед злиттям:", lists)

    merged_list = merge_k_lists(lists)

    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()
