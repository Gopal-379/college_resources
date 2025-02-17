# This program demonstrates PLAYFAIR CIPHER.
# Only lowercase letters are allowed.
# Ex1: PT: instruments  KEY: monarchy CT: gatlmzclrqxa
# Ex2: PT: informationsecurity  KEY: playfairexample  CT: rkaseipvekokrdlcbpxg
import numpy as np
plainText = input("Enter Plaintext: ")
key = input("Enter Key String: ")

l = []
i = 0
while i < len(plainText)-1:
    if(plainText[i]==plainText[i+1]):
        plainText = (plainText[:i+1] + "x" + plainText[i+1:])
    i+=1
if(len(plainText)%2!=0):
    plainText += "x"
print("\nModified Plain Text: ",plainText)

# Create matrix
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m = []
for i in range(5):
    m.append(['.'] * 5)
i = 0
j = 0
k = 0
while k < len(key):
    # add characters from key
    if key[k] not in m[0]+m[1]+m[2]+m[3]+m[4]:
        m[i][j] = key[k]
        if j == 4:
            i += 1
        j = (j + 1) % 5
    k += 1
k = 0
while k < len(alphabet):
    # add remaining characters from  alphabet
    if alphabet[k] not in m[0]+m[1]+m[2]+m[3]+m[4]:
        m[i][j] = alphabet[k]
        if j == 4:
            i += 1
        j = (j + 1) % 5
    k += 1
print("Matrix:\n",m)
mt = np.array(m).T.tolist()

# Create plain text pairs
k = 0
p = [] # plain text pairs
for i in range(int(len(plainText)/2)):
    p.append([plainText[k],plainText[k+1]])
    k += 2
print("Pairs:\n",p)

# FUNCTION FOR ENCRYPTION & DECRYPTION
def encrypt_decrypt(p,method): # method = 'e' means encryption, method = 'd' means decryption
    arr = []
    # for each pair
    for pi in range(len(p)):
        found0 = False
        found1 = False
        p0i = -1 # row number of 1st character in the pair
        p0j = -1 # column number of 1st character in the pair
        p1i = -1 # row number of 2nd character in the pair
        p1j = -1 # column number of 2nd character in the pair
        i = 0
        # get row and column numbers (indices) of the characters in the pair
        while not (found0 and found1):
            if p[pi][0] in m[i]:
                p0i = i
                p0j = m[i].index(p[pi][0])
                found0 = True
            if p[pi][1] in m[i]:
                p1i = i
                p1j = m[i].index(p[pi][1])
                found1 = True
            i += 1
        # if pair characters are in same row
        if p0i == p1i:
            if method == 'e':
                arr.append([m[p0i][(p0j+1) % 5], m[p0i][(p1j+1) % 5]])
            if method == 'd':
                arr.append([m[p0i][(p0j-1) % 5], m[p0i][(p1j-1) % 5]])
        # elif pair characters are in same column
        elif p0j == p1j:
            if method == 'e':
                arr.append([mt[p0j][(p0i+1) % 5], mt[p0j][(p1i+1) % 5]])
            if method == 'd':
                arr.append([mt[p0j][(p0i-1) % 5], mt[p0j][(p1i-1) % 5]])
        # else pair characters are in different row & col
        else:
            arr.append([m[p0i][p1j], m[p1i][p0j]])
    return arr

# ENCRYPTION
encryptedPairs = encrypt_decrypt(p,'e')
print("Encrypted Pairs:\n",encryptedPairs)
cipherText = ""
for pair in encryptedPairs:
    cipherText+=(pair[0]+pair[1])
print("\nCipher Text: ",cipherText)

# DECRYPTION
decryptedPairs = encrypt_decrypt(encryptedPairs,'d')
print("\nDecrypted Pairs:\n",decryptedPairs)
decryptedText = ""
for pair in decryptedPairs:
    decryptedText+=(pair[0]+pair[1])
print("\nDecrypted Text: ",decryptedText)