def split_string(source,splitlist):
    L=[]
    H=[]
    G=[]
    i=0
    b=0
    L=list(splitlist)
    H=[source]

    while i<len(splitlist):
        H=[str(H[0]).replace(splitlist[i],"##########")]
        i=i+1

    b=str(H[0])
    c=b
    j=0
    G.append(b[0:b.find("##########")])
    while j<c.count("##########"):
        start=b.find("##########")+len("##########")
        end=b.find("##########",start)
        if end==-1:
           G.append(b[start:]) 
        else:
            G.append(b[start:end])
        b=b[end:]
        j=j+1
    while True:
        if "" in G:
            G.remove("")
        else:
            return G

print split_string("This is a test-of the,string separation-code!"," ,!-")
print split_string("After  the flood   ...  all the colors came out.", " .")
print split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
