# Designer Door Mat 

N,M = map(int, input().split())
M = N * 3
n = M
mid = N//2
high = 1
for i in range(N):
    if mid != i:
        text = ".|."*high 
        print(text.center(n,"-"))
        high = high + 2
        low = high - 2
        j = i 
    else:
        print("WELCOME".center(n,"-"))
        for j in range (N-j):
            text = ".|."*low
            print(text.center(n,"-"))
            low = low - 2
            if low < 1:
                break
        break
