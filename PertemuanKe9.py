# Kezia adalah seorang mahasiswa yang juga mengisi waktu luanya bekerja di perpustakaan kampusnya. 
# Ia bertugas untuk memberikan denda kepada setiap mahasiswa yang tidak mengembalikan buku pada waktunya.
# Karena biasanya, dalam sehari ada beberapa mahasiswa yang terlambat dalam mengembalikan buku yang ia pinjam, terkadang Kezia kewalahan menghitung
# berapa jumlah yang harus dibayarkan oleh setiap mahasiswa yang terlambat mengumpulkan buku yang ia pinjam tepat waktu.
# Selain itu juga setiap minggunya, kepala perpustakaan meminta laporan mahasiswa yang terkena denda akibat terlambat mengembalikan buku yang dipinjam,
# lengkap dengan data jumlah denda per mahasiswa dan total keseluruhan denda. 
# Buatlah sebuah program yang dapat membantu Kezia dalam mengurus denda tersebut jika setiap buku yang dipinjam, terlambat sehari terkena denda Rp.2000
# dan apabila user memasukkan "ya", maka tampilkan laporan mengenai denda keterlambatan tersebut!
# https://student.blog.dinus.ac.id/thoriqhafidzuzumar/2020/01/09/cara-membuat-program-raport-mahasiswa-with-python/ 

#input = jumlah mahasiswa yang terlambat, nama mahasiswa, berapa hari keterlambatan mahasiswa, apakah ingin melihat laporan atau tidak, berapa buku yang dipinjam oleh 
#       mahasiswa
#proses = mengetahui nama mahasiswa, keterlambatan mahasiswa, berapa buku yang dipinjam oleh mahasiswa, mengetahui jumlah denda tiap mahasiswa, memasukkan data yang sudah ada
#         kedalam sebuah list yang akan ditampilkan sebagai laporan
#output = nama mahasiswa beserta jumlah dendanya, apabila kita memasukkan kata "ya" maka menampilkan data atau laporan yang sudah diinputkan oleh user 

print("===========DENDA KETERLAMBATAN==========")
jumMhs = int(input("Masukkan jumlah mahasiswa yang terlambat: "))
namaMhs = []
jumDenda = []
TotalKeseluruhanDenda = 0
for i in range(0, jumMhs):
    namaMahasiswa = input("Masukkan Nama Mahasiswa: ")
    namaMhs.append(namaMahasiswa)
    keterlambatan = int(input("Masukkan jumlah hari terlambat: "))
    jumBuku = int(input("Masukkan jumlah buku yang dipinjam oleh mahasiswa: "))
    DENDA = keterlambatan * jumBuku * 2000
    jumDenda.append(DENDA)
    TotalKeseluruhanDenda += DENDA 
for i in range(0, jumMhs):
    print("Mahasiswa bernama ", namaMhs[i], "didenda sebanyak Rp. ", jumDenda[i])

laporan = input("Apakah ingin melihat laporan? (ya/tidak) ")
if laporan == "ya":
    print("==========Laporan Denda Keterlambatan Mahasiswa==========")
    for i in range(0, jumMhs):
        print("Nama: ", namaMhs[i], ", Jumlah Denda: ", jumDenda[i])
    print("Total Keseluruhan Denda: ", TotalKeseluruhanDenda)
else:
    print() 
