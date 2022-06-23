def decrypt_nolib(key1, key2):
    return ''.join([chr(y - (int(int((int(key2) - 314921) / 2081) / 1000) if int((int(key2) - 314921) / 2081) > 1000 else 1)) for y in [ord(y) for y in key1]])
key1 = input("Enter key1: ")
key2 = input("Enter key2: ")
print(decrypt_nolib(key1, key2))