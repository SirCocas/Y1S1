from saes import saes


def main():
    print("Testing S-AES...")
    SAES = saes("aaaa12aaaasdasddasdsadasddaa", "xxxxxxxxxxxxxxxx")


    SAES.currentLoop = SAES.special_round_time
    
    toTest = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]]

    print("TESTING ADDROUNDKEY...")

    SAES.state = toTest
    SAES.addRoundKey()
    SAES.addRoundKey()
    if(toTest == SAES.state):
        print(toTest)
        print(SAES.state)
        print("ADDROUNDKEY passed!")

    else:
        print("Error in ADDROUNDKEY")

    print("TESTING SUBBYTES...")
    SAES.state = toTest
    SAES.subBytes()
    SAES.inv_sub_bytes()
    if(toTest == SAES.state):
        print(toTest)
        print(SAES.state)
        print("SUBBYTES passed!")
    else:
        print("Error in SUBBYTES")

    print("TESTING SHIFTROWS...")
    SAES.state = toTest
    SAES.shift_rows()
    SAES.inv_shift_rows()
    if(toTest == SAES.state):
        print(toTest)
        print(SAES.state)
        print("SHIFTROWS passed!")
    else:
        print("Error in SHIFTROWS")


    print("TESTING MIXCOLUMNS...")
    SAES.state = toTest
    SAES.mix_columns()
    SAES.inv_mix_columns()
    if(toTest == SAES.state):
        print(toTest)
        print(SAES.state)
        print("MIXCOLUMNS passed!")
    else:
        print("Error in MIXCOLUMNS")
    
    


    print("Is the reverse s_box equal to inverting the s_box?")
    print(SAES.rev_s_box == SAES.invert(SAES.s_box))

    print("Testing decrypt(encrypt(X))")
    toCipher="asdasd"
    print(toCipher)
    print(SAES.decrypt(SAES.encrypt(toCipher)))
    print(SAES.result)
    
main()
