def encode(text, key):
    result = ""
    for i in range(len(text)):
        c = text[i]
        result += chr(ord(c) + key)
    return result


if __name__ == '__main__':
    print(encode("Sourpuss", 2))
