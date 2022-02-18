tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    delta = len(tutors) - len(klasses)
    if delta > 0:
        klasses.extend([None] * delta)  # в задаче нет условия сохранить списки неизменными иначе - создал бы новый
    zipped_couples = zip(tutors, klasses)
    for couple in zipped_couples:
        yield couple


generator = check_gen(tutors, klasses)
print(generator)  # добавьте здесь доказательство, что создали именно генератор
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
