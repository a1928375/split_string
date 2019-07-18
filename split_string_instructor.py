def split_string(source,splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                output[-1] = output[-1] + char
    return output

print split_string("This is a test-of the,string separation-code!"," ,!-")
print split_string("After  the flood   ...  all the colors came out.", " .")
print split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
