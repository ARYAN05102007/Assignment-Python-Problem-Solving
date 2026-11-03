#Question 1 [Fizz Buzz] LeetCode_Problem(412)

string = 'FizzBuzz'
tests = [4, 6, 10, 15]
l=[]
for j in tests:
    if 1 <= j <= 100:
        for i in range(1,j+1):
            if i%3==0 and i%5==0:
                l.append('FizzBuzz')

            elif i%3 == 0:
                l.append('Fizz')

            elif i%5 == 0:
                l.append('Buzz')

            else:
                l.append(str(i))
        print(l)
        l=[]

    else:
        print('NUMBER NOT IN RANGE !')
