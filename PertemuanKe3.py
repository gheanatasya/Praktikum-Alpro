#Kezia akan membuat kue entah itu jenis kue cookies coklat atau biskuit keju. 
#Jenis kue yang akan dibuat tergantung pada jumlah uang yang diberikan oleh ibunya. 
#Apabila ibunya memberi uang lebih dari atau sama dengan 150.000 maka Kezia akan membuat cookies coklat, apabila kurang dari 150.000 kezia akan membuat biskuit keju.
#Akan tetapi, Kezia juga tidak hafal bahan-bahan dari kedua jenis kue tersebut. Maka dari itu buatlah program untuk membantu Kezia
#untuk mengetahui bahan kue dari setiap jenis kue yang akan dipilih oleh Kezia. 

""" input : jumlah uang yang diberikan oleh ibu
proses : mengetahui jenis kue dan mengetahui bahan yang dibutuhkan oleh kezia
output : jenis kue dan bahan yang akan dibutuhkan oleh kezia """

uang_pemberianibu = int(input("Masukkan jumlah uang yang diberikan oleh ibu : "))
if uang_pemberianibu >= 150000:
    jenis_kue = "Cookies coklat"
elif uang_pemberianibu < 150000:
    jenis_kue = "Biskuit keju"

print("Jenis kue yang akan dibuat oleh Kezia adalah ", jenis_kue)

if jenis_kue == "Cookies coklat":
    print("Bahan bahan yang dibutuhkan untuk membuat cookies adalah tepung, mentega, gula, garam, telur, coklat bubuk dan coklat batang.")
elif jenis_kue == "Biskuit keju":
    print("Bahan bahan yang dibutuhkan untuk membuat biskuit keju adalah tepung, mentega, telur, gula dan keju.")
    
