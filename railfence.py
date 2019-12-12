def change(flag,counter):
    
    if(flag == 0):
        counter += 1
        return counter
    else:
        counter -= 1
        return counter


def railfence(text,val):
    ar = [[] for i in range(val)]
    counter = 0
    flag = 0
    for i in text:
        ar[counter].append(i)
        if(counter == val-1):
            flag = 1
        elif(counter == 0):
            flag = 0
        counter = change(flag,counter)
    final = []
    for i in range(len(ar)):
        final.extend(ar[i])
    return "".join(final)

def get(b,key,ar):
    return b[key][ar[key]]

def railfencedecrypt(enpt,val):
    ar = [0 for i in range(val)]
    counter = 0
    flag = 0
    for i in enpt:
        ar[counter] += 1
        if(counter == val-1):
            flag = 1
        elif(counter == 0):
            flag = 0
        counter = change(flag,counter)
    b = []
    base = 0
    for i in ar:
        b.append(enpt[base:base+i])
        base = base + i
    #reconstructed with apt partitions. contained in b
    text = ""
    for i in range(val):
        ar[i] = 0
    key = 0
    flag = 0
    for i in range(len(enpt)):
        text += get(b,key,ar)
        ar[key] += 1
        key = change(flag,key)
        if(key == 0):
            flag = 0
        elif(key == val-1):
            flag = 1
    return text
    
    


if __name__ == "__main__":
    orignalmessage = "Sarvesh Bhatnagar"
    print("Orignal Message: "+orignalmessage)
    enpt = railfence(orignalmessage,4)
    print("Encrypted Message: " + enpt)
    enptt = railfence(enpt,3)
    print("Double Encryption: "+ enptt)
    st = railfencedecrypt(enptt,3)
    print("first lvl decrypt: "+st)
    print("Decrypted Message: "+railfencedecrypt(st,5))
    

    
