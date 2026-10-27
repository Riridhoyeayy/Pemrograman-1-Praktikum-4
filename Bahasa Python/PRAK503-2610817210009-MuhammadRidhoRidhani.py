def maksimal(a, b):
    if (b>a):
        a=b
    return a
def minimal(a, b):
    if (a < b):
        b = a
    return b
bilangan = int(input())
nilai = list(map(int, input(). split()))
batas = int (0)
maks = int (-100000)
minim = int (100000)
while (batas < bilangan):
    maks = maksimal(maks, nilai[batas])
    minim = minimal(minim, nilai[batas])
    batas += 1
print(f"{maks} {minim}")