#Question 3: Contains Duplicate LeetCode_Problem(217)

#Question 3: Contains Duplicate  WAY-1
tests = [[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]

if 1 <= len(tests) <= 100:
    for i in tests:
        for j in i:
            if -1000 <= j <= 1000:
                a = i.count(j)
                if a >= 2 :
                    print("True")
                    break
                else:
                    print('False')
                    break
            else:
                print("number is out of range")
                break
else:
    print('length is zero')




#Question 3: Contains Duplicate  WAY-2
tests = [[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]

for i in tests:
    seen = list()
    found = False
    for n in i:
        if n in seen:
            found = True
            break
        seen.append(n)
    print(found)



#Question 3: Contains Duplicate  WAY-3
tests = [[5, 6, 7], [4, 4], [9, 8, 7, 6, 5, 9], [1], [10, 20, 30, 40, 50, 10]]

for i in tests:
    seen = set()
    found = False
    for n in i:
        if n in seen:
            found = True
            break
        seen.add(n)
    print(found)
