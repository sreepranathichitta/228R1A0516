def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
a1 = [1,2,3,4,5]
a2 = [3,5,2,1,7]

print(is_sorted(a1))
print(is_sorted(a2))
