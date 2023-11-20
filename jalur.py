from customtkinter import *  # Mengimpor semua definisi dari modul customtkinter untuk GUI kustom
from PIL import Image  # Mengimpor kelas Image dari modul PIL untuk manipulasi gambar
from inputnilai import *  # Mengimpor fungsi atau modul inputnilai untuk digunakan nanti

# Fungsi untuk mendapatkan path lengkap dari sumber daya (gambar) dengan path relatif
def resourcePath(relativePath):
    try:
        basePath = sys._MEIPASS  # Mencoba mendapatkan path sumber daya jika skrip dijalankan sebagai executable
    except Exception:
        basePath = os.path.abspath(".")  # Jika tidak dijalankan sebagai executable, gunakan path absolut saat ini

    return os.path.join(basePath, relativePath)

# Fungsi untuk menyembunyikan jendela utama dan menampilkan jendela pemilihan jalur
def jalur(asd):
    asd.iconify()  # Mengonifikasi (menyembunyikan) jendela utama
    app = CTkToplevel()  # Membuat jendela pemilihan jalur sebagai jendela anak
    screen_width = app.winfo_screenwidth()  # Mendapatkan lebar layar
    screen_height = app.winfo_screenheight()  # Mendapatkan tinggi layar
    app.geometry("405x637")  # Mengatur ukuran jendela pemilihan jalur
    x = (screen_width - 405) // 2  # Menghitung posisi x agar jendela berada di tengah
    y = (screen_height - 637) // 2  # Menghitung posisi y agar jendela berada di tengah
    app.geometry(f"+{x}+{y}")  # Menetapkan posisi jendela
    app.title("Pemilihan Penjaluran")  # Mengatur judul jendela pemilihan jalur

    # Menambahkan gambar latar belakang ke jendela
    background_data = Image.open(resourcePath('img/BG_PILIHJALUR.png'))
    background_image = CTkImage(light_image=background_data, size=(405, 637))
    background_label = CTkLabel(master=app, text='', image=background_image, bg_color='transparent')
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Mendefinisikan data gambar dan membuat tombol untuk setiap jalur (j1-j5)
    jalur_data1 = Image.open(resourcePath('img/j1.png'))
    jalur1 = CTkImage(light_image=jalur_data1, size=(120, 120))
    button1 = CTkButton(master=app, text='', image=jalur1,  bg_color='#95B0DF', fg_color='transparent', command=lambda: (j1_page(app, asd)))
    button1.place(x=50, y=150)

    jalur_data2 = Image.open(resourcePath('img/j2.png'))
    jalur2 = CTkImage(light_image=jalur_data2, size=(120, 120))
    button2 = CTkButton(master=app, text='', image=jalur2,  bg_color='#95B0DF', fg_color='transparent', command=lambda: (j2_page(app, asd)))
    button2.place(x=210, y=150)

    jalur_data3 = Image.open(resourcePath('img/j3.png'))
    jalur3 = CTkImage(light_image=jalur_data3, size=(120, 120))
    button3 = CTkButton(master=app, text='', image=jalur3,  bg_color='#95B0DF', fg_color='transparent', command=lambda: (j3_page(app, asd)))
    button3.place(x=50, y=290)

    jalur_data4 = Image.open(resourcePath('img/j4.png'))
    jalur4 = CTkImage(light_image=jalur_data4, size=(120, 120))
    button4 = CTkButton(master=app, text='', image=jalur4,  bg_color='#95B0DF', fg_color='transparent', command=lambda: (j4_page(app, asd)))
    button4.place(x=210, y=290)

    jalur_data5 = Image.open(resourcePath('img/j5.png'))
    jalur5 = CTkImage(light_image=jalur_data5, size=(120, 120))
    button5 = CTkButton(master=app, text='', image=jalur5,  bg_color='#95B0DF', fg_color='transparent', command=lambda: (j5_page(app, asd)))
    button5.place(x=130, y=430)

    app.resizable(0, 0)  # Mengatur agar ukuran jendela tidak dapat diubah

    app.mainloop()  # Memulai loop utama aplikasi pemilihan jalur
