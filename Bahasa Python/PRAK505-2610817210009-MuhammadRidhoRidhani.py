def Biodata (tahunLahir, Nama, Asal):
    tahun_sekarang= 2020
    umur=tahun_sekarang - int (tahunLahir)
    print(f"Perkenalkan Nama Saya : {Nama}")
    print(f"Umur Saya : {umur}")
    print(f"Saya Adalah Angkatan : {tahun_sekarang}")
    print(f"Asal Saya dari : {Asal}")
tahunLahir= int (input())
Nama= (input())
Asal= (input())
Biodata(tahunLahir, Nama, Asal)