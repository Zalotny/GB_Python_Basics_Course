def convert_time(duration: int) -> str:
    str_result = ''
    period = 0
    period_limit = [86400, 3600, 60]
    period_names = ['дн', 'час', 'мин']
    str_is_not_empty = False
    for i in range(3):
        if duration >= period_limit[i]:
            period = duration // period_limit[i]
            str_result += f"{period} {period_names[i]} "
            str_is_not_empty = True
        elif str_is_not_empty:
            period = 0
            str_result += f"0 {period_names[i]} "
        duration -= period * period_limit[i]
    str_result += f"{duration} сек"
    return str_result


duration = 400153
result = convert_time(duration)
print(result)
