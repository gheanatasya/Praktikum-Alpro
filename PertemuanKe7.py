# buatlah sebuah program untuk membantu Kezia dalam menghitung banyaknya jumlah huruf dari setiap kata
# yang berada dalam sebuah kalimat. Setelah itu identifikasi jumlah huruf per katanya. Apabila jumlah hurufnya
# lebih kecil atau sama dengan tiga berikan simbol "X", apabila jumlah huruf per katanya lebih kecil dari 5 berikan 
# simbol "Y", apabila jumlah huruf per katanya lebih kecil dari 8 berikan simbol "Z" dan selain itu diberikan simbol *.
# simbol ini berguna untuk memudahkan Kezia mengetahui berapa kira-kira jumlah per katanya.

""" input = sebuah kalimat
proses = mengetahui jumlah huruf dari setiap kata yang ada di dalam kalimat dan menentukan simbol
output = jumlah huruf perkatanya dan simbol """

kalimat = input("Masukkan kalimat: ")
kata = kalimat.lower()
kal = kata.split()
for i in (kal):
    jumlah = len(i)
    if jumlah <= 3:
        simbol = "X"
    elif jumlah < 5:
        simbol = "Y"
    elif jumlah < 8:
        simbol = "Z"
    else:
        simbol = "*"
    print(i, "terdiri dari", jumlah, "huruf (", simbol,")")



    