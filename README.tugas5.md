1.  Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.
        kelebihan:
            Sangat membantu ketika Anda hanya ingin menguji dan melihat perubahan pada satu elemen.
            Berguna untuk memperbaiki kode dengan cepat.
            Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.
        kekurangan:
            Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML

    Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.
        kelebihan:
            Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
            Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
            Class dan ID bisa digunakan oleh internal stylesheet.
        kekurangan:
            Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
            Membuat performa website lebih lemot. Sebab, CSS yang berbeda-beda akan mengakibatkan loading ulang setiap kali Anda ganti halaman website

    Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman
        kelebihan:
            Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapi.
            Loading website menjadi lebih cepat.
            File CSS dapat digunakan di beberapa halaman website sekaligus
        kekurangan:
            Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat

2.  <!--...--> = comment
    <!DOCTYPE> = tipe dokumen
    <a> = link
    <b> = bold text
    <br> = single line break
    <button> = tombol
    <div> = divition
    <form> = form user input
    <h1> to <h6> = heading
    <html> = HTML document root
    <nav> = navigation links
    <section> = section
    <style> = informasi style untuk document
    <table> = table

3.  .class = menunjuk element dengan class="class"
    #id = menunjuk element dengan id="id"
    * = memilih semua elemen
    element = memilih semua elemen <element>

4.  1.  halaman login, dan create-task dibantu oleh template di web https://mdbootstrap.com/docs/standard/extended/login/#section-7

