# Perangkum Handal Indonesia

## Deskripsi
Ini adalah program Python yang dapat merangkum materi yang diberikan. Menggunakan library Sastrawi untuk preprocessing teks dan library numpy untuk menghitung bobot kata, serta algoritma TextRank untuk menentukan kalimat yang paling penting, membuat program ini mampu merangkum materi secara akurat.

## Instalasi
1. Clone repositori ini
    `git clone https://github.com/maulanamuhammadzidan4-commits/perangkum-handal.git`
2. Install dependensi yang dibutuhkan
    `pip install -r requirements.txt`
3. Jalankan program
    `python src/main.py`

## Cara Kerja
Program ini menggunakan algoritma TextRank untuk menentukan kalimat yang paling penting dalam teks. Kalimat yang paling penting akan diambil sebagai ringkasan.

## Cara Penggunaan
1. Buka terminal di direktori repositori
2. Jalankan program
    `python src/main.py`

## Contoh
Input:
```
Python adalah bahasa pemrograman. Python banyak digunakan untuk membuat aplikasi. Bahasa Python relatif mudah dipelajari.
```
Output:
```
Python banyak digunakan untuk membuat aplikasi. Bahasa Python relatif mudah dipelajari.
```
