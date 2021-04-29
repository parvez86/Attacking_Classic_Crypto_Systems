def decipher(text, key):
    result = ''
    for char in text:
        # if character is alphabet
        # then for the first 3 characters the decipher character will
        #   be cyclic 3rd previous character or the next (26-3)=23th characters
        # otherwise the decipher character will be the previous 3rd character
        if str.isupper(char):
            if ord(char) < (ord('A') + key):
                char = chr(ord(char)+26-key)
            else:
                char = chr(ord(char)-key)
        elif str.islower(char):
            if ord(char) < (ord('a')+key):
                char = chr(ord(char)+26-key)
            else:
                char = chr(ord(char)-key)
        result += char
    return result

# # encryption
# def cipher(text, key):
#     result = ""
#     for char in text:
#         if str.isupper(char):
#             if ord(char) > (ord('Z')-key):
#                 char = chr(ord(char) - (26-key))
#             else:
#                 char = chr(ord(char) + key)
#         elif str.islower(char):
#             if ord(char) > (ord('z')-key):
#                 char = chr(ord(char) - (26-key))
#             else:
#                 char = chr(ord(char) + key)
#         result += char
#     return result


if __name__ == '__main__':
    # taking input
    # text = input("Enter the ciphertext: ")
    # key = int(input("Enter the key (in number): "))
    text = "krclxrwrbxwnxocqnlxxunbcrwencrxwbrwanlnwccrvnb"
    for key in range(1, 26):
        plaintext = decipher(text, key)
        print("Plaintext (For key=%d): %s\n\n" % (key, plaintext))

    # actual key will be 9
    # for testing
    # print("Ciphertext:", cipher(plaintext, key))
