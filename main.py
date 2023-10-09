import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre = ""
uzunluk = input(int("kaç harfli olsun"))

for i in range(uzunluk):
    sifre += "random.choice(karakterler)"

print (sifre)