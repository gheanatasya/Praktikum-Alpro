# Pada file listkeperluan.txt berisi semua list keperluan Alex, Kezia dan Claire. Mereka bertiga akan pergi berbelanja
# di supermarket terdekat sesuai dengan isi list yang telah mereka tuliskan pada file listkeperluan.txt. 
# Ternyata saat mereka ingin pergi berbelanja, teman-temannya yang lain juga ingin menitip keperluan mereka untuk dibelikan.
# Agar Alex, Claire dan Kezia tidak lupa atas permintaan temannya, buatlah program yang bisa menambahkan list keperluan temannya
# dan menambahkan nama temannya agar mereka ingat setiap permintaan barang dari teman-temannya sesuai nama temannya.
# https://www.petanikode.com/python-file/ 

""" input = nama teman Alex,Kezia dan Claire dan list keperluan teman mereka
proses = membuka file dan menambahkan inputan user tadi ke dalam file listkeperluan.txt
output = pada file listkeperluan.txt, akan inputan oleh user telah ditambahkan kedalam file listkeperluan.txt. """

handle = open("listkeperluan.txt", "a")
namaTambahan = input("Masukkan nama: ")
listTambahan = input("Masukkan list keperluan tambahan: ")
handle.write("\n{} : {}".format(namaTambahan, listTambahan))
handle.close()