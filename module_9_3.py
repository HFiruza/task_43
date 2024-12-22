first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(string_1) - len(string_2) for string_1, string_2 in zip(first, second)
                if len(string_1) != len(string_2))
second_result = ((len(first[i]) == len(second[i])) for i in range(len(first) and len(second)))

print(list(first_result))
print(list(second_result))