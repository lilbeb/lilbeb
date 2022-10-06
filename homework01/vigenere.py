import string

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    ind = 0
    for i in plaintext:
        if i.islower():
            cur = ord(keyword[ind]) - ord('a')
            enc = chr((ord(i) - ord('a') + cur) % 26 + ord('a'))
            ciphertext += enc
            ind = (ind + 1) % len(keyword)
        elif i.isupper():
            cur = ord(keyword[ind]) - ord('A')
            enc = chr((ord(i) - ord('A') + cur) % 26 + ord('A'))
            ciphertext += enc
            ind = (ind + 1) % len(keyword)
        else:
            ciphertext += i

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    ind = 0

    for i in ciphertext:
        if i.islower():
            cur = ord(keyword[ind]) - ord('a')
            dec = ord(i) - ord('a') - cur
            if dec < 0:
                dec += 26

            decc = chr(dec + ord('a'))
            plaintext += decc
            ind = (ind + 1) % len(keyword)

        elif i.isupper():
            cur = ord(keyword[ind]) - ord('A')
            dec = ord(i) - ord('A') - cur
            if dec < 0:
                dec += 26

            decc = chr(dec + ord('A'))
            plaintext += decc
            ind = (ind + 1) % len(keyword)
        else:
            plaintext += i

    return plaintext
