#tasks = ['a','a','a','b','b','b','c','a']
tasks =["A","A","A","A","A","A","B","C","D","E","F","G"]

def leastInterval(t,n):
    counter = [0] * 26
    maxx = 0
    maxCounter = 0
    for i in t:
        if maxx == counter[str(i) - 'A']:
            macCounter += 1
        elif maxx < counter[str(i)-'A']:
            maxx = counter[str(i)-'A']
            maxCounter = 1
    partCount = max - 1
    partLen = n - (maxCounter - 1)
    emptySlots = partCount * partLen
    avail = len(t) - maxx * maxCounter
    idles = max(0,emptySlots - avail)
    return len(t) + idles
print(leastInterval(tasks,2))
