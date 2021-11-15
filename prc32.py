n = int (input())
product = 1
for i in range(1,n+1,1):
    product = product * i
    print(product)

def unique(S,N):
    ans = "NO"
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans = "NO"
            print(ans)
            return
        elif S[i] != S[i+1]:
            ans = "YES"
    print(ans)
S=input()
N=len(S)
unique(S,N)