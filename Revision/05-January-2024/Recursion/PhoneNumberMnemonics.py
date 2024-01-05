def phoneNumberMnemonics(phoneNumber):
    mnemonics = []
    currentMnemonic = ['0'] * len(phoneNumber)
    
    phoneNumberMnemonicsHelper(0,phoneNumber,currentMnemonic,mnemonics)
    
    return mnemonics

def phoneNumberMnemonicsHelper(idx,phoneNumber,currentMnemonic,mnemonics):
    if idx == len(phoneNumber):
        mnemonics.append("".join(currentMnemonic))
    else:
        digit = phoneNumber[idx]
        letters = dialer[digit]
        for letter in letters:
            currentMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx+1,phoneNumber,currentMnemonic,mnemonics)

dialer = {
    "0":["0"],
    "1":["1"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}

print(phoneNumberMnemonics("1905"))