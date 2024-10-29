#affine Cipher Decryption

from math import gcd


#Start of Modular
def modular(a, alphabet):
    for x in range(1, alphabet):
        if (a * x) % alphabet == 1:
            return x
    return None
#END OF MODULAR 

def DECRYPTION(Cypher, a, b, alphabet):

    inverse = modular(a, alphabet)
    if inverse is None:
        return ""

    decrypted = ""

    for char in Cypher:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            x = (inverse * (y - b)) % alphabet
            decrypted += chr(x + ord('a'))
        else:
            decrypted += char
            
    return decrypted

    
def BRUTEFORCE(Cypher):

    alphabet = 26
    
    Alpha = [a for a in range(1, alphabet) if gcd(a, alphabet) == 1]
    outcomes = []

    for a in Alpha:
        for b in range(alphabet):
            answer = DECRYPTION(Cypher, a, b, alphabet)
            outcomes.append(f"a = {a}, b = {b} decode into: {answer}")
    return outcomes
    

#indput
Cypher = input("Please enter the Cypher: ")

print("Starting Cypher = " + Cypher)


outcomes = BRUTEFORCE(Cypher)

for outcome in outcomes:
    print(outcome)

    
