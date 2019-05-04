def lcs(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    memo = [[-1] * (l1+1) for x in range(l2+1)]
    sol = [[None for x in range(l1+1)] for x in range(l2+1)]

    for i in range(l1):
        for j in range(l2):
            if i == 0 or j == 0:
                q = 0
                memo[i][j] = 0
                sol[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
                sol[i][j] = 'd'
            elif memo[i-1][j] >= memo[i][j-1]:
                memo[i][j] = memo[i-1][j]
                sol[i][j] = 'l'
            else:
                memo[i][j] = memo[i][j-1]
                sol[i][j] = 'u'
    a=[]
    a.append(memo)
    a.append(sol)
    return a

def print_lcs(s1,b,i,j):
    l1 = len(s1)
    if i == 0 or j == 0:
        return
    if b[i][j] == 'd':
        print_lcs(s1,b,i-1,j-1)
        print(b[i])
    elif b[i][j] == 'u':
        print_lcs(s1,b,i,j-1)
    else:
        print_lcs(s1,b,i-1,j)

s1 = "hey im good"
s2 = "howdy yall"
a = lcs(s1,s2)
print_lcs(s1,a[1],len(s1),len(s2))
