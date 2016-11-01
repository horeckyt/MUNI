d = 28
binar = ""
while d > 1:
    zbytek = d%2
    d = d//2
    binar = str(zbytek) + binar

print(binar)