def dailyTemp(t):
    out = []
    for _ in t:
        out.append(0)
    for i in range(len(t)-2,-1,-1):
        j = i + 1
        while(j < len(t) and t[j] <= t[i]):
            if out[j] > 0:
                j = out[j] + j
            else:
                j = len(t)
        if j < len(t):
            out[i] = j - i
    return out

t = [73,69,72,76]

print(dailyTemp(t))

