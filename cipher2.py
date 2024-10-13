import string

letters = list(string.ascii_lowercase)
arrLen=len(letters)

def encryptString(text,shift):
    res=""
    for let in text:
        if(let==" "):
            res+=let
        else:
            pos=letters.index(let)+shift
            if(pos>arrLen):
                pos=arrLen-pos
            res+=letters[pos]
    return res

def decryptString(text,shift):
    res=""
    for let in text:
        if(let==" "):
            res+=let
        else:
            res+=letters[letters.index(let)-shift]
    return res

play=True

while(play):
    flag=input('''
    press 1 to encrypt
    press 2 to decrypt
    press 0 to quit
    ''')

    if(flag=='0'):
        print('Out of the loop')
        play=False
        break
    
    else:
        inText=input('Enter the string: ')
        inShift=int(input('Enter the shift: '))

        if(flag=='1'):
            input(f'Encrypted string is :{encryptString(inText,inShift)}')
        elif(flag=='2'):
            input(f'Decrypted string is :{decryptString(inText,inShift)}')
        else:
            input("INVALID CHOICE")
        

    
                