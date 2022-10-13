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

    for i in range(0, len(plaintext)):
        curr = ord(plaintext[i])
        if len(keyword) <= i:
            tab = ord(keyword[i - len(keyword) * (i // len(keyword))])
            if ord("A") <= tab <= ord("Z"):
                tab = tab - ord("A")
            elif ord("a") <= tab <= ord("z"):
                tab -= ord("a")
        else:
            tab = ord(keyword[i])
            if ord("A") <= tab <= ord("Z"):
                tab -= ord("A")
            elif ord("a") <= tab <= ord("z"):
                tab -= ord("a")
        if ord("A") <= curr <= ord("Z"):
            ciphertext += chr(((curr - ord("A") + tab) % 26) + ord("A"))
        elif ord("a") <= curr <= ord("z"):
            ciphertext += chr(((curr - ord("a") + tab) % 26) + ord("a"))
        else:
            ciphertext += plaintext[i]

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

    for i in range(0, len(ciphertext)):
        curr = ord(ciphertext[i])
        if len(keyword) <= i:
            tab = ord(keyword[i - len(keyword) * (i // len(keyword))])
            if ord("A") <= tab <= ord("Z"):
                tab -= ord("A")
            elif ord("a") <= tab <= ord("z"):
                tab -= ord("a")
        else:
            tab = ord(keyword[i])
            if ord("A") <= tab <= ord("Z"):
                tab -= ord("A")
            elif ord("a") <= tab <= ord("z"):
                tab -= ord("a")
        if ord("A") <= curr <= ord("Z"):
            plaintext += chr(((curr - ord("A") - tab) % 26) + ord("A"))
        elif ord("a") <= curr <= ord("z"):
            plaintext += chr(((curr - ord("a") - tab) % 26) + ord("a"))
        else:
            plaintext += ciphertext[i]

    return plaintext
