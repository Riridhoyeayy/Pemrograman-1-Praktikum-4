def hitung(nilai1, nilai2):
    return mutlak (nilai1-nilai2)
def mutlak(angka):
    if (angka < 0):
        return -angka
    return angka
a, b, c, d = map(int, input().split())
hasil = hitung (a,c) + hitung (b,d)
print("%d" % hasil)