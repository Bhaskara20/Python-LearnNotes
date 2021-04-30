import tkinter

#variabel
window=tkinter.Tk()

#inisiasi
label1=tkinter.Label(window,text="Andru")
label2=tkinter.Label(window,text="Anggi")

tombol1=tkinter.Button(window,text="Register")
tombol2=tkinter.Button(window,text="Log out")

#memposisikan
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#gui
window.mainloop()