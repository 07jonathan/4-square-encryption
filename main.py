def generate_squares(key1, key2):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J are merged because Four-Square Cipher treats them as the same

    def create_square(key):
        square = []
        letters_used = set()
        for char in key.upper():
            if char not in letters_used and char in alphabet:
                letters_used.add(char)
                square.append(char)
        for char in alphabet:
            if char not in letters_used:
                letters_used.add(char)
                square.append(char)
        return ''.join(square)[:25]

    # The upper-left and lower-right squares are the standard alphabet
    plain1 = alphabet
    plain2 = alphabet
    # The other two squares are created using the keys
    cipher1 = create_square(key1)
    cipher2 = create_square(key2)

    return plain1, plain2, cipher1, cipher2


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    return text


def encrypt(plaintext, key1, key2):
    plain1, plain2, cipher1, cipher2 = generate_squares(key1, key2)
    plaintext = prepare_text(plaintext)

    ciphertext = []
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = divmod(plain1.index(char1), 5)
        row2, col2 = divmod(plain2.index(char2), 5)
        ciphertext.append(cipher1[row1 * 5 + col2])
        ciphertext.append(cipher2[row2 * 5 + col1])

    return ''.join(ciphertext)


def decrypt(ciphertext, key1, key2):
    plain1, plain2, cipher1, cipher2 = generate_squares(key1, key2)

    plaintext = []
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = divmod(cipher1.index(char1), 5)
        row2, col2 = divmod(cipher2.index(char2), 5)
        plaintext.append(plain1[row1 * 5 + col2])
        plaintext.append(plain2[row2 * 5 + col1])

    return ''.join(plaintext)


# Example usage:
plaintext = "testplaintext"
key1 = "example"
key2 = "keyword"

encrypted_text = encrypt(plaintext, key1, key2)
print(f"Encrypted: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, key1, key2)
print(f"Decrypted: {decrypted_text}")
