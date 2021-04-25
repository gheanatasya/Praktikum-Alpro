# Sebuah butik terkenal menjual berbagai pakaian dengan merk ternama. Setiap pakaian dengan merk berbeda disimpan dalam sebuah Dictionary dengan 
# kata key sebanyak merk-merk yang mereka miliki. Biasanya sekali dalam sebulan, butik ini akan kedatangan pakaian-pakaian dengan merk baru.
# Manager butik ini ingin menyimpan data pakaian dengan merk yang masuk kedalam gudang butik mereka kedalam sebuah dictionary agar memudahkan 
# pegawai lain untuk melihat daftar merk baju yang masuk berdasarkan kodenya. Contoh kodenya misalnya LV001, GC002, dll.
# Hal ini agar memudahkan pegawai untuk melihat jumlah barang yang masuk. 
# Buatlah sebuah program yang dapat memudahkan sang manager untuk mendata pakaian-pakaian yang masuk beserta jumlah barangnya dan 
# tampilkan data-datanya!
# referensi materi : Modul PrakAlpro Pertemuan ke-10

""" input = kode pakaian sesuai dengan merk pakaian dan jumlah pakaian sesuai merk
proses = mengetahui kode pakaian dari setiap merk baju yang masuk kedalam guding butik dan mengetahui jumlah pakaian yang masuk sesuai dengan merk
output = keseluruhan merk pakaian (kode pakaian) yang masuk kedalam gudang butik ini dan jumlah pakaian yang masuk ke dalam gudang butik. """

jumMerkPakaian = int(input("Masukkan jumlah merk pakaian yang masuk: "))
Dictionary = {}
dataKey = []
dataValue = []
for i in range(0, jumMerkPakaian):
    kode = input("Masukkan kode: ")
    dataKey.append(kode)
    jumlah = int(input("Masukkan jumlah pakaian: "))
    dataValue.append(jumlah)

for i in range(len(dataKey)):
    Dictionary[dataKey[i]] = dataValue[i]
    
print(Dictionary)