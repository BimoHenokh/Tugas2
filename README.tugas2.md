1. ![This is an image](bagan_django.jpg)
    Django menggunakan request dan respon object untuk berkomunikasi antara klien dan server.

    URL digunakan untuk mengarahkan permintaan HTTP klien lalu meneruskannya ke views

    views adalah business logic yang menerima permintaan HTTP dan mengembalikan respon HTTP. View mengakses data yang dibutuhkan untuk memenuhi "request" melalui models dan memformat "response" ke templat

    models adalah objek yang membentuk struktur data dari sebuah aplikasi, dan sebagai perantara dari view dan database

    template adalah "text file" yang membentuk struktur atau layout dari file. Template mengubah script data yang diterima dari view agar bisa ditampilkan pada layar user.

2. Virtual environment memberikan ruang yang terpisah untuk membuat aplikasi yang diinginkan dari sistem operasi. Kita bisa menginstall berbagai macam hal khusus untuk projek yang kita inginkan dan tidak mempengaruhi sistem operasi atau projek lainnya

3. Pada views.py terdapat fungsi show_katalog fungsi ini mendefinisikan berbagai macam benda yang diambil dari models.py agar bisa dilanjutkan ke HTML

    data di views.py dirouting menggunakan file bernama urls.py. Setelah menerima request dari pengguna maka routing berfungsi untuk mengarahkan request ke aplikasi yang benar.  Pada urls.py pada folder katalog terdapat variable yang mendefinisikan routing aplikasi tersebut. Lalu pada urls.py di folder project_django aplikasi tadi akan diarahkan dengan path ''

    Pada file templates bernama katalog.html, yang menggunakan html, data dari views akan diproses disini menjadi tampilan yang diinginkan kepada pengguna

    Untuk di deploy ke HEROKU project akan di push ke repository di GitHub. Karena file penunjang untuk mendeploy heroku sudah lengkap tinggal kita buat link aplikasinya di heroku lalu mendeploy repositori di GitHub ke link aplikasi yang sudah dibuat di heroku.




Link : https://tugas2-bimo-h.herokuapp.com/