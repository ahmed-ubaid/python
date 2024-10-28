import string

letters = list(string.ascii_lowercase)
arrLen=len(letters)
def encryptFunc(intxt,inSh):
    res=""
    for let in intxt:
        if let==" ":
            res+=let
        else:
            pos=letters.index(let)+inSh
            if pos>arrLen:
                pos=pos-arrLen
            res+=letters[pos]
    return res
def decryptFunc(intxt,inSh):
    res=""
    for let in intxt:
        if let==" ":
            res+=let
        else:
            res+=letters[letters.index(let)-inSh]
    return res

play=True

while play:
    cho=input('''
    press 1 for encrypt
    press 2 for decrypt
    press Q to quit
    :
    ''')
    if cho=="q":
        play=False
        break
    txt=input("    Enter the text: ")
    shift=int(input("   how much would you lke to shift"))

    if cho=="1":
        print(f"    your encrypted message: {encryptFunc(intxt=txt,inSh=shift)}")
    elif cho=="2":
        print(f"    your decrypted message: {decryptFunc(intxt=txt,inSh=shift)}")
