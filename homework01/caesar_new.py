import typing as tp


def caesar(flag, plaintext: str, shift: int = 3) -> str:

    ans = ""

    for i in plaintext:
        if flag == "encrypt":
            if i.isalpha():
                curr = ord(i) + shift
                if i.isupper() and curr > ord("Z"):
                    curr -= 26
                if i.islower() and curr > ord("z"):
                    curr -= 26
                ans += chr(curr)
            else:
                ans += i
        elif flag == "decrypt":
            if i.isalpha():
                curr = ord(i) - shift
                if i.isupper() and curr < ord("A"):
                    curr += 26
                if i.islower() and curr < ord("a"):
                    curr += 26
                ans += chr(curr)
            else:
                ans += i
    return ans
