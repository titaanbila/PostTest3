class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        
    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration})"

#Node
class Node:
    def __init__(self, song=None):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        
    def add_song(self, song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    #Pointer     
    def remove_song(self, song_title):
        current_node = self.head
        previous_node = None
        while current_node is not None and current_node.song.title != song_title:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"Song {song_title} tidak ditemukan!")
        elif previous_node is None:
            self.head = current_node.next
            print(f"Song {song_title} telah dihapus dari playlist!")
        else:
            previous_node.next = current_node.next
            print(f"Song {song_title} telah dihapus dari playlist!")
            
    def display_playlist(self):
        current_node = self.head
        if current_node is None:
            print("Playlist kosong!")
        else:
            print("Playlist:")
            while current_node is not None:
                print(current_node.song)
                current_node = current_node.next


library = Playlist()

while True:
    
    print("---------------------------------------")
    print("|                                     |")
    print("|                JOOX                 |")
    print("|                                     |")
    print("---------------------------------------")
    print("***************************************")
    print("| 1. Display Playlist                 |")
    print("| 2. Tambah Lagu                      |")
    print("| 3. Remove Lagu                      |")
    print("| 4. Out                              |")
    print("***************************************")
    
    menu = int(input("Masukkan pilihan Anda : "))
    
    if menu == 1:
        library.display_playlist()

    elif menu == 2:
        title = input("Judul Lagu: ")
        artist = input("Penyanyi: ")
        duration = input("Durasi: ")
        song = Song(title, artist, duration)
        library.add_song(song)
        print(f"{song} telah ditambahkan ke playlist")

    elif menu == 3:
        title = input("Judul lagu yang ingin dihapus: ")
        library.remove_song(title)

    elif menu == 4:
        exit()

    else:
        print("Invalid menu! Harap pilih kembali.")