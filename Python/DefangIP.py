def defangIPaddr(address):

    #convert to mutable list
    lAddress = list(address)
    delim = ''
    
    for i in range(len(lAddress)):
        if lAddress[i] == ".":
            lAddress[i] = "[.]"
    return delim.join(lAddress) 



ip = "1.1.1.1.1"

print(defangIPaddr(ip))
