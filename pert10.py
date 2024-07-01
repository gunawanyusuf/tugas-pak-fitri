def tampilkan_menu():
    print("\nMenu Kasir")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang Belanja")
    print("3. Checkout")
    print("4. Keluar")

def tambah_barang(keranjang):
    nama_barang = input("Masukkan nama barang: ")
    harga_barang = float(input("Masukkan harga barang: "))
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    keranjang.append({'nama': nama_barang, 'harga': harga_barang, 'jumlah': jumlah_barang})
    print(f"{jumlah_barang} x {nama_barang} telah ditambahkan ke keranjang dengan harga {harga_barang} per item.")

def lihat_keranjang(keranjang):
    if not keranjang:
        print("Keranjang belanja kosong.")
    else:
        print("\nKeranjang Belanja:")
        total_harga = 0
        for idx, itemdalam in enumerate(keranjang, 1):
         subtotal = any['harga'] * any['jumlah']
        total_harga += subtotal
        print(f"{idx}. {any['nama']} - {any['jumlah']} x{ any['harga']} = {subtotal}")
        print(f"\nTotal Harga: {total_harga}")

def checkout(keranjang):
    if not keranjang:
        print("Keranjang belanja kosong. Tidak ada yang bisa di-checkout.")
    else:
        lihat_keranjang(keranjang)
        konfirmasi = input("Apakah Anda ingin melanjutkan dengan checkout? (y/n): ")
        if konfirmasi.lower() == 'y':
            total_harga = sum(item['harga'] * item['jumlah'] for item in keranjang)
            print(f"\nTotal yang harus dibayar: {total_harga}")
            keranjang.clear()
            print("Terima kasih sudah berbelanja!")

def main():
    keranjang = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tambah_barang(keranjang)
        elif pilihan == '2':
            lihat_keranjang(keranjang)
        elif pilihan == '3':
            checkout(keranjang)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program kasir.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if "kasir":  "_main_"
main()