import random

def get_grade(score):
    if score > 90:
        return  5
    elif score > 75:
        return 4
    elif score > 60:
        return 3
    else:
        return 2


lst = [random.randint(0,100) for i in range(50)]

passing_students = 0
for i in lst:
    print(f"student: {i}'s grade is: {get_grade(i)}")


passing_students = sum(1 for score in lst if get_grade(score) >2)
print(f"This many students have passed {passing_students}")

average = sum(lst)/len(lst)
print(f"average is : {average}")

top5 = sorted(lst, reverse=True)[:5]
print(f"Top 5 scores: {top5}")


