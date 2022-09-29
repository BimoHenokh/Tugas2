1.  {% csrf_token %} digunakan untuk mencegah serangan cyber berupa crsf attack
    Jika tidak ada {% csrf_token %} maka halaman akan error 

2. Kita bisa membuat elemen form secara manual. Menggunakan Dajango Templates engine, kita bisa membuat form secara manual bahkan bisa lebih baik.
    menggunakan html outpot private method
    1. Mengumpulkan eror yang tidak terhubung dengan field yang spesifil dan error dari hidden fields
    2. Menaruh non field error dan hidden field error di tempat paling atas
    3. Iterasi seluruh form fields
    4. Merender form fields satu persatu

3.  1. Menerima data dari user lalu melekatkannya ke forum
    2. clean dan memvalidasi data
    3. jika data invalid tampilkan ulang form atau error
    4. jika data valid lakukan langkah selanjutnya sesuai dari code yang ditulis
    5. setelah selesai pindahkan user ke url lain, salah satunya menampilkan data form

4.  1. menjalankan perintah python manage.py startapp di terminal
    2.  membuat file urls.py dan menambahkan script sesuai yang ada di urls.py
    3. dalam models.py membuat Class Task dan menambahkan model-model yang dibutuhkan
    4. dalam views.py membuat method register, login_user, logout_user. lalu membuat html sesuai dengan method dan membuat urlnya di urls.py
    5. membuat form user menjadi seperti ini     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_todolist", null=True), lalu pada html untuk mengambil data menggunakan script user.user_todolist.all

