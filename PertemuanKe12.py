# Kezia suka bermain-main dengan sebuah string atau kalimat. Ia sangat suka menuliskan kalimat - kalimat yang panjang dan menghitung ada berapa banyak huruf
# yang sama yang ia tulis. Ia suka mengelompokkannya berdasarkan huruf vokal dan huruf konsonan. Setelah itu Kezia akan melihat huruf mana yang paling sering muncul.
# Untuk mempermudah Kezia dalam melakukan hobinya tersebut dan untuk membantu Kezia, buatlah sebuah program yang dapat membantu Kezia dalam menghitung 
# berapa banyak setiap huruf muncul dalam kalimat yang dituliskan oleh Kezia dan menampilkan huruf yang paling banyak muncul dalam kalimat yang telah diinputkan
# oleh Kezia! 
# Referensi : Logika Pemrograman Python oleh Abdul Kadir  

""" input = sebuah kalimat yang akan dihitung berapa banyak setiap huruf yang muncul di dalamnya 
proses = mengetahui jumlah setiap huruf yang muncul di dalam kalimat yang telah diinputkan oleh user (Kezia)
output = huruf yang paling banyak atau yang paling sering muncul didalam kalimat yang diinputkan oleh user, dan menampilkan jumlah dari huruf tersebut. """

kalimat = input("Masukkan kalimat : ")
KALIMAT = set(kalimat)
hitung = 0
huruf = ''
for i in KALIMAT:
    jum = kalimat.count(i)
    if jum > hitung:
        hitung = jum
        huruf = i
print("Huruf yang paling sering keluar adalah huruf", huruf)
print("Huruf", huruf, "keluar sebanyak", hitung)