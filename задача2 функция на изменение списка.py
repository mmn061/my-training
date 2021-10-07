lst = [10, 5, 8, 3]


def modify_list(l):
    lstm = []
    for i in l:
        if i % 2 == 0:
            lstm.append(int(i / 2))
    l.clear()
    for j in lstm:
        l.append(j)


print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]

modify_list(lst)
print(lst)  # [1]
