#Question 4: Two Sum  LeetCode_Problem(1)
tests = [([1, 5, 8, 3], 11), ([10, 2, 7, 15], 9), ([6, 4, 9, 2], 8), ([-3, 4, 3, 90], 0)]

for i in range(len(tests)):
    target = tests[i][-1]
    for j in range(len(tests[i][0])):
        for k in range(j+1,len(tests[i][0])):
            a = tests[i][0][j]
            b = tests[i][0][k]
            if a+b == target:
                print(j ," ",k)
                break
