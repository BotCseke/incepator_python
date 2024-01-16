import random
letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","@","#","$","%","^","&","*","(",")","=","+"]
print("Bine ati venit la password generator")
nr_letters = int(input("Cate litere vreti sa contina parola ?\n"))
nr_symbols = int(input("Cate simpboluri vreti sa contina parola ?\n"))
nr_numbers = int(input("Cate numere vrei sa contina parola ?\n"))
password = []
a=1
b=1
c=1
while a <= nr_letters:
    random_l = random.randint(-1,27)
    random_letters = letters[random_l]
    password.extend(random_letters)
    a+=1
while b <= nr_numbers:
    random_n = random.randint(-1,11)
    random_numbers = numbers[random_n]
    password.extend(random_numbers)
    b+=1
while c <= nr_symbols:
    random_s = random.randint(-1,13)
    random_symbols = symbols[random_s]
    password.extend(random_symbols)
    c+=1
random.shuffle(password)
print(*password, sep = "")