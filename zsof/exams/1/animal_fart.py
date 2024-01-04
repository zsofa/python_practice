# bemenet: dictionary [elephant: yes, giraffe: no]
# kimenet: egyik tupleban eltárolni az állatokat akik finganak a másikban akik nem


def separate_animals(d):
    farting_animals = tuple(animal for animal, farts in d.items() if farts == 'yes')
    non_farting_animals = tuple(animal for animal, farts in d.items() if farts == 'no')
    return farting_animals, non_farting_animals


animal_dict = {'elephant': 'yes', 'giraffe': 'no', 'dog': 'yes', 'cat': 'no'}

farting, non_farting = separate_animals(animal_dict)

print("Farting Animals:", farting)
print("Non-farting Animals:", non_farting)
