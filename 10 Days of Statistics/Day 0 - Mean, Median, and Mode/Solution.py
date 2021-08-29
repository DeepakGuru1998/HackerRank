# Enter your code here. Read input from STDIN. Print output to STDOUT
# Python 3

num = int(input())
samples = list(map(int, input().split()))

def mean(samples,num):
    add = 0
    for i in samples:
        add += i
    m = add/num
    return m

def median(samples, num):
    s = samples
    s.sort()
    if num%2 == 0:
        return (s[int(num/2) - 1] + s[int(num/2)]) / 2
    else:
        return (s[int(num/2)]) / 2

def mode(samples):
    dicti = {}
    for x in set(samples):
        dicti[x] = samples.count(x)
    l = list(dicti.values())
    l.sort()
    max = l[-1]
    if l.count(max) == 1:
        for i,j in dicti.items():
            if j == max: 
                return i
    else:
        n = []
        for i,j in dicti.items():
            if j == max:
                n.append(i)
        n.sort()
        return n[0]
    
print(mean(samples,num))
print(median(samples,num))    
print(mode(samples))
        

