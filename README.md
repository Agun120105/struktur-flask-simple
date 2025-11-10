# struktur-flask-simple
.

📁 Struktur Proyek

Proyek ini memiliki struktur folder sederhana yang terdiri dari satu file utama bernama app.py yang berisi program utama Flask, serta file requirements.txt yang berisi daftar library yang dibutuhkan.
Selain itu, bisa juga dibuat folder venv sebagai virtual environment agar instalasi library tidak mengganggu sistem Python utama.

⚙️ Langkah Instalasi

Buat virtual environment (opsional):
Langkah ini dilakukan agar lingkungan kerja Python terpisah dari sistem utama.
Setelah membuat virtual environment, aktifkan sebelum menginstal dependency.

Instal Flask:
Gunakan perintah untuk menginstal library Flask sesuai dengan daftar yang tercantum di requirements.txt.

Jalankan aplikasi:
Setelah Flask terinstal, jalankan file app.py menggunakan perintah Python atau melalui Flask CLI.
Jika berhasil, server akan berjalan pada alamat lokal dengan port default 5000.

Akses di browser:
Buka browser dan ketik alamat http://127.0.0.1:5000/
 untuk melihat hasilnya.
Jika berhasil, akan muncul tulisan “Hello, World!”.

💡 Penjelasan Singkat

Aplikasi ini bekerja dengan cara memanfaatkan konsep route pada Flask.
Ketika pengguna mengakses alamat utama atau root (/), Flask akan memanggil fungsi tertentu yang mengembalikan teks “Hello, World!”.
Fungsi tersebut berjalan di dalam server lokal yang dibuat otomatis oleh Flask ketika program dijalankan.

Aplikasi ini juga dapat dikembangkan lebih lanjut dengan menambahkan route lain seperti menampilkan pesan berbeda berdasarkan nama pengguna, menampilkan data dalam format JSON, atau menambahkan halaman HTML menggunakan template.

🔍 Cara Pengujian

Setelah aplikasi dijalankan, buka browser dan kunjungi alamat lokal.
Selain melalui browser, aplikasi juga bisa diuji dengan menggunakan alat seperti Postman atau perintah curl untuk mengirim permintaan HTTP ke server Flask.
Jika server menampilkan pesan “Hello, World!”, berarti aplikasi sudah berjalan dengan benar.

📚 Kesimpulan

Proyek ini merupakan langkah awal untuk memahami cara kerja Flask.
Dengan struktur sederhana dan hasil yang mudah dilihat, proyek Hello World ini membantu memahami dasar pembuatan web server menggunakan Python.
Langkah selanjutnya dapat berupa menambahkan halaman HTML, membuat API sederhana, atau menghubungkan Flask dengan database seperti PostgreSQL atau MySQL.
