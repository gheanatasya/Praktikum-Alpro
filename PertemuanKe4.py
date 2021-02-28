# buatlah fungsi untuk menentukan apakah sebuah nilai dari seorang mahasiswa lulus atau tidak lulus
# dengan ketentuan nilai diatas atau sama dengan 70 lulus dan ketentuan nilai :
# nilai 0 mendapatkan E 
# nilai lebih besar sama dengan 45 mendapat D
# nilai lebih besar sama dengan 55 mendapat C
# nilai lebih besar sama dengan 70 mendapat B
# nilai lebih besar sama dengan 85 mendapat A
# https://tutorallprogramming.blogspot.com/2017/12/contoh-program-fungsi-pada-python.html 

""" input : sebuah nilai
proses : apakah mahasiswa tersebut lulus atau tidak lulus dan predikat nilai yg didapatkan oleh mahasiswa dengan menggunakan fungsi
output : predikat yang didapatkan oleh mahasiswa dan apakah mahasiswa lulus atau tidak
 """
def cek_nilai(x):
    if x >= 85:
        print("Mahasiswa Lulus dengan predikat A")
    elif x >= 70:
        print("Mahasiswa Lulus dengan predikat B")
    elif x >= 55:
        print("Mahasiswa Tidak Lulus dengan predikat C")
    elif x >= 45:
        print("Mahasiswa Tidak Lulus dengan predikat D")
    else:
        print("Mahasiswa Tidak Lulus dengan predikat E")

cek_nilai(90)
cek_nilai(50)
cek_nilai(30)
cek_nilai(75)
cek_nilai(45)

