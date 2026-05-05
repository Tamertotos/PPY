import random
import string

list1 = [random.randint(1,20) for i in range(random.randint(8,16))]
print(list1)
print(list1[0::2])
print("=================")
list2 = [random.randint(0,50) for _ in range(random.randint(10,20))]
print(list2)
print(list2[3:8])
print("=================")
list3 = [random.choice(string.ascii_lowercase) for _ in range(random.randint(6,12))]
print(list3)
print(list3[::-1])
print("=================")
list4 = [random.randint(1,5) for _ in range(random.randint(9,15))]
print(list4)
print(list4[::-3])
print("=================")
list5 = [random.randint(1,20) for _ in range(random.randint(6,12))]
print(list5)
print(list5[:3] , list5[-3::])
print("=================")
list6 = [random.randint(0,50) for _ in range(random.randint(10,20))]
print(list6)
print(list6[2:9:2])
print("=================")
list7 = [random.choice(string.ascii_lowercase) for _ in range(random.randint(5,10))]
print(list7)
list8 = list7[:2] + list7[-2:]
print(list8)
print("=================")
list9 = [random.randint(1,50) for _ in range(random.randint(10,20))]
print(list9)
print(list9[1:-1])
print("=================")
list10 = [random.choice(string.ascii_lowercase) for _ in range(random.randint(8,12))]
print(list10)
print(list10[-1::-3])
print("=================")
list11 = [random.randint(0,50) for _ in range(random.randint(10,15))]
print(list11)
list12 = [random.randint(0,50) for _ in range(len(list11))]
print(list12)
list11[2:6] = list12[2:6]
print(list11)
print("=================")
list13 = [random.randint(0,50) for _ in range(random.randint(8,12))]
print(list13)
del list13[4:]
print(list13)
print("=================")
list14 = [random.randint(0,20) for _ in range(random.randint(10,15))]
print(list14)
print(list14[8:1:-1])
print("=================")
list15 = [random.randint(0,50) for _ in range(random.randint(5,10))]
print(list15)
copy = list15[:]
print(copy)
print("=================")
list16 = [random.randint(0,50) for _ in range(random.randint(10,20))]
print(list16)
list17 = list16[::2]
print(list17)
print("=================")
list18 = [random.choice(string.ascii_lowercase) for _ in range(random.randint(7,12))]
print(list18)
print(list18[::-2])