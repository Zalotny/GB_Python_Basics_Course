def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum_result = 0
    for dataset_elem in dataset:
        sum_numbers = 0
        dataset_elem10 = dataset_elem
        while dataset_elem10 // 10 > 0:
            sum_numbers += dataset_elem10 - dataset_elem10 // 10 * 10
            dataset_elem10 //= 10
        sum_numbers += dataset_elem10
        if sum_numbers % 7 == 0:
            sum_result += dataset_elem
    return sum_result


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    dataset17 = []
    for dataset_elem in dataset:
        dataset17.append(dataset_elem + 17)
    return sum_list_1(dataset17)


def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7
        (п.'c' - без создания нового списка)"""
    for idx, dataset_elem in enumerate(dataset):
        dataset[idx-1] += 17
    return sum_list_1(dataset)


my_list = []  # Соберите нужный список по заданию
for i in range(1, 1001, 2):
    my_list.append(i ** 3)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)
