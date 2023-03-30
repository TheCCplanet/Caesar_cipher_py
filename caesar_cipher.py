plain_text = input("What is your plaintext? ")
shift = int(input("What is your shift?   between 0 - 25 :"))
cipher_code = list()
this_one = list()

#def outside(num,fst,last):
#     while True :
#        if num > last :
#            return "trt again"
#        elif num < fst :
#            break


def caesar(plain_text , shift):
    #plain_text = (plain_text).lower()
    cipher_range = int()

    for letter in plain_text :
        cipher_range = ord(letter) + shift
        if letter != ' '  and cipher_range <= 122:
            cipher_code.append(chr((ord(letter))+shift))
        elif letter == " " :
            cipher_code.append(chr(ord(letter)))
        elif cipher_range > 122 :
            cipher_code.append((chr((ord(letter))+shift-26)))
    return cipher_code
print (caesar(plain_text , shift))

def encode_caesar(text_code):
    cipher_range = int()
    for letter in text_code :
        difference = ord(letter) - ord("h")
        if difference < 0  and cipher_range <= 122 :
            cipher_code.append(chr((ord(letter))-(abs(difference))))
    return (cipher_code)

