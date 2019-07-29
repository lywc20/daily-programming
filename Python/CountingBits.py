def countingBits(inp):
    result = []
    for i in range(inp):
        count = 0
        while i > 0:
            if i%2 == 1:
                count += 1
            i = i//2
        result.append(count)
    return result

def improved(inp):
    result = [0]
    power, p = 1, 1
    for i in range(1,inp+1):
        if i == power:
            result.append(1)
            power = power << 1
            p = 1
        else:
            result.append(result[p] + 1)
            p += 1
    return result
x = improved(0)
print(x)
