n = int(input('Enter the size of the list_1: '))
m = int(input('Enter the size of the list_2: '))
list_1 = []
list_2 = []
for i in range(n):
    list_1.append(int(input(f'Enter {i + 1} eltment of the list_1: ')))
for j in range(m):
    list_2.append(int(input(f'Enter {j + 1} eltment of the list_2: ')))
list_new = []
for i in list_1:
    for j in list_2:
        if j == i:
            list_new.append(j)
for i in range(len(list_new) - 1):
    for j in range(len(list_new) - i - 1):
        if list_new[j] > list_new[j + 1]:
            list_new[j], list_new[j + 1] = list_new[j + 1], list_new[j]
print(*set(list_new))