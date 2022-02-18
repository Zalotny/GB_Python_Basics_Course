def get_uniq_numbers(src: list):
    set_unic = set()
    set_tmp = set()
    for num in src:
        if num not in set_tmp:
            set_unic.add(num)
        else:
            set_unic.discard(num)
        set_tmp.add(num)

    list_unic = [num for num in src if num in set_unic]
    return list_unic


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
