def encrypt_nolib(x):
    return ''.join([chr(y + (int(sum([ord(y) for y in x]) / 1000) if sum([ord(y) for y in x]) > 1000 else 2)) for y in [ord(y) for y in x]]), str((sum([ord(y) for y in x])+314921)+(sum([ord(y) for y in x])*32)+(sum([ord(y) for y in x])*2048))
x = input("Enter string details:")
y = encrypt_nolib(x)
print(y)