#Tugas no 1

print("Masukkan Nama Anda!")
nama = str(input("Nama: "))
jenis_kelamin = input("Pilih jenis kelamin! (L/P)").upper()
if jenis_kelamin == "L":
    print("Selamat datang, Tuan", nama, "!")
else:
    print("Selamat datang, Nyonya", nama, "!")