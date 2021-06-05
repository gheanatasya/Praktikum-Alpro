# Kezia adalah seorang yang maniak huruf vokal. Ia sangat suka menghitung huruf vokal yang berada dalam sebuah file yang telah ia buat.
# Setiap Kezia selesai membuat satu buah file, ia akan menghitung berapa banyak huruf vokal yang berada di dalam file yang telah ia buat tadi.
# Biasanya untuk file yang memuat banyak kalimat, Kezia akan menghabiskan banyak waktu untuk menghitung berapa banyak huruf vokal yang berada
# di dalam file tersebut dan berakhir membuatnya berhenti di tengah jalan karena lelah menghitung. Untuk itu buatlah sebuah program 
# yang dapat membantu Kezia dalam menghitung jumlah huruf vokal yang ada di dalam sebuah file agar ia bisa menghemat waktunya!
# Referensi : Modul 14 Praktikum Algoritma (Regular Expression) dan https://www.pythonindo.com/regular-expression/ 

""" input = memasukkan nama file 
proses = menghitung frekuensi huruf vokal berapa banyak
output = jumlah keseluruhan huruf vokal yang muncul di dalam file yang telah diinputkan. """

import re
namaFile = input("Masukkan nama file : ")
handle = open(namaFile)
count = 0
for line in handle:
    words = line.split()
    VOKAL = re.compile(r'[aiueoAIUEO]')
    vokal = VOKAL.findall(line)
    count += len(vokal)

print(count)