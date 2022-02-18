def get_numbers(src: list):
    return (num for i, num in enumerate(src) if i > 0 and src[i-1] < num)


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
