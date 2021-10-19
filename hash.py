import hashlib

hashed = hashlib.md5(input("What do you want to hash?\n").encode("UTF-8")).hexdigest()
# hexdigest- changes it from binary to hexadecimal
with open("hashed.txt","a") as file:
    file.write(f"(hashed)\n")
print(hashed)
