#Question 6: Roman to Integer LeetCode_Problem(13)
tests = ["III","IX", "XL", "MMXXIV", "CDXLIV", "XIV"]
l= []
I ,V ,X ,L ,C ,D ,M = 1 ,5 ,10 ,50 ,100 ,500 ,1000
for i in tests:
    for j in i:
        if j=='I':
            l.append(1)
        if j=='V':
            l.append(5)
        if j=='X':
            l.append(10)
        if j=="L":
            l.append(50)
        if j=='C':
            l.append(100)
        if j=='D':
            l.append(500)
        if j=="M":
            l.append(1000)
    
    sum = 0
    a = l[0]
    
    for k in l:
        if k<=a:
            sum+=k
            a=k
        elif k>a:
            sum = sum +(k-a*2)
            a=k
            
    l=[]
    print(sum)
