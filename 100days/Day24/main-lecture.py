f = open("my_file.txt")
contens = f.read()

print(contens)
f.close()


with open("my_file.txt", "r") as f:
    contens = f.read()
    print(contens)

with open("my_file.txt", "a") as f:
    f.write("I will be a coding god, raining down memory leaks on you till there's no more memory left")

with open("my_file.txt", "r") as f:
    print(f.read())