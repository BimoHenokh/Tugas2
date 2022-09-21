1. Jelaskan perbedaan antara JSON, XML, dan HTML!
    HTML menampilkan data dan menggambarkan struktur halaman webnya dan merupakan markup language
    XML menyimpan dan mengirim data dan merupakan markup language
    JSON menyimpan dan mengirim data dalam bahasa javascript

2. Karena dalam web ada komunikasi antara client dan server yang tentu saja perlu untuk menstransfer data

TANDA SAMA DENGAN(=) ARTINYA PEMBATAS
3.  1.  menjalankan perintah =python manage.py startapp mywatchlist=
    2.  dalam file settings.py dalam folder urls dalam folder project_django dalam variable installed apps ditambahkan nama apps mywatchlist. lalu dalam file urls di folder project_django, dalam variable url_path tambahkan =path('katalog/', include('katalog.urls'))=
    3. dalam file models.py di folder mywatchlist ditambahkan function =MyWatchlistItem(models.Model):= dengan jenis item dan data typenya
    4. membuat file initial_mywatchlist_data.json pada folder fixtures untuk menyimpan 10 data yang dibutuhkan
    5. dala file views.py di folder mywatchlist ditambahkan function =def show_html(request):= untuk html, function =def show_json(request)= untuk json dan function =def show_xml(request):= untuk xml
    6. pada file urls.py di folder mywatchlist tambahkan urlpatterns dengan isinya =path('html/', show_html, name='show_html')= untuk merouting web yang html, =path('json/', show_json, name='show_json')= untuk merouting web yang json, =path('xml/', show_xml, name='show_xml')= untuk merouting web yang xml
    7. karena menggunakan tugas2 yang sudah dideploy minggu lalu, tugas tiga tinggal men-push ke github dan akan otomatis dideploy
    8. sisanya readme aja

4. ![This is an image](.jpg)

5. ![This is an image](.jpg)

https://tugas2-bimo-h.herokuapp.com/mywatchlist/html/
https://tugas2-bimo-h.herokuapp.com/mywatchlist/xml/
https://tugas2-bimo-h.herokuapp.com/mywatchlist/json/