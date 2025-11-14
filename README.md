# Prediksi-Harga-Jual-Mobil
Model prediksi harga jual kendaraan menggunakan algoritma Random Forest Regressor dan dataset yang berisi fitur-fitur seperti tahun produksi, jarak tempuh, jenis bahan bakar, dan transmisi. Model dievaluasi menggunakan metrik MAE = 0.6,MSE = 1.42, dan RMSE = 1.19, yang menunjukkan tingkat akuratan model dalam memprediksi harga kendaraan.

# AI PROJECT CYCLE
## 1. DATA ACQUISITION
pada tahap ini, fokus kita adalah mengumpulkan data mentah yang akan kita olah dan kita analisis untuk digunakan menjadi sebuah model.

model yang akan dibuat yaitu, "Prediksi Harga Jual Kendaraan" dengan dataset yang digunakan melibatkan beberapa fitur utama seperti profil kendaraan.

Kumpulan data ini berisi rincian kendaraan seperti merek, tahun produksi, jarak tempuh, jenis bahan bakar, tipe seller, transmisi, jumlah kepemilikan mobil sebelumnya. Variabel target dalam kasus ini adalah harga kendaraan, yang merupakan variabel numerik yang mencerminkan nilai kendaraan tersebut.

Variabel-variabel fitur ini akan diproses dan digunakan untuk membangun model machine learning regresi. Model ini akan digunakan untuk memprediksi harga kendaraan berdasarkan karakteristik yang dimiliki oleh setiap kendaraan dalam dataset.

Dalam hal ini, kita akan berfokus pada pengukuran metrik bisnis yang sesuai dengan permasalahan ini. Salah satu metrik yang relevan adalah "Root Mean Squared Error (RMSE)" yang mengukur seberapa akurat model dalam memprediksi harga kendaraan. Selain itu, kita juga dapat menggunakan metrik bisnis lain seperti "Mean Absolute Error (MAE)" untuk memberikan gambaran yang lebih lengkap tentang seberapa baik model ini dalam memprediksi harga kendaraan.

Dengan menggunakan metrik bisnis ini, kita dapat mengukur seberapa baik model ini dalam melakukan prediksi harga kendaraan, yang dapat sangat bermanfaat dalam industri penjualan kendaraan seperti otomotif. Semakin rendah nilai RMSE atau MAE, semakin baik model ini dalam memprediksi harga kendaraan, yang dapat membantu perusahaan atau individu yang terlibat dalam penjualan kendaraan untuk membuat keputusan yang lebih baik.

## 2. DATA EXPLORATION

Pada tahapan ini, kita akan mencoba memahami karakteristik dari sebuah dataset yang kita gunakan, seperti melihat nilai unik, mendeteksi data kosong, serta menganalisis hubungan antar variabel.

kemudian saya mencoba membuat feature baru bernama **no_year** yang digunakan untuk menghitung hasil pengurangan antara tahun sekarang dan tahun mobil dibuat.
tujuannya untuk menghitung umur mobil dalam hitungan satuan tahun
Semakin besar nilai no_year, berarti mobil tersebut lebih tua.

Contoh implementasi sederhana
| Year | Current Year | Hasil `no_year` |
| ---- | ------------ | --------------- |
| 2015 | 2020         | 5               |
| 2018 | 2020         | 2               |
| 2010 | 2020         | 10              |

Hasil:
- mobil tahun 2015 umurnya 5 tahun
- mobil tahun 2018 umurnya 2 tahun
- mobil tahun 2010 umurnya 10 tahun

dalam proses ini, Umur mobil adalah fitur penting dalam prediksi harga jual. Mobil yang lebih tua biasanya dijual dengan harga lebih murah, jadi fitur ini membantu model machine learning memahami hubungan antara usia dan harga mobil.

pada grafik heatmap yang saya buat berdasarkan hasil dari proses data exploration menunjukan bahwa:
 Variabel A                         | Variabel B | Korelasi                                                              | Arti |
| ---------------------------------- | ---------- | --------------------------------------------------------------------- | ---- |
| `Present_Price` vs `Selling_Price` | 0.88       | Sangat kuat positif → makin mahal harga baru, makin mahal harga jual. |      |
| `no_year` vs `Selling_Price`       | -0.23      | Kuat negatif → makin tua umur mobil, makin turun harga jual.          |      |
| `Kms_Driven` vs `Selling_Price`    | 0.03       | Sangat lemah → makin banyak jarak tempuh, harga cenderung turun.    |      |

<img width="1490" height="1728" alt="output" src="https://github.com/user-attachments/assets/4eb1f68a-9546-4248-aebd-794823c55374" />

## 3. MODELLING

Tahap terpenting dalam pembuatan model ML, yaitu pemodelan. Data yang sudah dipreprocessing akan digunakan untuk membuat sebuah model machine learning dengan menggunakan algoritma. Pada pemodelan kali ini, saya membuat model regresi dengan menggunakan algortima **Random Forest Regressor.**

algoritma ini saya gunakan pada pemodelan ini karena, mampu menangani data kompleks seperti contoh pada dataset yang saya gunakan dimana Harga kendaraan dipengaruhi banyak faktor (tahun, km, bahan bakar, transmisi, dll) yang hubungannya tidak selalu linear. Random Forest sangat kuat untuk menangkap hubungan non-linear dan interaksi antar fitur.

Selain itu juga, Algoritma ini Lebih akurat dibanding model sederhana karena terdiri dari banyak decision tree yang digabungkan (ensemble), model ini menghasilkan prediksi yang stabil dan biasanya lebih akurat dibanding regresi biasa.

## 4. EVALUATION

MAE, MSE, dan RMSE digunakan untuk evaluasi model karena ketiganya bisa mengukur seberapa jauh hasil prediksi model dari nilai sebenarnya. Alias dapat digunakan untuk mengukur tingkat kesalahan (error) dari model regresi.


* **MAE (Mean Absolute Error):**
  Mengukur rata-rata selisih antara hasil prediksi dan nilai aslinya.
  → Semakin kecil nilainya, semakin akurat model.

* **MSE (Mean Squared Error):**
  Mengukur rata-rata selisih yang dikuadratkan antara prediksi dan nilai asli.
  → Kesalahan besar akan lebih berpengaruh.

* **RMSE (Root Mean Squared Error):**
  Akar dari MSE, jadi hasilnya sama satuannya dengan data.
  → Nilai kecil berarti prediksi model makin mendekati kenyataan.

## DEPLOYMENT

Model prediksi harga jual mobil ini saya deploy menggunakan flask dan berbasis website. hanya saja aplikasi ini masih bisa dijalankan di localhost, belum secara publish.

# STEP BY STEP MENJALANKAN APLIKASI

1. clone repository --> git clone <link: [repository](https://github.com/Jalil98/Prediksi-Harga-Jual-Mobil.git)>
2. buat environment(bisa di cmd atau di anaconda prompth), caranya:
   - buka cmd/anaconda prompth
     
     <img width="238" height="95" alt="image" src="https://github.com/user-attachments/assets/a443f6d0-358f-470f-b57c-6a7a313a4bf8" />
   - Buat environment baru untuk menjalankan file project:

     <img width="597" height="56" alt="image" src="https://github.com/user-attachments/assets/408144e4-b4fc-4468-9b45-03beabcb29db" />

     aktifkan environment yang sudah dibuat --> ketikkan:
     
     <img width="629" height="81" alt="image" src="https://github.com/user-attachments/assets/8845b57f-d357-4c14-9864-fa1b2c80d54b" />

     kemudian install python seperti contoh diatas.

   - pindah ke file folder project:

     <img width="514" height="46" alt="image" src="https://github.com/user-attachments/assets/025ebd89-3529-4a5c-b3bd-bbcb314fb9a9" />

   - copy link address file ke cmd/anaconda prompth:

     <img width="629" height="32" alt="image" src="https://github.com/user-attachments/assets/9a6079a0-1191-4c81-a280-dd3abbfafc22" />

     <img width="441" height="30" alt="image" src="https://github.com/user-attachments/assets/2dd4ffd5-c49e-4e21-98af-573b8397d188" />

     - Install semua library project yang ada pada file requirements.txt

       <img width="827" height="41" alt="image" src="https://github.com/user-attachments/assets/b5ab4ab4-d4bc-4166-9cb7-f1296857c29a" />

     - Jalankan aplikasi:

       <img width="1310" height="447" alt="image" src="https://github.com/user-attachments/assets/3cf31ccd-40bf-4ecf-a295-2fdf9a9f150a" />

  ## SELAMAT! APLIKASI BERHASIL!

  <img width="635" height="772" alt="image" src="https://github.com/user-attachments/assets/52392bc4-60d7-4f8b-a5c2-e1186320a7d4" />


     


