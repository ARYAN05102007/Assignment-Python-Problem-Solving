#Question 2 : [Palindrome Number] LeetCode_Problem(9)

tests = [12321, -5, 100, 7, 1221, 120021]

for x in tests:
    if -1000000 <= x <= 1000000:
        a = str(x)
        b = a[::-1]
        if b == str(x):
            print('TRUE')
        else:
            print('FAlSE')
    else:
        print(x , '  this value is not in range ')
