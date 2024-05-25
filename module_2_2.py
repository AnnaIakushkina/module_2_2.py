# 1 вариант
first = 56
second = 34
third = 79
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second and first != third and second != third:
    print(0)
else:
    print(10)

# 2 вариант

first = 5
second = 5
third = 9
if first == second and first == third and second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
elif first == second or first == third or second == third:
    print(2)
else:
    print(10)


