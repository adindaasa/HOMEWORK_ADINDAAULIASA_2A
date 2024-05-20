data_barang = []

def tampilan():
    print("Selamat Datang di Program Manajemen Stok Barang!")
    print("Pilihan :")
    print("1. Tambah data barang")
    print("2. Edit Data")
    print("3. Hapus Data Barang")
    print("4. Cari Data")
    print("5. Tampilkan data barang")
    print("6. Tampilkan Jumlah Barang")
    print("7. Keluar")
  
def tambah_data():
    nama = str(input("Masukkan Nama Barang : "))
    stok = int(input("Masukkan Stok Barang : "))
    barang_new = {'nama' : nama, 'stok' : stok}
    data_barang.append(barang_new)
    print("---------- Data Berhasil Ditambahkan ----------")
    print("\n")

def edit_data():
    edit = int(input("Hapus data index ke : "))
    if edit >= len(data_barang):
        print("Index Tidak Ada Dalam Data")
        return
    
    nama_baru = str(input("Masukkan Nama Barang Baru : "))
    stok_baru = int(input("Masukkan Jumlah Stok Baru : "))

    data_barang[edit]["nama"] = nama_baru.capitalize()
    data_barang[edit]["stok"] = stok_baru
    print("<<< Data Berhasil Diubah >>>")

def hapus_data():
    hapus = int(input("Hapus Data Index Ke = "))
    data_barang.pop(hapus) 
    print("--- Data Berhasil Dihapus ---")
    print("\n")

def cari_data():
    nama_cari = str(input("Cari Nama Barang: "))
    print("===== Hasil Pencarian =====")
    for i in data_barang:
        if i['nama'].capitalize() == nama_cari.capitalize():
            print('•',i['nama'],'--> Stok :',i['stok'])
            return
    print("---- Data Tidak Ditemukan ----")

def tampil_data():
    print("===== Toko Elektronik =====")
    for barang in data_barang:
        print('•', barang['nama'], '--> Stok :', barang['stok'])
    if not data_barang:
        print("--------- Data Barang Kosong ---------")

def jumlah_data():
    print(f'Total data: {len(data_barang)}')


     