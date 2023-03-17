Nama : Tita Nabila Putri
 | NIM : 2209116092
 | Sistem Informasi - B'22

## Post Test 3 - PlayList JOOX

## Cara Kerja Program
Pada saat program dijalankan, user akan diminta untuk menginput pilihan dari nomor 1-4. Pilihan pertama adalah Display Playlist yang dimana kita hanya dapat melihat isi yang ada dalam playlist. Pilihan kedua yaitu Tambah Lagu, dimana user diminta untuk menginput judul, penyanyi dan durasi lagu. Kemudian pilihan ketiga adalah Remove Lagu, yaitu user menghapus lagu hanya dengan mengetikkan judulnya saja. Lalu pada pilihan keempat ialah pilihan untuk keluar/berhenti dari pemrograman.

## Output
---------------------------------------
|                                     |
|                JOOX                 |
|                                     |
---------------------------------------
***************************************
| 1. Display Playlist                 |
| 2. Tambah Lagu                      |
| 3. Remove Lagu                      |
| 4. Out                              |
***************************************
Saat di-run, program akan menampilkan pilihan dari 1-4 kepada user ingin melakukan apa. Jika user memilih/menginputkan pilihan pertama yaitu Display Playlist, maka akan ditampilkan lagu-lagu apa saja yang ada di dalam playlist. Jika belum ada lagu yang ditambahkan, maka program akan menampilkan/memberitahukan bahwa isi playlist masih kosong. Selanjutnya ketika user menginput pilihan kedua yaitu Tambah Lagu, maka user akan diminta memasukkan judul, penyanyi dan durasi lagu yang nantinya akan otomatis masuk pada Display Playlist di pilihan pertama dan pada saat kita membuka Display Playlist kembali, maka akan tertera judul, penyanyi dan durasi yang telah dimasukkan. Kemudian jika user menginputkan pilihan ketiga yaitu Remove Lagu, maka user hanya akan diminta untuk memasukkan judul lagu yang ingin dihapus. Dan apabila lagu telah terhapus, maka lagu tersebut otomatis juga hilang/terhapus dari Display Playlist. Lalu ketika user menginput pilihan keempat yaitu Out, maka program akan terhenti. Sementara jika user menginputkan pilihan angka yang tidak tertera pada pilihan, maka akan diberitahukan bahwa pilihan tidak tersedia.

## Fungsionalitas
Pada program ini, linked list difungsikan agar dapat menyimpan record data yang ada pada masing-masing pilihan. Mulai dari melihat display playlist yang ada, menambah lagu dan menghapus lagu pada playlist. Linked list digunakan dalam pengimplementasian struktur data yang terdiri dari urutan record data dimana setiap record memiliki field yang menyimpan alamat record data selanjutnya di dalam urutan. Artinya, setiap elemen memiliki keterkaitan dengan elemen berikutnya yang membuat pemrograman menjadi lebih efisien dan terstruktur sehingga dapat secara otomatis membuat suatu tempat baru untuk menyimpan data.

## Sistem Kerja Aplikasi
Aplikasi ini merujuk pada playlist yang memungkinkan kita untuk menambah lagu, menghapus lagu dan melihat display playlist yang programnya saling terhubung satu sama lain. Ketika kita ingin menambahkan satu atau lebih lagu, maka otomatis lagu tersebut akan masuk pada display playlist. Sementara jika kita ingin menghapus sebuah lagu yang telah ditambahkan pada display playlist, maka lagu tersebut akan terhapus.

## Elemen Penting
class Song:
    def __init__(self, title, artist, duration)

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration})"

class Node:
    def __init__(self, song=None):
        self.song = song
        self.next = None
        def add_song(self, song):
            new_node = Node(song)
        def remove_song(self, song_title):
            current_node = self.head
            previous_node = None

    def display_playlist(self):
        current_node = self.head

Bagian-bagian penting yang digunakan terdiri dari class, yang berfungsi untuk merepresentasikan suatu objek pada linked list. Node berfungsi untuk menyimpan data. Kemudian terdapat metode def str yang digunakan untuk mendefinisikan cara merepresentasi linked list dalam bentuk string. Sementara def init digunakan untuk menginisialisasi linked list dengan membuat head node sehingga memberi akses ke elemen lain. Head node sendiri digunakan untuk menyimpan pointer ke node berikutnya. Kemudian Add digunakan untuk menambah node baru sementara remove digunakan untuk menghapus node tertentu pada linked list.