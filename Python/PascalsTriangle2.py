def makeTri(N):
    out = []
    out.append([1])
    out.append([1,1])
    for i in range(2,N+1):
        out2 = [1]
        for j in range(1,len(out[i-1])):
            res = out[i-1][j-1]+out[i-1][j]
            out2.append(res)
        out2.append(1)
        out.append(out2)
    return out

def makeTri2(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = (x+y for x,y in zip([0]+row,row+[0]))
    return row
print(makeTri2(3))
