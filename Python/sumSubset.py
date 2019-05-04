def naiveSum(arr, index, rem):
    if rem != 0 and index < 1:
        return False
    elif rem == 0:
        return True

    return naiveSum(arr,index - 1, rem) or naiveSum(arr,index - 1, rem - arr[index - 1])

arr = [34,4,5]

print(naiveSum(arr,len(arr),9))