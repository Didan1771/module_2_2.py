
first = input(int)
second = input(int)
third = input(int)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)