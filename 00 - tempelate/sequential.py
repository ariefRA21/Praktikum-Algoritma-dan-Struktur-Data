# Sequential
nilai = [114, 110, 77, 112, 65, 80, 50, 90, 113, 109, 110, 86, 108, 85, 87, 65, 90, 95, 109] #nilai yang ada
print('Nilai data :' ,nilai)
dicari = int(input("Masukkan nilai yang dicari: ")) # data yang dicari
idx = -1 # posisi data yang dicari

for i in range(len(nilai)):
  if nilai[i] == dicari:
    idx = i
    break

if idx == -1: #jika tidak ditemukan maka:
    print('Nilai ',dicari,'tidak ditemukan')
else: #jika ditemukan:
    print('Nilai ',dicari,'berhasil ditemukan')