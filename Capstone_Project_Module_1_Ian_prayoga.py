data_perpustakaan={
    "0001":{
        "judul buku":"Koala Kumal",
        "harga buku":70000,
        "peminjam":"Arif",
        "status pinjam":True,
        "status hilang":False
    },
    "0002":{
        "judul buku":"Death Note",
        "harga buku":50000,
        "peminjam":"",
        "status pinjam":False,
        "status hilang":False
    },
    "0003":{
        "judul buku":"Kamus Bahasa Inggris Indonesia",
        "harga buku":150000,
        "peminjam":"Caca",
        "status pinjam":True,
        "status hilang":False
    },
    "0004":{
        "judul buku":"Top Gear",
        "harga buku":300000,
        "peminjam":"",
        "status pinjam":False,
        "status hilang":False
    },
    "0005":{
        "judul buku":"Derai-derai Cemara",
        "harga buku":100000,
        "peminjam":"Budi",
        "status pinjam":True,
        "status hilang":True
    }
}

def display_main_menu():
    print("\nMain Menu Perpustakaan:")
    print("1. Display data")
    print("2. Create data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Rata-rata Harga buku")
    print("6. Keluar")

def display_menu_display_data():
    print("\nMenu display data:")
    print("1. Menampilkan semua data buku")
    print("2. Menampilkan data Buku tertentu")
    print("3. Menampilkan data buku yang sedang dipinjam")
    print("4. Menampilkan data buku hilang")
    print("5. Kembali ke main menu perpustakaan")

def display_menu_create_data():
    print("\nMenu create data:")
    print("1. Menambah data buku")
    print("2. Kembali ke main menu perpustakaan")

def display_menu_update_data():
    print("\nMenu update data:")
    print("1. Mengubah data buku")
    print("2. Mengembalikan buku yang dipinjam")
    print("3. Ganti rugi buku hilang")
    print("4. Kembali ke main menu perpustakaan")

def display_menu_delete_data():
    print("\nMenu delete data:")
    print("1. Menghapus data buku")
    print("2. Kembali ke main menu perpustakaan")

def not_exist():
    print("\nData does not exist")

def rata_rata_harga():
    jumlah=0
    for barcode,data_buku in data_perpustakaan.items():
        jumlah+=int(data_buku["harga buku"])
    print(f'rata-rata harga buku : Rp.{jumlah/len(data_perpustakaan):.0f}')

def menampilkan_semua_data():
    if 'data_perpustakaan' in globals():
        print("\nData Perpustakaan : ")
        for barcode,data_buku in data_perpustakaan.items():
            print(f'{barcode} :')
            for ket,val in data_buku.items():
              print(f"  -{ket} = {val}")
    else:
        not_exist()

def menampilkan_data_buku_tertentu():
    if 'data_perpustakaan' in globals():
        input_barcode=input("Masukkan barcode : ")
        if input_barcode in data_perpustakaan:
            print(f'\n{input_barcode} :')
            for ket,val in data_perpustakaan[input_barcode].items():
                print(f"  -{ket} = {val}")
        else:
            not_exist()
    else:
        not_exist()

def menampilkan_data_buku_yang_dipinjam():
    if 'data_perpustakaan' in globals():
        for barcode,data_buku in data_perpustakaan.items():
            if data_buku["status pinjam"]==True:
                print(f'\n{barcode} :')
                for ket,val in data_buku.items():
                    print(f"  -{ket} = {val}")
    else:
        not_exist()

def menampilkan_data_buku_hilang():
    if 'data_perpustakaan' in globals():
        for barcode,data_buku in data_perpustakaan.items():
            if data_buku["status hilang"]==True:
                print(f'\n{barcode} :')
                for ket,val in data_buku.items():
                    print(f"  -{ket} = {val}")
    else:
        not_exist()

def menambah_data_buku():
    input_barcode=input("Masukkan barcode buku yang ingin ditambah : ")
    if input_barcode in data_perpustakaan:
        print("\nData already exists")
    else:
        input_judul=input("\nMasukkan judul buku : ")
        input_harga=input("Masukkan harga buku : ")
        input_stsp=input("Masukkan status pinjam (True/False) : ")
        input_stsh=input("Masukkan status hilang (True/False) : ")
        print(f"\nData yang yang ingin ditambahkan :\nData {input_barcode} : \n  -Judul buku = {input_judul}\n  -harga buku = {input_harga}\n  -status pinjam = {input_stsp}\n  -status hilang = {input_stsh}")
        input_save=input("\nApakah anda yakin ingin menyimpan data ini? (y/n) : ")
        if input_save=="y":
            data_perpustakaan[input_barcode]={
                "judul buku":input_judul,
                "harga buku":input_harga,
                "status pinjam":input_stsp,
                "status hilang":input_stsh
            }
            print("\nData successfully saved")

def mengubah_data_buku():
    input_barcode=input("Masukkan barcode buku yang ingin diupdate : ")
    if input_barcode in data_perpustakaan:
        print(f'\nData {input_barcode} :')
        for ket,val in data_perpustakaan[input_barcode].items():
            print(f"  -{ket} = {val}")
        input_lanjut=input("\nApakah ingin melanjutkan update? (y/n) : ")
        if input_lanjut=="y":
            input_kolom=input("kolom apa yang ingin diupdate : ")
            input_data=input("data yang baru : ")
            input_update=input("Apakah anda yakin ingin mengupdate data ini? (y/n) : ")
            if input_update=="y":
                data_perpustakaan[input_barcode][input_kolom]=input_data
                print("\nData successfully updated")
    else:
        print("\nThe data you are looking for does not exist")

def mengembalikan_buku():
    input_barcode=input("Masukkan barcode buku yang ingin dikembalikan : ")
    for barcode,data_buku in data_perpustakaan.items():
        if barcode==input_barcode and data_buku["status pinjam"]==True:
            data_buku["peminjam"]=""
            data_buku["status pinjam"]=False
            print("Buku berhasil dikembalikan")

def ganti_rugi_buku():
    input_buku=input("Masukkan nama buku yang hilang : ")
    for barcode,data_buku in data_perpustakaan.items():
        if data_buku["judul buku"]==input_buku:
            while True:
                print(f"\nGanti rugi Rp.{int(data_buku["harga buku"]*1.5)}")
                input_uang=int(input("Masukkan jumlah uang : "))
                if data_buku["harga buku"]*1.5<input_uang:
                    data_buku["peminjam"]=""
                    data_buku["status pinjam"]=False
                    data_buku["status hilang"]=False
                    print(f"Uang anda kembali Rp.{int(input_uang-(data_buku["harga buku"]*1.5))}, Terima Kasih")
                    break
                elif data_buku["harga buku"]*1.5==input_uang:
                    data_buku["peminjam"]=""
                    data_buku["status pinjam"]=False
                    data_buku["status hilang"]=False
                    print("Terima kasih")
                    break
                else:
                    print("pembayaran gagal")

                

def menghapus_data_buku():
    input_barcode=input("Masukkan barcode buku yang ingin dihapus : ")
    if input_barcode in data_perpustakaan:
        print(f'\nData {input_barcode} :')
        for ket,val in data_perpustakaan[input_barcode].items():
            print(f"  -{ket} = {val}")
        input_hapus=input("\nApakah anda yakin ingin menghapus data ini? (y/n) : ")
        if input_hapus=="y":
            del data_perpustakaan[input_barcode]
            print("\nData successfully deleted")
    else:
        print("\nThe data you are looking for does not exist")

def menu_display_data():
    while True:
        display_menu_display_data()
        choice = input("Pilih menu (1-5): ")
        if choice == '1':
            menampilkan_semua_data()
        elif choice == '2':
            menampilkan_data_buku_tertentu()
        elif choice == '3':
            menampilkan_data_buku_yang_dipinjam()
        elif choice == '4':
            menampilkan_data_buku_hilang()
        elif choice == '5':
            break

def menu_create_data():
    while True:
        display_menu_create_data()
        choice = input("Pilih menu (1-2): ")
        if choice == '1':
            menambah_data_buku()
        elif choice == '2':
            break

def menu_update_data():
    while True:
        display_menu_update_data()
        choice = input("Pilih menu (1-4): ")
        if choice == '1':
            mengubah_data_buku()
        elif choice == '2':
            mengembalikan_buku()
        elif choice == '3':
            ganti_rugi_buku()
        elif choice == '4':
            break

def menu_delete_data():
    while True:
        display_menu_delete_data()
        choice = input("Pilih menu (1-2): ")
        if choice == '1':
            menghapus_data_buku()
        elif choice == '2':
            break

def main_menu():
    while True:
        display_main_menu()
        choice = input("Pilih menu (1-6): ")
        if choice == '1':
            menu_display_data()
        elif choice == '2':
            menu_create_data()
        elif choice == '3':
            menu_update_data()
        elif choice == '4':
            menu_delete_data()
        elif choice == '5':
            rata_rata_harga()
        elif choice == '6':
            break
        else:
            print("The option you entered is not valid")

main_menu()
