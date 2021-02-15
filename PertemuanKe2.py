# buatlah algoritma program untuk menghitung total pembayaran dari pembelian seorang pelanggan toko
# dalam masalah ini ada ketentuan, apabila pembelian pelanggan tersebut sama dengan atau melebihi 100.000 , 
# maka pelanggan mendapat discount 10%, jika tidak pelanggan tersebut hanya mendapat discount 5%.
# https://pesonainformatika.com/python/program-diskon-menggunakan-python/

# input: total pembayaran pelanggan
# proses: mendapatkan diskon 10% atau hanya mendapatkan diskon 5%
# output: total pembayaran pelanggan setelah di diskon atau setelah mendapatkan diskon

total_pembayaran = int(input("Masukkan total pembayaran pelanggan : "))
if total_pembayaran >= 100000:
    diskon = total_pembayaran * 0.1
else :
    diskon = total_pembayaran * 0.05

jumlah_setelah_didiskon = total_pembayaran - diskon

print("Jadi totak yang harus dibayarkan oleh pelanggan toko setelah di diskon adalah Rp ", jumlah_setelah_didiskon) 