# import all the thing that we want
from logging import PlaceHolder
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube
# import the all the things
def download():
    link = video_link.get()
    save_dir = download_dir.get()
    print(save_dir)
    yt = YouTube(link)
    yt.streams.first().download(save_dir)
    messagebox.showinfo(title="message" , message="download succsud!")
def browse():
    directory = askdirectory(initialdir="YOUR DIRECTORY PATH" , title="save")
    download_dir.set(directory)
    
### make the instance from out class
window = tk.Tk()
window.title("youtube downloader")
window.minsize(450,200)
### make two variable
download_dir = tk.StringVar()
video_link = tk.StringVar()
### make the label
link_label = tk.Label(window , text="Vide link")
link_label.grid(row=0,column=0,padx=10, pady=10)
link_label.config(font=("None",15) , fg="blue")
### make the link input
link_input = tk.Entry(window , width=30,textvariable=video_link)
link_input.grid(row=0,column=1 , sticky="w")
### make the scound label
place_label = tk.Label(window , text="File" , bd=1 , fg="green")
place_label.grid(row=2 , column=0 , padx=2 , pady=2)
place_label.config(font=("None",15))
### make the directory input
place_input = tk.Entry(window , width=30,textvariable=download_dir)
place_input.grid(row=2,column=1)
### make the open buttom
file_search = tk.Button(text="open" , width=12,command=browse , pady=5)
file_search.grid(row=2 , column=2)
file_search.config(fg="blue")
### make the download buttom
download_btn = tk.Button(text="download",command=download , padx=3)
download_btn.grid(row=3 , column=1)
download_btn.config(height=3 , width=20 , bg="green" , fg="white")



window.mainloop()