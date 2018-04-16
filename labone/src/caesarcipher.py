
key = 'abcdefghijklmnopqrstuvwxyz'


def encrypt_caesar(n, content):
    result = ''
    for l in content.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()


def decrypt_caesar(n, encryptedtxt):
    result = ''
    for l in encryptedtxt:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result


f = open("one.txt", "r")
if f.mode == 'r':
    z = f.read().splitlines()
    f.close()
    for text in z:
        print(text)

offset = 1

encrypted = encrypt_caesar(offset, text)
print('Encrypted using caesar cipher :', encrypted)

decrypted = decrypt_caesar(offset, encrypted)
print('Decrypted using caser cipher:', decrypted)

