# Buatlah program yang memberikan inputan sebanyak N bilangan dimana program nantinya akan menampilkan apakah setiap bilangan yang ada dalam
# N deretan bilangan tersebut adalah bilangan genap atau bilangan ganjil.
# https://core.ac.uk/download/pdf/45375438.pdf 

# input : N bilangan / jumlah bilangan
# proses : mengetahui apakah setiap bilangan dalam deretan N jumlah bilangan adalah bilangan ganjil atau genap
# output : setiap bilangan apakah adalah bilangan genap atau bilangan ganjil.

jumlahbil = int(input("Masukkan jumlah bilangan: "))
for i in range (1, jumlahbil+1):
    if i % 2 == 0:
        print("Bilangan", i, "adalah bilangan genap")
    else:
        print("Bilangan", i, "adalah bilangan ganjil")