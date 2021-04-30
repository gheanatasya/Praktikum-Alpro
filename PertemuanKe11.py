# Seorang guru ingin menghitung keseluruhan atau total dari nilai-nilai anak walinya lalu mencari rata-rata dari keseluruhan nilai tersebut
# untuk dimasukkan kedalam buku nilainya dan untuk mengevaluasi apakah anak walinya memiliki perkembangan dalam akademiknya.
# Bantulah guru tersebut dalam memudahkan pekerjaannya dengan membuat sebuah program yang dapat menjumlahkan keseluruhan nilai yang berada dalam sebuah tuple
# lalu mencari rata-ratanya. Juga buatlah program tersebut dapat menampilkan indeks atau letak dari sebuah data yang ingin dicari oleh guru tersebut
# agar memudahkan guru tersebut untuk mengetahui letak nilai yang diinginkan di dalam tuple tersebut. 
# Referensi : Buku Logika Pemrograman Python oleh Abdul Kadir

""" input = sejumlah nilai anak wali dari guru tersebut yang berada dalam tuple dan nilai yang ingin diketahui letak atau posisinya di dalam sebuah tuple
proses = mengetahui total dari keseluruhan nilai yang berada di dalam tuple dan akan mengetahui rata-rata dari jumlah nilai yang diinputkan melalui sebuah tuple, 
         mengetahui letak atau posisi dari nilai yang ingin diketahui letaknya oleh guru tadi
output = rata-rata dari seluruh jumlah nilai yang berada dalam tuple dan posisi atau letak dari nilai tersebut tadi. """

def ratarata(tupleku, nilai):
    ubah = list(tupleku)
    total = 0
    for i in range (len(ubah)):
        total += int(ubah[i])
    rataRatanya = total // len(tupleku)
    print("Rata-ratanya adalah", rataRatanya)
    print("Data", nilai, "berada pada indeks ke", tupleku.index(nilai))

""" tupleku = ('34','56','78','98','89','77', '99', '87', '35', '48','12', '73')
ratarata(tupleku, '99')

nilainilai = ('56', '87', '11', '34', '67', '33', '22', '11', '61', '38', '90', '100', '55')
ratarata(nilainilai, '38') """

x = ('78', '90', '45', '67', '55', '90', '12', '8', '56', '54')
ratarata(x, '56')