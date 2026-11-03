#Question 5: Best Time to Buy and Sell Stock  LeetCode_Problem(121)

tests = [[2, 4, 1], [3, 3, 5, 0, 0, 3, 1, 4], [1, 2, 3, 4, 5], [5], [10, 9, 8, 12]]

for i in tests:
    n=len(i)
    max_profit=0
    for j in range(n):
        for k in range(j+1,n):
            p=i[k]-i[j]
            if p > max_profit:
                max_profit=p
    print(max_profit)
