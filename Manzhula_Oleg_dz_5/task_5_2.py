"""Генератор нечётных чисел от 1 до n (включительно) не используя ключевое слово yield"""
n = 15
generator = (num for num in range(1, n + 1, 2))
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

"""Если не использовать код предыдущего задания, то можно заменить код строк 4-7 на одну строку:"""
# print(*(num for num in range(1, n + 1, 2)), sep='\n')
