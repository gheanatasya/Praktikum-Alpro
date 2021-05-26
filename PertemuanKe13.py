# Kezia adalah anak kelas 7 SMP yang sangat menyukai perhitungan. Kezia juga mengikuti lomba olimpiade matematika untuk mewakili sekolah ke tingkat provinsi.
# Untuk mengasah kemampuan perhitungannya, biasanya di waktu luang Kezia suka melakukan perhitungan kecil-kecilan seperti menjumlahkan setiap angka yang berada
# dalam sebuah deretan agar menjaga otaknya tetap bekerja di waktu senggang atau di luar waktu belajarnya. 
# Biasanya karena Kezia tidak suka menggunakan kalkulator untuk memastikan apakah perhitungan-perhitungan yang ia lakukan sudah benar, 
# ia kesulitan dalam menentukan apakah perhitungannya sudah benar dan berakhir ia akan melakukan perhitungan itu sebanyak dua kali untuk memastikannya. 
# Bantulah Kezia untuk membuat program yang dapat mempermudah Kezia dalam melakukan penjumlahan sederet angka yang akan ia inputkan!
# Referensi : Logika Pemrograman Python oleh Abdul Kadir

""" input = sederet angka yang akan dijumlahkan
proses = menjumlahkan semua angka yang berada dalam deretan tersebut 
output = total ketika dijumlah seluruh angka tersebut yang berada di dalam deretan.  """

def totalderetan(n, r):
    if r == 0:
        return n[0]
    else:
        return n[r] + totalderetan(n, r-1)

n = [5,9,1,2,0,5,4,2,1,3]
print(totalderetan(n, len(n)-1)) 