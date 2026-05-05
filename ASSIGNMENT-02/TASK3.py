import random

def is_even (numbers):
    for n in numbers:
        print(f"number {n} is {"even" if n % 2 == 0  else "odd" }")

lst = [random.randint(0,10) for _ in range(20)]

average = sum(lst)/len(lst)
print(f"Average of the list: {average}")

print(lst)
print(f"The maximum element in the list is: {max(lst)}")
print(f"The minimum element in the list is: {min(lst)}")

numbers_greater_average = sum(1 for i in lst if i > average)
print(f"Number count greater than the average in the list is: {numbers_greater_average}")
is_even(lst)

print(f"Every second element in the list : {lst[::2]}")
print(f"Sorted list: {sorted(lst)}")
print(f"The second biggest number in the list is: {sorted(set(lst))[-2]}")

