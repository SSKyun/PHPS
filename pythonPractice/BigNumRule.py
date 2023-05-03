n, m, k = map( int, input().split() )

data = list(map(int, input().split()))

data.sort()

""" 어센딩오더로 정렬됨 """

first = data[n-1]
second = data[n-2]

result = 0

""" while True :
    # 가장 큰 수 k번 더하기
    for i in range(k) :
        if(m == 0 ) : break
        result += first
        m -= 1
    
    if m == 0 : break
    result+=second
    m -= 1 """


bnum = ((m//(k+1))*k)+(m%(k+1))
snum = bnum//k

realresult = (bnum*first) + (snum*second)


print(realresult)