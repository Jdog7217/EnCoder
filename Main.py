opening = input("Please type 1 for endoding or 2 for decoding: ")
if opening == str(1):
    

    start = input("Please type your message here: ")
    code = input("Please type your key, if you don't have a key please type no-key: ")
    if code.lower() == "no-key":
        import secrets
        code = secrets.token_urlsafe(64)
        
    Crow = bytearray(start, "utf8")


    by = []
    bys = ""
    for byte in Crow:
        bi = bin(byte)
        bys = str(bys)+"ob"+str(bi[2:])
        by.append(bi[2:])

    Cosmic = bytearray(code, "utf8")
    bya = []
    byas = ""
    for byte in Cosmic:
        bia = bin(byte)
        byas = str(byas)+str(bia[2:])
        bya.append(bia[2:])

    count = 0
    l = 0
    ending = ""

    for num in by:
        lettercount = 0

        for letter in num:
            if l >= int(len(byas))-1:
                l = 0
            if int(letter) + int(byas[l]) == 2:
                final = 0
            elif int(letter) + int(byas[l]) == 0:
                final = 0
            elif int(letter) + int(byas[l]) == 1:
                final = 1
            else:
                print("error")
            lettercount = lettercount+1
            ending = ending + str(final)
            l = l+1
        count = count +1
        ending = ending + " "

    print(f"Endoded message:\n{ending}")
    print(f"Key: {code}")
else:
    start = input("Please type your encoded message here: ")
    code = input("Please type your key: ")


    by = start.split()
    CosmicCrow = bytearray(code, "utf8")


    bya = []
    byas = ""
    for byte in CosmicCrow:
        bia = bin(byte)
        byas = str(byas)+str(bia[2:])
        bya.append(bia[2:])

    count = 0
    l = 0
    ending = ""
    for num in by:

        lettercount = 0

        for letter in num:
            if l >= int(len(byas))-1:
                l = 0

            if int(letter) + int(byas[l]) == 2:
                final = 0
            elif int(letter) + int(byas[l]) == 0:
                final = 0
            elif int(letter) + int(byas[l]) == 1:
                final = 1
            else:
                print("error")
            lettercount = lettercount+1
            ending = ending + str(final)
            l = l+1
        count = count +1
        ending = ending + " "
        

    bi = ending.split()


    ascii_string = ""
    for binary_value in bi:
        an_integer = int(binary_value, 2)



        ascii_character = chr(an_integer)



        ascii_string += ascii_character


    print("Done!")
    print("_____________________________________________________________________________________________________________")
    print(ascii_string)
    
print("Made by CosmicCrow")
im = input("Press enter to exit")
