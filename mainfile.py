import tkinter as tk
from compressinfunction import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file that you want to compress or decompress")
    return filename

def compression(i,o):
    compress(i, o)

def decompression(i,o):
    decompress(i,o)    


window = tk.Tk()
window.title("compression/decompression engine")
window.geometry("600x400")



inputlabel = tk.Label(window,text="file to be compressed/decompressed")
outputentry = tk.Entry(window)


compressbutton = tk.Button(window,text="compress",command=lambda: compression(open_file(),outputentry.get()))
decompressbutton = tk.Button(window,text="decompress",command=lambda: decompression(open_file(),outputentry.get()))

inputlabel.grid(row=0,column=0)
outputentry.grid(row=0,column=1)
compressbutton.grid(row=0,column=2)
decompressbutton.grid(row=0,column=3)

window.mainloop()