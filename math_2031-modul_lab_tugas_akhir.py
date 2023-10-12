"""
Nama : Laurentius Santiago Pratama 
Nim : 232200410
Prodi : IBDA
"""

import numpy as np
from tabulate import tabulate

latihan_soal = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv",delimiter=",", dtype='str') # Ambil nilai_akhir latihan soal dari file csv
kuis         = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv",delimiter=",", dtype='str') # Ambil nilai_akhir kuis dari file csv
lab          = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv",delimiter=",", dtype='str') # Ambil nilai_akhir lab dari file csv
proyek       = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv",delimiter=",", dtype='str') # Ambil nilai_akhir proyek dari file csv
jurnal       = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv",delimiter=",", dtype='str') # Ambil nilai_akhir jurnal dari file csv
ujian        = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv",delimiter=",", dtype='str') # Ambil nilai_akhir ujian dari file csv

nilai_latihan_soal = latihan_soal[1:,1:].astype(float) #Untuk mengekstrak nilai latihan soal dan mengembalikannya ke bentuk (float)
nilai_kuis         = kuis[1:,1:].astype(float) #Untuk mengekstrak nilai kuis dan mengembalikannya ke bentuk (float)
nilai_lab          = lab[1:,1:].astype(float) #Untuk mengekstrak nilai lab dan mengembalikannya ke bentuk (float)
nilai_proyek       = proyek[1:,1:].astype(float) #Untuk mengekstrak nilai proyek dan mengembalikannya ke bentuk (float)
nilai_jurnal       = jurnal[1:,1:].astype(float) #Untuk mengekstrak nilai jurnal dan mengembalikannya ke bentuk (float)
nilai_ujian        = ujian[1:,1:].astype(float) #Untuk mengekstrak nilai ujian dan mengembalikannya ke bentuk (float)

bobot_latihan_soal = 1/100
bobot_kuis         = 2/100
bobot_lab          = 4/100
bobot_proyek       = 7.5/100
bobot_jurnal       = 3/100
bobot_ujian        = 25/100

total_latihan_soal = np.sum(nilai_latihan_soal, axis=1) #total nilai dari latihan soal tiap mahasiswa
total_kuis         = np.sum(nilai_kuis, axis=1) #total nilai dari kuis tiap mahasiswa
total_lab          = np.sum(nilai_lab, axis=1) #total nilai dari lab tiap mahasiswa
total_proyek       = np.sum(nilai_proyek, axis=1) #total nilai dari proyek tiap mahasiswa
total_jurnal       = np.sum(nilai_jurnal, axis=1) #total nilai dari jurnal tiap mahasiswa
total_ujian        = np.sum(nilai_ujian, axis=1) #total nilai dari ujian tiap mahasiswa

total_bobot_latihan_soal = total_latihan_soal * bobot_latihan_soal  #Total nilai latihan soal per 1 mahasiswa dan dikali bobot
total_bobot_kuis         = total_kuis * bobot_kuis #Total nilai kuis per 1 mahasiswa dan dikali bobot
total_bobot_lab          = total_lab * bobot_lab #Total nilai lab per 1 mahasiswa dan dikali bobot
total_bobot_proyek       = total_proyek* bobot_proyek #Total nilai proyek per 1 mahasiswa dan dikali bobot
total_bobot_jurnal       = total_jurnal* bobot_jurnal #Total nilai jurnal per 1 mahasiswa dan dikali bobot
total_bobot_ujian        = total_ujian * bobot_ujian #Total nilai ujian per 1 mahasiswa dan dikali bobot


nilai_akhir_awal = total_bobot_latihan_soal + total_bobot_kuis + total_bobot_lab + total_bobot_proyek + total_bobot_jurnal + total_bobot_ujian # Menjumlahkan semua nilai beserta bobotnya menjadi nilai akhir
nilai_akhir = nilai_akhir_awal[:,np.newaxis] #mengubah kembali yang awalnya 1 array menjadi array column
print(nilai_akhir)
print()

skala_nilai = [
    (nilai_akhir >= 91),                      #A+
    (nilai_akhir >= 86) & (nilai_akhir < 91), #A-
    (nilai_akhir >= 81) & (nilai_akhir < 86), #B+
    (nilai_akhir >= 76) & (nilai_akhir < 81), #B
    (nilai_akhir >= 71) & (nilai_akhir < 76), #B-
    (nilai_akhir >= 61) & (nilai_akhir < 71), #C+
    (nilai_akhir >= 51) & (nilai_akhir < 61), #C
    (nilai_akhir >= 46) & (nilai_akhir < 51), #C-
    (nilai_akhir >= 41) & (nilai_akhir < 46), #D
    (nilai_akhir >= 0) & (nilai_akhir < 41),  #F
]

# indeks_prestasi yang sesuai dengan rentang
categories = ['A','A-', 'B+','B','B-','C+', 'C','C-', 'D', 'F']


indeks_prestasi = np.select(skala_nilai,categories) # indeks prestasi dari nilai akhir
print (indeks_prestasi)
print()

nim = latihan_soal[1:,0:1].astype(str)
print(nim)
print()

# Tugas 1 
math_2031_angkatan_20xx = np.block([nim, nilai_akhir,indeks_prestasi]) # menggabungkan nim, nilai akhir, dan indeks prestasi menjadi 1 array
header = ['NIM', 'Nilai Akhir', 'Indeks Prestasi']
table = tabulate (math_2031_angkatan_20xx, header,tablefmt="fancy_grid") # Mengubah tampilan dari yang awalnya array menjadi tabel
print(table)
print()

# Tugas 2 

#Untuk mengetahui nilai mana yang paling tinggi sehingga bisa berdampak jika bobotnya diberatkan.
print (np.mean(nilai_latihan_soal,axis=0))
print (np.mean(nilai_kuis,axis=0))
print (np.mean(nilai_lab,axis=0))    
print (np.mean(nilai_proyek,axis=0))
print (np.mean(nilai_jurnal,axis=0))
print (np.mean(nilai_ujian,axis=0))
print()

# Nilai dengan bobot baru
# karena UTS dan UAS tidak boleh < 15% dan nilai UTS & UAS adalah yang terendah, maka:
# UTS = 15%
# UAS = 15%
# Nilai rata rata tertinggi adalah jurnal 1, maka:
# Jurnal 1 = 51%
# Jurnal 2 = 1%
# latihan soal = 1%
# kuis = 1%
# lab = 1%
# proyek = 1%

# Bobot baru agar rata rata naik
bobot_latihan_soal_baru = 1/100
bobot_kuis_baru         = 1/100
bobot_lab_baru          = 1/100
bobot_proyek_baru       = 1/100
bobot_jurnal_1_baru     = 51/100 #karena rata rata nilainya paling tinggi
bobot_jurnal_2_baru     = 1/100
bobot_ujian_baru        = 15/100

nilai_jurnal_1 = jurnal[1:,1:2].astype(float)
nilai_jurnal_2 = jurnal[1:,2:3].astype(float)

jurnal_1       = np.sum(nilai_jurnal_1, axis=1)
jurnal_2       = np.sum(nilai_jurnal_2, axis=1)


nilai_bobot_jurnal_1_baru = jurnal_1* bobot_jurnal_1_baru #nilai jurnal 1 tiap mahasiswa dikali dengan bobotnya
nilai_bobot_jurnal_2_baru = jurnal_2* bobot_jurnal_2_baru #nilai jurnal 2 tiap mahasiswa dikali dengan bobotnya


total_bobot_latihan_soal_baru = total_latihan_soal * bobot_latihan_soal_baru  #Total nilai baru dari latihan soal per 1 mahasiswa dan dikali bobot 
total_bobot_kuis_baru         = total_kuis * bobot_kuis_baru #Total nilai baru dari kuis per 1 mahasiswa dan dikali bobot
total_bobot_lab_baru          = total_lab * bobot_lab_baru #Total nilai baru dari lab per 1 mahasiswa dan dikali bobot
total_bobot_proyek_baru       = total_proyek* bobot_proyek_baru #Total nilai baru dari proyek per 1 mahasiswa dan dikali bobot
total_bobot_jurnal_baru       = nilai_bobot_jurnal_1_baru + nilai_bobot_jurnal_2_baru #Total nilai baru dari jurnal per 1 mahasiswa yang telah dikali bobot
total_bobot_ujian_baru        = total_ujian * bobot_ujian_baru #Total nilai baru dari ujian per 1 mahasiswa dan dikali bobot


nilai_akhir_awal_baru = total_bobot_latihan_soal_baru + total_bobot_kuis_baru + total_bobot_lab_baru + total_bobot_proyek_baru + total_bobot_jurnal_baru + total_bobot_ujian_baru # Menjumlahkan semua nilai baru beserta bobot barunya menjadi nilai akhir
nilai_akhir_baru = nilai_akhir_awal_baru[:,np.newaxis] #mengubah kembali yang awalnya 1 array menjadi array column
print(nilai_akhir_baru)
print()

skala_nilai_baru = [
    (nilai_akhir_baru >= 91),                           #A+
    (nilai_akhir_baru >= 86) & (nilai_akhir_baru < 91), #A-
    (nilai_akhir_baru >= 81) & (nilai_akhir_baru < 86), #B+
    (nilai_akhir_baru >= 76) & (nilai_akhir_baru < 81), #B
    (nilai_akhir_baru >= 71) & (nilai_akhir_baru < 76), #B-
    (nilai_akhir_baru >= 61) & (nilai_akhir_baru < 71), #C+
    (nilai_akhir_baru >= 51) & (nilai_akhir_baru < 61), #C
    (nilai_akhir_baru >= 46) & (nilai_akhir_baru < 51), #C-
    (nilai_akhir_baru >= 41) & (nilai_akhir_baru < 46), #D
    (nilai_akhir_baru >= 0) & (nilai_akhir_baru < 41),  #F
]

indeks_prestasi_baru = np.select(skala_nilai_baru,categories) # indeks prestasi dari nilai akhir
print (indeks_prestasi_baru)
print()

print("rata rata lama: ",np.mean(nilai_akhir)) #menampilkan nilai rata rata lama
print("rata rata baru: ",np.mean(nilai_akhir_baru)) #menampilkan nilai rata rata baru

index_yang_dicari = 'A'
index_F_dicari = 'F'
index_lama = np.count_nonzero(indeks_prestasi == index_yang_dicari) #mencari jumlah nilai 'A' pada array lama
index_baru = np.count_nonzero(indeks_prestasi_baru == index_yang_dicari) #mencari jumlah nilai 'A' pada array baru
index_lama_F = np.count_nonzero(indeks_prestasi == index_F_dicari) #mencari jumlah nilai 'F' pada array lama
index_baru_F = np.count_nonzero(indeks_prestasi_baru == index_F_dicari) #mencari jumlah nilai 'F' pada array baru
print("Jumlah nilai 'A' lama: ", index_lama) 
print("Jumlah nilai 'A' baru: ", index_baru) 
print("Jumlah nilai 'F' lama: ", index_lama_F) 
print("Jumlah nilai 'F' baru: ", index_baru_F) 
print()

math_2031_angkatan_20xx_baru = np.block([nim, nilai_akhir_baru,indeks_prestasi_baru]) # menggabungkan nim, nilai akhir, dan indeks prestasi menjadi 1 array
table_baru = tabulate (math_2031_angkatan_20xx_baru, header,tablefmt="fancy_grid") # Mengubah tampilan dari yang awalnya array menjadi tabel
print(table_baru)
