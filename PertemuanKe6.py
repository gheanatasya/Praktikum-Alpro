# Buatlah program untuk mengurutkan 3 bilangan yang diinputkan oleh user dari terbesar ke terkecil.
# https://student.blog.dinus.ac.id/fanuelphalosa/2019/12/21/nested-if-dan-loop/ 

""" input = 3 bilangan
proses = mengurutkan ketiga bilangan dari bilangan terbesar ke bilangan terkecil
output = ketiga bilangan telah diurutkan dari yang terbesar ke bilangan terkecil. """

bil1 = int(input("Masukkan bilangan ke-1: "))
bil2 = int(input("Masukkan bilangan ke-2: "))
bil3 = int(input("Masukkan bilangan ke-3: "))

if bil1 > bil2:
    if bil1 > bil3:
        if bil2 > bil3:
            print(bil1, bil2, bil3)
        else:
            print(bil1, bil3, bil2)
else:
    if bil2 > bil3:
        if bil1 > bil3:
            print(bil2, bil1, bil3)
        else:
            print(bil2, bil3, bil1)
    else:
        print(bil3, bil2, bil1)