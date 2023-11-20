from customtkinter import *
from PIL import Image
from  module.DFA import *

string = ""  #String yang bakal dipass ke dalam diagram dfa
counter = 0
nilai_list = []
sertif_status = ""


def button_handler(main, asd, invalue, MK1_Entry, MK2_Entry, MK3_Entry, MK4_Entry, MK5_Entry, MK6_Entry):
    global counter
    global string
    global nilai_list
    if counter == 0:
        if invalue == 'A':
            MK1_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK1_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK1_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK1_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK1_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK1_Entry.insert("1.0", 'E')
            counter = counter + 1

    elif counter == 1:
        if invalue == 'A':
            MK2_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK2_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK2_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK2_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK2_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK2_Entry.insert("1.0", 'E')
            counter = counter + 1

    elif counter == 2:
        if invalue == 'A':
            MK3_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK3_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK3_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK3_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK3_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK3_Entry.insert("1.0", 'E')
            counter = counter + 1

    elif counter == 3:
        if invalue == 'A':
            MK4_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK4_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK4_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK4_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK4_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK4_Entry.insert("1.0", 'E')
            counter = counter + 1

    elif counter == 4:
        if invalue == 'A':
            MK5_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK5_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK5_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK5_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK5_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK5_Entry.insert("1.0", 'E')
            counter = counter + 1

    elif counter == 5:
        if invalue == 'A':
            MK6_Entry.insert("1.0", 'A')
            counter = counter + 1
        if invalue == 'B+':
            MK6_Entry.insert("1.0", 'B+')
            counter = counter + 1
        if invalue == 'B':
            MK6_Entry.insert("1.0", 'B')
            counter = counter + 1
        if invalue == 'C':
            MK6_Entry.insert("1.0", 'C')
            counter = counter + 1
        if invalue == 'D':
            MK6_Entry.insert("1.0", 'D')
            counter = counter + 1
        if invalue == 'E':
            MK6_Entry.insert("1.0", 'E')
            counter = counter + 1
            
    dict = {'A':'1', 'B+':'2', 'B':'3', 'C':'4', 'D':'5', 'E':'6'}
    if counter==6:
        if string[1:] == '1':
            MK_list = ["ALP", "TBO", "BD", "MI", "SD", "MD1"]

        if string[1:] == '2':
            MK_list = ["ALP", "RPL", "BD", "MI", "SD", "DAA"]

        if string[1:] == '3':
            MK_list = ["ALP", "MI", "BD", "SDG", "DAA", "MD1"]
        
        if string[1:] == '4':
            MK_list = ["ALP", "SDG", "BD", "MI", "SD", "SO"]

        if string[1:] == '5':
            MK_list = ["ALP", "KDJK", "RPL", "MI", "MD2", "SO"]
        
        nilai = [MK1_Entry.get(1.0, 2.0), MK2_Entry.get(1.0, 2.0), MK3_Entry.get(1.0, 2.0),
                 MK4_Entry.get(1.0, 2.0), MK5_Entry.get(1.0, 2.0), MK6_Entry.get(1.0, 2.0)]
        

        for i in range(0, 6):
            nilai_list.append((MK_list[i], nilai[i]))

        nilai_list = [(item[0], item[1].strip()) for item in nilai_list]
        nilai_list = [(item[0], dict.get(item[1], item[1])) for item in nilai_list]

        print(nilai_list)
        sertifikat_page(asd, main)


def sertif_handler(main, asd, invalue):
    asd.destroy()
    global sertif_status
    sertif_status = f'{invalue}'
    global nilai_list
    global string
    for mata_kuliah, nilai in nilai_list:
            print(mata_kuliah, nilai)
            if string[0] == '1':
                if mata_kuliah == 'TBO':
                    if nilai != '1':
                        string += f'{nilai}{invalue}'
                        #string += invalue
                        continue
            elif string[0] == '2':
                if mata_kuliah == 'RPL':
                    if nilai != '1':
                        string += f'{nilai}{invalue}'
                        #string += invalue
                        continue
            elif string[0] == '3':
                if mata_kuliah == 'MI':
                    if nilai != '1':
                        string += f'{nilai}{invalue}'
                        #string += invalue
                        continue
            elif string[0] == '4':
                if mata_kuliah == 'SDG':
                    if nilai != '1':
                        string += f'{nilai}{invalue}'
                        #string += invalue
                        continue
            elif string[0] == '5':
                if mata_kuliah == 'KDJK':
                    if nilai != '1':
                        string += f'{nilai}{invalue}'
                        #string += invalue
                        continue
            string += f'{nilai}'
    hasil_page(asd, main)



def j1_page(asd, main):  #yang dimaksud asd itu page sebelumnya, jadi di page ini page sebelumnya bakal diclose
    asd.destroy()
    global string
    global counter
    string += '11'
    app = CTkToplevel()
    app.title("Input Nilai")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')


    bg_data = Image.open("img/BG_INPUTNILAINEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)
    ALP_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Algoritma & Pemrograman").place(x=31, y=136)
    ALP_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    ALP_Entry.place(x=306, y=132)

    TBO_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Teori Bahasa dan Otomata").place(x=31, y=185)
    TBO_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    TBO_Entry.place(x=306, y=181)

    BD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Basis Data").place(x=31, y=234)
    BD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    BD_Entry.place(x=306, y=230)

    MI_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Informatika").place(x=31, y=283)
    MI_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MI_Entry.place(x=306, y=279)

    SD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Struktur Data").place(x=31, y=332)
    SD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SD_Entry.place(x=306, y=328)

    MD1_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Diskrit 1").place(x=31, y=381)
    MD1_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MD1_Entry.place(x=306, y=377)

    A_data = Image.open("img/A.png")
    A = CTkImage(light_image=A_data, dark_image=A_data, size=(52, 50))

    Bp_data = Image.open("img/B+.png")
    Bp = CTkImage(light_image=Bp_data, dark_image=Bp_data, size=(52, 50))

    B_data = Image.open("img/B.png")
    B = CTkImage(light_image=B_data, dark_image=B_data, size=(52, 50))

    C_data = Image.open("img/C.png")
    C = CTkImage(light_image=C_data, dark_image=C_data, size=(52, 50))

    D_data = Image.open("img/D.png")
    D = CTkImage(light_image=D_data, dark_image=D_data, size=(52, 50))

    E_data = Image.open("img/E.png")
    E = CTkImage(light_image=E_data, dark_image=E_data, size=(52, 50))

    A_Button = CTkButton(master=app, text='', image=A, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='A':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=45, y=453)
    Bp_Button = CTkButton(master=app, text='', image=Bp, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B+':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=137, y=453)
    B_Button = CTkButton(master=app, text='', image=B, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=229, y=453)

    C_Button = CTkButton(master=app, text='', image=C, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='C':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=45, y=519)
    D_Button = CTkButton(master=app, text='', image=D, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='D':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=137, y=519)
    E_Button = CTkButton(master=app, text='', image=E, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='E':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=TBO_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=MD1_Entry)).place(x=229, y=519)
    app.mainloop()

def j2_page(asd, main):  #yang dimaksud asd itu page sebelumnya, jadi di page ini page sebelumnya bakal diclose
    asd.destroy()
    global string
    global counter
    string += '22'
    app = CTkToplevel()
    app.title("Input Nilai")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')


    bg_data = Image.open("img/BG_INPUTNILAINEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)
    ALP_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Algoritma & Pemrograman").place(x=31, y=136)
    ALP_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    ALP_Entry.place(x=306, y=132)

    RPL_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Rekayasa Perangkat Lunak").place(x=31, y=185)
    RPL_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    RPL_Entry.place(x=306, y=181)

    BD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Basis Data").place(x=31, y=234)
    BD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    BD_Entry.place(x=306, y=230)

    MI_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Informatika").place(x=31, y=283)
    MI_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MI_Entry.place(x=306, y=279)

    SD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Struktur Data").place(x=31, y=332)
    SD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SD_Entry.place(x=306, y=328)

    DAA_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Desain dan Analisis Algoritma").place(x=31, y=381)
    DAA_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    DAA_Entry.place(x=306, y=377)

    A_data = Image.open("img/A.png")
    A = CTkImage(light_image=A_data, dark_image=A_data, size=(52, 50))

    Bp_data = Image.open("img/B+.png")
    Bp = CTkImage(light_image=Bp_data, dark_image=Bp_data, size=(52, 50))

    B_data = Image.open("img/B.png")
    B = CTkImage(light_image=B_data, dark_image=B_data, size=(52, 50))

    C_data = Image.open("img/C.png")
    C = CTkImage(light_image=C_data, dark_image=C_data, size=(52, 50))

    D_data = Image.open("img/D.png")
    D = CTkImage(light_image=D_data, dark_image=D_data, size=(52, 50))

    E_data = Image.open("img/E.png")
    E = CTkImage(light_image=E_data, dark_image=E_data, size=(52, 50))

    A_Button = CTkButton(master=app, text='', image=A, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='A':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=45, y=453)
    Bp_Button = CTkButton(master=app, text='', image=Bp, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B+':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=137, y=453)
    B_Button = CTkButton(master=app, text='', image=B, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=229, y=453)

    C_Button = CTkButton(master=app, text='', image=C, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='C':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=45, y=519)
    D_Button = CTkButton(master=app, text='', image=D, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='D':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=137, y=519)
    E_Button = CTkButton(master=app, text='', image=E, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='E':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=RPL_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=DAA_Entry)).place(x=229, y=519)
    app.mainloop()

def j3_page(asd, main):  #yang dimaksud asd itu page sebelumnya, jadi di page ini page sebelumnya bakal diclose
    asd.destroy()
    global string
    global counter
    string += '33'
    app = CTkToplevel()
    app.title("Input Nilai")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')


    bg_data = Image.open("img/BG_INPUTNILAINEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)
    ALP_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Algoritma & Pemrograman").place(x=31, y=136)
    ALP_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    ALP_Entry.place(x=306, y=132)

    MI_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Informatika").place(x=31, y=185)
    MI_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MI_Entry.place(x=306, y=181)

    BD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Basis Data").place(x=31, y=234)
    BD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    BD_Entry.place(x=306, y=230)

    SDG_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Sistem Digital").place(x=31, y=283)
    SDG_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SDG_Entry.place(x=306, y=279)

    DAA_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Desain dan Analisis Algoritma").place(x=31, y=332)
    DAA_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    DAA_Entry.place(x=306, y=328)

    MD1_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Diskrit 1").place(x=31, y=381)
    MD1_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MD1_Entry.place(x=306, y=377)

    A_data = Image.open("img/A.png")
    A = CTkImage(light_image=A_data, dark_image=A_data, size=(52, 50))

    Bp_data = Image.open("img/B+.png")
    Bp = CTkImage(light_image=Bp_data, dark_image=Bp_data, size=(52, 50))

    B_data = Image.open("img/B.png")
    B = CTkImage(light_image=B_data, dark_image=B_data, size=(52, 50))

    C_data = Image.open("img/C.png")
    C = CTkImage(light_image=C_data, dark_image=C_data, size=(52, 50))

    D_data = Image.open("img/D.png")
    D = CTkImage(light_image=D_data, dark_image=D_data, size=(52, 50))

    E_data = Image.open("img/E.png")
    E = CTkImage(light_image=E_data, dark_image=E_data, size=(52, 50))

    A_Button = CTkButton(master=app, text='', image=A, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='A':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=45, y=453)
    Bp_Button = CTkButton(master=app, text='', image=Bp, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B+':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=137, y=453)
    B_Button = CTkButton(master=app, text='', image=B, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=229, y=453)

    C_Button = CTkButton(master=app, text='', image=C, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='C': button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=45, y=519)
    D_Button = CTkButton(master=app, text='', image=D, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='D':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=137, y=519)
    E_Button = CTkButton(master=app, text='', image=E, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='E':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=MI_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=SDG_Entry, MK5_Entry=DAA_Entry, MK6_Entry=MD1_Entry)).place(x=229, y=519)
    app.mainloop()

def j4_page(asd, main):  #yang dimaksud asd itu page sebelumnya, jadi di page ini page sebelumnya bakal diclose
    asd.destroy()
    global string
    global counter
    string += '44'
    app = CTkToplevel()
    app.title("Input Nilai")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')


    bg_data = Image.open("img/BG_INPUTNILAINEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)
    ALP_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Algoritma & Pemrograman").place(x=31, y=136)
    ALP_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    ALP_Entry.place(x=306, y=132)

    SDG_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Sistem Digital").place(x=31, y=185)
    SDG_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SDG_Entry.place(x=306, y=181)

    BD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Basis Data").place(x=31, y=234)
    BD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    BD_Entry.place(x=306, y=230)

    MI_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Informatika").place(x=31, y=283)
    MI_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MI_Entry.place(x=306, y=279)

    SD_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Struktur Data").place(x=31, y=332)
    SD_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SD_Entry.place(x=306, y=328)

    SO_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Sistem Operasi").place(x=31, y=381)
    SO_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SO_Entry.place(x=306, y=377)

    A_data = Image.open("img/A.png")
    A = CTkImage(light_image=A_data, dark_image=A_data, size=(52, 50))

    Bp_data = Image.open("img/B+.png")
    Bp = CTkImage(light_image=Bp_data, dark_image=Bp_data, size=(52, 50))

    B_data = Image.open("img/B.png")
    B = CTkImage(light_image=B_data, dark_image=B_data, size=(52, 50))

    C_data = Image.open("img/C.png")
    C = CTkImage(light_image=C_data, dark_image=C_data, size=(52, 50))

    D_data = Image.open("img/D.png")
    D = CTkImage(light_image=D_data, dark_image=D_data, size=(52, 50))

    E_data = Image.open("img/E.png")
    E = CTkImage(light_image=E_data, dark_image=E_data, size=(52, 50))

    A_Button = CTkButton(master=app, text='', image=A, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='A':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=45, y=453)
    Bp_Button = CTkButton(master=app, text='', image=Bp, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B+':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=137, y=453)
    B_Button = CTkButton(master=app, text='', image=B, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=229, y=453)

    C_Button = CTkButton(master=app, text='', image=C, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='C': button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=45, y=519)
    D_Button = CTkButton(master=app, text='', image=D, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='D':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=137, y=519)
    E_Button = CTkButton(master=app, text='', image=E, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='E':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=SDG_Entry, MK3_Entry=BD_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=SD_Entry, MK6_Entry=SO_Entry)).place(x=229, y=519)
    app.mainloop()

def j5_page(asd, main):  #yang dimaksud asd itu page sebelumnya, jadi di page ini page sebelumnya bakal diclose
    asd.destroy()
    global string
    global counter
    string += '55'
    app = CTkToplevel()
    app.title("Input Nilai")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')


    bg_data = Image.open("img/BG_INPUTNILAINEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)
    ALP_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Algoritma & Pemrograman").place(x=31, y=136)
    ALP_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    ALP_Entry.place(x=326, y=132)

    KDJK_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Komunikasi Data dan Jaringan Komputer").place(x=31, y=185)
    KDJK_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    KDJK_Entry.place(x=326, y=181)

    RPL_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Rekayasa Perangkat Lunak").place(x=31, y=234)
    RPL_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    RPL_Entry.place(x=326, y=230)

    MI_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Informatika").place(x=31, y=283)
    MI_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MI_Entry.place(x=326, y=279)

    MD2_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Matematika Diskrit 2").place(x=31, y=332)
    MD2_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    MD2_Entry.place(x=326, y=328)

    SO_Text = CTkLabel(master=app, font=font, text_color='white', fg_color='#95B0DF', text="Sistem Operasi").place(x=31, y=381)
    SO_Entry = CTkTextbox(master=app, width=50, height=30, fg_color='white', text_color='black', border_color='#95B0DF', font=font2)
    SO_Entry.place(x=326, y=377)

    A_data = Image.open("img/A.png")
    A = CTkImage(light_image=A_data, dark_image=A_data, size=(52, 50))

    Bp_data = Image.open("img/B+.png")
    Bp = CTkImage(light_image=Bp_data, dark_image=Bp_data, size=(52, 50))

    B_data = Image.open("img/B.png")
    B = CTkImage(light_image=B_data, dark_image=B_data, size=(52, 50))

    C_data = Image.open("img/C.png")
    C = CTkImage(light_image=C_data, dark_image=C_data, size=(52, 50))

    D_data = Image.open("img/D.png")
    D = CTkImage(light_image=D_data, dark_image=D_data, size=(52, 50))

    E_data = Image.open("img/E.png")
    E = CTkImage(light_image=E_data, dark_image=E_data, size=(52, 50))

    A_Button = CTkButton(master=app, text='', image=A, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='A':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=45, y=453)
    Bp_Button = CTkButton(master=app, text='', image=Bp, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B+':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=137, y=453)
    B_Button = CTkButton(master=app, text='', image=B, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='B':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=229, y=453)

    C_Button = CTkButton(master=app, text='', image=C, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='C': button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=45, y=519)
    D_Button = CTkButton(master=app, text='', image=D, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='D':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=137, y=519)
    E_Button = CTkButton(master=app, text='', image=E, fg_color='white', hover=False, border_color='white', bg_color='white', command=lambda invalue='E':  button_handler(main=main, asd=app, invalue=invalue, MK1_Entry=ALP_Entry,
                                                                                                                                                                           MK2_Entry=KDJK_Entry, MK3_Entry=RPL_Entry,
                                                                                                                                                                           MK4_Entry=MI_Entry, MK5_Entry=MD2_Entry, MK6_Entry=SO_Entry)).place(x=229, y=519)
    app.mainloop()

def sertifikat_page(asd, main):
    asd.destroy()
    app = CTkToplevel()
    app.title("Input Sertifikat")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')

    bg_data = Image.open("img/BG_SERTIFNEW.png")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 12)

    centang_data = Image.open("img/Y.png")
    centang = CTkImage(dark_image=centang_data, light_image=centang_data, size=(87, 83))

    silang_data = Image.open("img/N.png")
    silang = CTkImage(dark_image=silang_data, light_image=silang_data, size=(87, 83))

    centang_button = CTkButton(master=app, text='', image=centang, bg_color='white', fg_color='white', hover=False, 
                               command = lambda invalue='Y': sertif_handler(main, app, invalue)).place(x=48, y=428)
    silang_button = CTkButton(master=app, text='', image=silang, bg_color='white', fg_color='white', hover=False,
                              command=lambda invalue='T': sertif_handler(main, app, invalue)).place(x=211, y=428)

    app.mainloop()

def hasil_page(asd, main):
    global nilai_list
    global string
    asd.destroy()

    a = dfa()
    a.addFinalState("ACC")
    result = automata(a, string)

    app = CTkToplevel()
    app.title("Hasil Penjurusan")
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()   
    app.geometry("405x637") 
    x = (screen_width - 405) // 2
    y = (screen_height - 637) // 2
    app.geometry(f"+{x}+{y}")
    app.configure(fg_color='#95B0DF')

    bg_data = Image.open("img/SELEKSINEW.jpg")
    bg = CTkImage(dark_image=bg_data, light_image=bg_data, size=(405, 637))
    CTkLabel(master=app, text='', image=bg).place(x=0, y=0)

    font = CTkFont("Jost Bold", 15)
    font2 = CTkFont("Jost Bold", 10)
    font3 = CTkFont("Jost Bold", 8)
    dict = {'A': '1', 'B+': '2', 'B': '3', 'C': '4', 'D': '5', 'E': '6'}
    dict = {v: k for k, v in dict.items()}
    global sertif_status
    
    if string[0] == '1':
        CTkLabel(master=app, text='J1', font=font, bg_color='white', fg_color='white', text_color='black').place(x=280, y=106)

        MK1_Text = CTkLabel(master=app, font=font2, text='Algoritma dan Pemrograman', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=207)
        nilai1 = nilai_list[0][1]
        nilai1 = dict.get(nilai1, nilai1)
        MK1_Nilai = CTkLabel(master=app, font=font, text=nilai1, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=207)
        
        MK2_Text = CTkLabel(master=app, font=font2, text='Teori Bahasa dan Otomata', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=247)
        nilai2 = nilai_list[1][1]
        nilai2 = dict.get(nilai2, nilai2)
        MK2_Nilai = CTkLabel(master=app, font=font, text=nilai2, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=247)
        
        MK3_Text = CTkLabel(master=app, font=font2, text='Basis Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=282)
        nilai3 = nilai_list[2][1]
        nilai3 = dict.get(nilai3, nilai3)
        MK3_Nilai = CTkLabel(master=app, font=font, text=nilai3, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=282)

        MK4_Text = CTkLabel(master=app, font=font2, text='Matematika Informatika', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=320)
        nilai4 = nilai_list[3][1]
        nilai4 = dict.get(nilai4, nilai4)
        MK4_Nilai = CTkLabel(master=app, font=font, text=nilai4, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=320)

        MK5_Text = CTkLabel(master=app, font=font2, text='Struktur Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=358)
        nilai5 = nilai_list[4][1]
        nilai5 = dict.get(nilai5, nilai5)
        MK5_Nilai = CTkLabel(master=app, font=font, text=nilai5, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=358)
        
        MK6_Text = CTkLabel(master=app, font=font2, text='Matematika Diskrit 1', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=393)
        nilai6 = nilai_list[5][1]
        nilai6 = dict.get(nilai6, nilai6)
        MK6_Nilai = CTkLabel(master=app, font=font, text=nilai6, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=393)
    
    if string[0] == '2':
        CTkLabel(master=app, text='J2', font=font, bg_color='white', fg_color='white', text_color='black').place(x=280, y=106)

        MK1_Text = CTkLabel(master=app, font=font2, text='Algoritma dan Pemrograman', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=207)
        nilai1 = nilai_list[0][1]
        nilai1 = dict.get(nilai1, nilai1)
        MK1_Nilai = CTkLabel(master=app, font=font, text=nilai1, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=207)
        
        MK2_Text = CTkLabel(master=app, font=font2, text='Rekayasa Perangkat Lunak', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=247)
        nilai2 = nilai_list[1][1]
        nilai2 = dict.get(nilai2, nilai2)
        MK2_Nilai = CTkLabel(master=app, font=font, text=nilai2, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=247)
        
        MK3_Text = CTkLabel(master=app, font=font2, text='Basis Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=282)
        nilai3 = nilai_list[2][1]
        nilai3 = dict.get(nilai3, nilai3)
        MK3_Nilai = CTkLabel(master=app, font=font, text=nilai3, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=282)

        MK4_Text = CTkLabel(master=app, font=font2, text='Matematika Informatika', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=320)
        nilai4 = nilai_list[3][1]
        nilai4 = dict.get(nilai4, nilai4)
        MK4_Nilai = CTkLabel(master=app, font=font, text=nilai4, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=320)

        MK5_Text = CTkLabel(master=app, font=font2, text='Struktur Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=358)
        nilai5 = nilai_list[4][1]
        nilai5 = dict.get(nilai5, nilai5)
        MK5_Nilai = CTkLabel(master=app, font=font, text=nilai5, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=358)
        
        MK6_Text = CTkLabel(master=app, font=font2, text='Desain dan Analisis Algoritma', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=393)
        nilai6 = nilai_list[5][1]
        nilai6 = dict.get(nilai6, nilai6)
        MK6_Nilai = CTkLabel(master=app, font=font, text=nilai6, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=393)
        
    if string[0] == '3':
        CTkLabel(master=app, text='J3', font=font, bg_color='white', fg_color='white', text_color='black').place(x=280, y=106)

        MK1_Text = CTkLabel(master=app, font=font2, text='Algoritma dan Pemrograman', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=207)
        nilai1 = nilai_list[0][1]
        nilai1 = dict.get(nilai1, nilai1)
        MK1_Nilai = CTkLabel(master=app, font=font, text=nilai1, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=207)
        
        MK2_Text = CTkLabel(master=app, font=font2, text='Matematika Informatika', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=247)
        nilai2 = nilai_list[1][1]
        nilai2 = dict.get(nilai2, nilai2)
        MK2_Nilai = CTkLabel(master=app, font=font, text=nilai2, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=247)
        
        MK3_Text = CTkLabel(master=app, font=font2, text='Basis Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=282)
        nilai3 = nilai_list[2][1]
        nilai3 = dict.get(nilai3, nilai3)
        MK3_Nilai = CTkLabel(master=app, font=font, text=nilai3, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=282)

        MK4_Text = CTkLabel(master=app, font=font2, text='Sistem Digital', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=320)
        nilai4 = nilai_list[3][1]
        nilai4 = dict.get(nilai4, nilai4)
        MK4_Nilai = CTkLabel(master=app, font=font, text=nilai4, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=320)

        MK5_Text = CTkLabel(master=app, font=font2, text='Desain dan Analisis Algoritma', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=358)
        nilai5 = nilai_list[4][1]
        nilai5 = dict.get(nilai5, nilai5)
        MK5_Nilai = CTkLabel(master=app, font=font, text=nilai5, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=358)
        
        MK6_Text = CTkLabel(master=app, font=font2, text='Matematika Diskrit 1', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=393)
        nilai6 = nilai_list[5][1]
        nilai6 = dict.get(nilai6, nilai6)
        MK6_Nilai = CTkLabel(master=app, font=font, text=nilai6, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=393)


    if string[0] == '4':
        CTkLabel(master=app, text='J4', font=font, bg_color='white', fg_color='white', text_color='black').place(x=280, y=106)

        MK1_Text = CTkLabel(master=app, font=font2, text='Algoritma dan Pemrograman', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=207)
        nilai1 = nilai_list[0][1]
        nilai1 = dict.get(nilai1, nilai1)
        MK1_Nilai = CTkLabel(master=app, font=font, text=nilai1, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=207)
        
        MK2_Text = CTkLabel(master=app, font=font2, text='Sistem Digital', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=247)
        nilai2 = nilai_list[1][1]
        nilai2 = dict.get(nilai2, nilai2)
        MK2_Nilai = CTkLabel(master=app, font=font, text=nilai2, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=247)
        
        MK3_Text = CTkLabel(master=app, font=font2, text='Basis Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=282)
        nilai3 = nilai_list[2][1]
        nilai3 = dict.get(nilai3, nilai3)
        MK3_Nilai = CTkLabel(master=app, font=font, text=nilai3, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=282)

        MK4_Text = CTkLabel(master=app, font=font2, text='Matematika Informatika', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=320)
        nilai4 = nilai_list[3][1]
        nilai4 = dict.get(nilai4, nilai4)
        MK4_Nilai = CTkLabel(master=app, font=font, text=nilai4, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=320)

        MK5_Text = CTkLabel(master=app, font=font2, text='Struktur Data', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=358)
        nilai5 = nilai_list[4][1]
        nilai5 = dict.get(nilai5, nilai5)
        MK5_Nilai = CTkLabel(master=app, font=font, text=nilai5, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=358)
        
        MK6_Text = CTkLabel(master=app, font=font2, text='Sistem Operasi', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=393)
        nilai6 = nilai_list[5][1]
        nilai6 = dict.get(nilai6, nilai6)
        MK6_Nilai = CTkLabel(master=app, font=font, text=nilai6, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=393)
        
    if string[0] == '5':
        CTkLabel(master=app, text='J5', font=font, bg_color='white', fg_color='white', text_color='black').place(x=280, y=106)

        MK1_Text = CTkLabel(master=app, font=font2, text='Algoritma dan Pemrograman', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=207)
        nilai1 = nilai_list[0][1]
        nilai1 = dict.get(nilai1, nilai1)
        MK1_Nilai = CTkLabel(master=app, font=font, text=nilai1, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=207)
        
        MK2_Text = CTkLabel(master=app, font=font3, text='Komunikasi Data dan Jaringan Komputer', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=247)
        nilai2 = nilai_list[1][1]
        nilai2 = dict.get(nilai2, nilai2)
        MK2_Nilai = CTkLabel(master=app, font=font, text=nilai2, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=247)
        
        MK3_Text = CTkLabel(master=app, font=font2, text='Rekayasa Perangkat Lunak', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=282)
        nilai3 = nilai_list[2][1]
        nilai3 = dict.get(nilai3, nilai3)
        MK3_Nilai = CTkLabel(master=app, font=font, text=nilai3, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=282)

        MK4_Text = CTkLabel(master=app, font=font2, text='Matematika Informatika', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=320)
        nilai4 = nilai_list[3][1]
        nilai4 = dict.get(nilai4, nilai4)
        MK4_Nilai = CTkLabel(master=app, font=font, text=nilai4, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=320)

        MK5_Text = CTkLabel(master=app, font=font2, text='Matematika Diskrit 2', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=358)
        nilai5 = nilai_list[4][1]
        nilai5 = dict.get(nilai5, nilai5)
        MK5_Nilai = CTkLabel(master=app, font=font, text=nilai5, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=358)
        
        MK6_Text = CTkLabel(master=app, font=font2, text='Sistem Operasi', bg_color='white', fg_color='white',
                            text_color='black').place(x=63, y=393)
        nilai6 = nilai_list[5][1]
        nilai6 = dict.get(nilai6, nilai6)
        MK6_Nilai = CTkLabel(master=app, font=font, text=nilai6, bg_color='white', fg_color='white',
                            text_color='black').place(x=280, y=393)

    if result==True:
        result_text = 'Diterima'
    elif result==False:
        result_text = 'Ditolak'
    
    if sertif_status == 'Y':
        sertif_text = 'Punya'
        CTkLabel(master=app, text=sertif_text, font=font, bg_color='white', fg_color='white', text_color='black').place(x=265, y=451)
    elif sertif_status == 'T':
        sertif_text = "Tidak Punya"
        CTkLabel(master=app, text=sertif_text, font=font, bg_color='white', fg_color='white', text_color='black').place(x=245, y=451)

    
    CTkLabel(master=app, text=result_text, font=font, bg_color='white', fg_color='white', text_color='black').place(x=260, y=520)
    next_data = Image.open("img/button_next.png")
    next_img = CTkImage(light_image=next_data, dark_image=next_data, size=(50, 50))
    next_button = CTkButton(master=app, text='', image=next_img, hover=False, fg_color='white', bg_color='white', command=lambda: close_page(app, main))
    next_button.place(x=135, y=575)


def close_page(asd, main):
    asd.destroy()
    main.destroy()