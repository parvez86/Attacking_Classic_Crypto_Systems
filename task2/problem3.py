def cipher(text, key):
    # encryption:
    # ciphertext[i] = (plaintext[i] + key[i]) % 26

    text = text.lower()
    key = key.lower()
    length = len(text)
    ciphertext = ''
    key_length = len(key)
    j = 0
    for i in range(length):
        if str.isalpha(text[i]):
            # as ord('a') = 97, so ord(A) + ord(A) = 97+97 = 194
            ciphertext += chr((ord(text[i])+ord(key[j % key_length])-194) % 26 + 97)
            j += 1
        else:
            ciphertext += text[i]
    return ciphertext


def decipher(text, key):
    # decryption:
    # plaintext[i] = (ciphertext[i] - key[i] + 26) % 26

    text = text.lower()
    key = key.lower()
    length = len(text)
    deciphertext = ''
    key_length = len(key)
    j = 0
    for i in range(length):
        if str.isalpha(text[i]):
            deciphertext += chr((ord(text[i]) - ord(key[j % key_length]) + 26) % 26 + 97)
            j += 1
        else:
            deciphertext += text[i]
    return deciphertext


if __name__ == '__main__':

    # text = input("Enter your text: ")
    # key = input("\nEnter the key: ")
    # option_type = int(input("\nEnter the option (1 for encryption, 2 for decryption): "))

    text = """
    Ethereum is an open-source, public, blockchain-based distributed
    computing platform and operating system featuring smart contract functionality
    """
    key = "pinkfloyd"

    ciphertext = cipher(text, key)
    print("Cipher text: ", ciphertext)

    plaintext = decipher(ciphertext, key)
    print("Plain text: ", plaintext.strip().capitalize())