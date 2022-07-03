numbers = list(range(0, 20))
def sequential_search(list, n):
    found = False
    for i in list:
        if i == n:
            found = True
            break
    return found

print(sequential_search(numbers, 5))
