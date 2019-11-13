def AnagramGroup(strs):
    dic = {}
    for item in sorted(strs):
        sortedItem = sorted(item)
        dic[sortedItem] = dic.get(sortedItem,[]) + [item]
    return dic.values()
