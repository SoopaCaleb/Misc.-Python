# Iterative Encryptor
# Encrypts a user message as many times as desired with optional random key generation

import random

original_characters = list("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;:'.,(){}[]!£$%^&*/+-=_")
encryption_key_to_use = "Invalid"
valid_num_iterations = False

# Generates the encryption key

def generate_encryption_key():
    generated_encryption_key = []
    while len(generated_encryption_key) < len(original_characters):
        x = random.randrange(0, len(original_characters))
        if not original_characters[x] in generated_encryption_key:
            generated_encryption_key.append(original_characters[x])
    return generated_encryption_key

premade_encryption_key = list("8*1(:9Xm5s^=A/kxzepYhJQ'%yjVNo;&vEIfc2.n7w£,dTWPb60Kt}{ClMG)aZ[3RFrS4+iOgUD$-L!uH]q_B")

# Iterable Encryption System (returned as string)

def encrypt(x, num_repeats, preferred_encryption_key):
    y = list(x)
    z = list(x)
    for i in range(num_repeats):
        for j in range(len(y)):
            for k in range(len(original_characters)):
                if y[j] == original_characters[k]:
                    z[j] = preferred_encryption_key[k]
        y = z
    w = "".join(z)
    return w

# Allows for encryption key option to be decided upon

def encryption_decision(a):
    match a:
        case "1":
            return generate_encryption_key()
        case "2":
            return premade_encryption_key
        case _:
            print("Invalid Input. Try Again.")
            return "Invalid"

# User input system

encryption_input = input("Type in a message to encrypt: ")
while encryption_key_to_use == "Invalid":
    print("Press 1 to generate a new encryption key for this encryption.")
    print("Press 2 to use the premade encryption key")
    decision_input = input()
    encryption_key_to_use = encryption_decision(decision_input)
    while not valid_num_iterations:
        num_iterations = input("Enter number of iterations desired here: ")
        try:
            num_iterations = int(num_iterations)
            if num_iterations < 1:
                print("Invalid Number of Iterations. Try Again.")
            else:
                valid_num_iterations = True
        except ValueError as ve:
            print("Invalid Number of Iterations. Try Again.")
    print("Your encrypted result is: " + encrypt(encryption_input, num_iterations, encryption_key_to_use))
