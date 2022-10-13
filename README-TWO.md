Tugas 6

1.  asynchronous programming, multithreading, berbagai macam operasi bisa berjalan tanpa harus menunggu operasi yang lain selesai
    synchronous programming, singlethreading, tiap operasi dijalankan satu persatu, menunggu operasi yang lain selesai dulu baru dilanjutkan operasi lain
<!-- https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/ -->

2.  Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu.misalnya ketika tombol A diklik maka nilai label 2 ditambah nilai label 3 dibagi nilai label4, tapi jika tombol A diklik dan ternyata label satu berisikan penjumlahan, maka program yang dijalankan label 2 ditambah label 3. 
<!-- https://osf.io/3s8tw/download#:~:text=Event%2DDriven%20programming%20juga%20bisa,berupa%20pesan%20dari%20program%20lainnya. -->

3.  Dengan asynchronous programming pada AJAX maka kita bisa mengubah event/tampilan pada web yang ditampilkan tanpa harus meload ulang web tersebut, ini sangat menghemat resource karena hanya beberapa bagian web yang akan diload ulang. Bayangkan jika web memiliki memori yang besar, jika seluruh web diload ulang ini akan memperberat kinerja komputer klien

4.  Tugas 6 dibuat dengan html baru dengan nama todolist_ajax.html untuk membedakan tugas 4 dan tugas 5 lalu dihubungkan dengan url todolist/ajax/

    GET
    1.  Untuk mengembalikan data dalam bentuk json dibuat method show_json dalam file views.py
    2.  Lalu dihubungkan view tersebut dengan url todolist/ajax/json. 
    3.  Untuk mengambil data json yang dikirim menggunakan ajax. Menggunakan jquery, dibuat file baru todolist_ajax.js didalam folder static. Data akan dipanggil menggunakan url lalu mengambil seluruh data menggunakan each dan ditampilkan pada html.

    POST
    1.  Dibuat tombol add task untuk menampilkan modal berdasarkan dari link berikut: https://getbootstrap.com/docs/4.0/components/modal/
    2.  Membuat method bernama add dalam file views.py untuk menambah data setelah menerima perintah POST
    3.  Membuat url /todolist/ajax/add/ untuk menghubungkan method add
    4.  Didalam todolist_ajax.js dipanggil fungsi .post ketika tombol #submit_form diklik lalu data-data yang diinput akan dikirim ke url /todolist/ajax/add/ 
    5.  Tidak hanya mengirim input, ditambah juga $("#djangoForm").modal('hide'); untuk menutup form
    6.  Setelah tombol dipencet data yang dimasukkan akan langsung terlihat