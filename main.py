import homework as work

print("Selamat Datang di Program Manajemen Stok Barang!")
print("Pilihan :")
print("1. Tambah Data Barang")
print("2. Edit Data")
print("3. Hapus Data Barang")
print("4. Cari Data")
print("5. Tampilkan Data Barang")
print("6. Tampilkan Jumlah Data")
print("7. Keluar")

while True:
    pilihan = input("\nMasukkan Pilihan Anda : ")

    if pilihan == '1':
        work.tambah_data()
    elif pilihan == '2':
        work.edit_data()
    elif pilihan == '3':
        work.hapus_data()
    elif pilihan == '4':
        work.cari_data()
    elif pilihan == '5':
        work.tampil_data()
    elif pilihan == '6':
        work.jumlah_data()
    elif pilihan == '7':
        print("Terimakasih :)\n")
        break