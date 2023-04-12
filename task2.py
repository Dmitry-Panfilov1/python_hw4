n = int(input('Enter the size of the list_1: '))
list_1 = []
for i in range(n):
    list_1.append(int(input(f'Enter {i + 1} eltment of the list_1: ')))
print(*list_1)
max_berries = 0
for i in range(len(list_1)):
    if i == len(list_1) - 1:
        if list_1[i - 1] + list_1[i] + list_1[0] > max_berries:
            max_berries = list_1[i - 1] + list_1[i] + list_1[0]
    else:
        if list_1[i - 1] + list_1[i] + list_1[i + 1] > max_berries:
            max_berries = list_1[i - 1] + list_1[i] + list_1[i + 1]
print(max_berries)