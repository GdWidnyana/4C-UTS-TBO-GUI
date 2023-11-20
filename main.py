from customtkinter import *  # Mengimpor modul customtkinter untuk keperluan GUI kustom
from PIL import Image  # Mengimpor modul PIL untuk manipulasi gambar
from jalur import *  # Mengimpor fungsi atau modul jalur untuk digunakan nanti

# Fungsi untuk mendapatkan path dari sumber daya (misalnya, gambar) dalam bentuk path relatif
def resourcePath(relativePath):
    try:
        basePath = sys._MEIPASS  # Mencoba mendapatkan path sumber daya jika skrip dijalankan sebagai executable
    except Exception:
        basePath = os.path.abspath(".")  # Jika tidak dijalankan sebagai executable, gunakan path absolut saat ini

    return os.path.join(basePath, relativePath)

# Fungsi untuk mengubah warna tombol menjadi merah
def change_button_color():
    button1.configure(bg_color='red')  # Mengubah warna latar belakang tombol menjadi merah
    app.after(500, restore_button_color)  # Menjadwalkan fungsi restore_button_color() setelah 500 milidetik

# Fungsi untuk mengembalikan warna tombol ke warna default
def restore_button_color():
    button1.configure(bg='SystemButtonFace')  # Mengembalikan warna latar belakang tombol ke warna default sistem

# Fungsi untuk menavigasi ke jalur (fungsi dari modul jalur)
def navigate_to_jalur():
    change_button_color()  # Memanggil fungsi untuk mengubah warna tombol
    jalur(app)  # Memanggil fungsi jalur() dari modul jalur

# Membuat objek aplikasi menggunakan custom tkinter (CTk)
app = CTk()
app.geometry("405x637")  # Mengatur ukuran jendela aplikasi
app.title("Sistem Seleksi 5 Penjaluran Informatika")  # Mengatur judul jendela aplikasi

# Membuat latar belakang menggunakan gambar dari file "BG.png"
bg_data = Image.open(resourcePath("img/BG.png"))
bg = CTkImage(light_image=bg_data, size=(405, 637))  # Menggunakan custom tkinter image untuk latar belakang
bg_label = CTkLabel(master=app, text='', image=bg)  # Membuat label untuk menampilkan latar belakang
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Menempatkan label dengan ukuran yang sesuai

# Membuat objek font untuk digunakan dalam aplikasi
font = CTkFont("Bahnschrift", 40)
font2 = CTkFont("SF Pro Text", 20)

# Membuat tombol dengan gambar dari file "Button.png"
button_image_data = Image.open(resourcePath("img/Button.png"))
button_image = CTkImage(light_image=button_image_data, size=(button_image_data.width, button_image_data.height))
button1 = CTkButton(master=app, image=button_image, text='', fg_color='white', font=font2, bg_color='transparent', command=navigate_to_jalur)
button1.place(y=432, x=98)  # Menempatkan tombol pada posisi yang diinginkan

app.resizable(0, 0)  # Mengatur agar ukuran jendela tidak dapat diubah

app.mainloop()  # Memulai loop utama aplikasi tkinter
