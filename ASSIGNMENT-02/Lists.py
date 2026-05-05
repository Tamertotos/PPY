import random
def create_list (min_len, max_len):
    len_of_list = random.randint(min_len,max_len)
    list1 = [random.randint(1,100) for _ in range(len_of_list)]
    return list1

print(create_list(1,5))
print("==========")
list2 = [random.randint(1,10) for _ in  range(5)]
print(list2)
print("==========")
list3 = [5,8,2,9,1]
print(list3[0], list3[-1])
print("==========")
count = 0
list4 = [3,7,2,9,4,5]
for _ in list4:
    count += 1
print(count)
print("==========")
list5 = [1,2,3]
for _ in range(4,8):
    list5.append(_)
print(list5)
list5.insert(0,0)
print(list5)
print("==========")
list6 = [1,2,3,4,5]
del list6[2]
print(list6)
list6.remove(4)
print(list6)
print("==========")
summation = 0
list7 = [5,8,2,9,1]
for _ in list7:
    summation += _
print(summation)
print("==========")
list8 = [12,7,19,3,8]
print(max(list8))
print(min(list8))
print("==========")
list9 = [1,2,3,4,5]
print(id(list9))
reversed_not_in_place_list9 = list9[::-1]
print(id(reversed_not_in_place_list9))
print(reversed_not_in_place_list9)
list9.reverse()
print(id(list9))
print(list9)
print("==========")
list10 = [4,1,7,3,9]
print(id(list10))
list10.sort()
print(id(list10))
print(list10)
list10.sort(reverse=True)
print(id(list10))
print(list10)
print("==========")
list11 = [1,2,3,4,5,6]
for i in list11:
    if i % 2 == 0:
        print(f"Even number {i}", end=' ')
print("\n==========")
list12 = [pow(i,2) for i in list11]
print(list12)
print("==========")
list13 = [1,2,3]
list14 = [4,5,6]
list15 = [i for i in list13] + [j for j in list14]
print(list15)
print("==========")
list16 = [1,2,2,3,4,4,5]
list_unique_items =  list(set(list16))
print(list_unique_items)
list_unique_itemsv2 = []
[list_unique_itemsv2.append(x) for x in list16 if x not in list_unique_itemsv2]
print(list_unique_itemsv2)
print("==========")
list17 = [1,2,3,4,5]
print(list17[::-1])
print("==========")
list18 = [3,5,7,9]
if 7 in list18:
    print("Yes 7 in the list")
print("==========")
list19 = [2,7,4,10,5]
result = sum(i for i in list19 if i > 5)
print(result)
print("==========")
list20 = ['a','b','c']
list21 = [i.upper() for i in list20]
print(list21)
print("==========")
list22 = ["Python","Java","Cpp"]
print(*list22 , sep='\n')
print("==========")
list23 = [1,3,2,3,4,3]
print(list23.count(3))
print("==========")
list24 = ['A','B','C']
print(''.join(list24))