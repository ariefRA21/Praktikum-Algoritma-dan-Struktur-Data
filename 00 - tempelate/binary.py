l = [1, 4, 80, 7, 8, 10, 13, 14, 18, 19, 21, 24, 3, 40, 45, 71]
dicari = 7
print('Mencari nilai',dicari,'dengan binary search','pada list',l)
ditemukan = False
batas_awal = 0
batas_akhir = len(l) - 1
while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir-batas_awal)//2 # ambil posisi tengah
    print('posisi pencarian: index',pos_cari,'dengan nilai',l[pos_cari])
    if l[pos_cari] == dicari:
        ditemukan = True
    elif l[pos_cari] > dicari:
        batas_akhir = pos_cari-1 # geser 1 titik lebih kecil dari posisi sekarang
    else:
        batas_awal = pos_cari+1 # geser 1 titik lebih besar dari posisi sekarang

if ditemukan:
    print('Nilai',dicari,'ditemukan pada index',pos_cari)
else:
    print('Nilai',dicari,'tidak ditemukan')