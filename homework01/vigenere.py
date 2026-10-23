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
    keyword = keyword.upper()
    for i, char in enumerate(plaintext):
        if char >= "A" and char <= "Z" or char >= "a" and char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            if char >= "A" and char <= "Z":
                pos = ord(char) - ord("A")
                new_pos = (pos + shift) % 26
                ciphertext += chr(new_pos + ord("A"))
            else:
                pos = ord(char) - ord("a")
                new_pos = (pos + shift) % 26
                ciphertext += chr(new_pos + ord("a"))
        else:
            ciphertext += char
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
    keyword = keyword.upper()
    for i, char in enumerate(ciphertext):
        if char >= "A" and char <= "Z" or char >= "a" and char <= "z":
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            if char >= "A" and char <= "Z":
                pos = ord(char) - ord("A")
                new_pos = (pos - shift) % 26
                plaintext += chr(new_pos + ord("A"))
            else:
                pos = ord(char) - ord("a")
                new_pos = (pos - shift) % 26
                plaintext += chr(new_pos + ord("a"))
        else:
            plaintext += char
    return plaintext
