from ctypes import resize
from textwrap import wrap
from tkinter import *
from pytube import YouTube

window =  Tk()
window.title("YouTube Video Downloader")
window.resizable(width=False, height=False)
canvas = Canvas(window, width=500, height=500)
canvas.grid(columnspan=3, rowspan=50)

#Get user input from box
def get_video():
    global input
    string = input.get()
    yt = YouTube(string)
    streams = yt.streams.filter(file_extension="mp4")
    list = streams.filter(file_extension="mp4").asc()
    row = 4
    for i in list:
        i = Label(window, text=i, wraplength=100)
        i.grid(columnspan=3, row=row)
        row += 1

#Title and subtitle
title = Label(window, text='Youtube Downloader', font=('Railway', 20))
title.grid(columnspan=3, column=0, row=0)
subtitle = Label(window, text="Paste a YouTube Link to download")
subtitle.grid(columnspan=3, column=0, row=1)

#Input box
input = Entry(window, width=50)
input.grid(columnspan=3, row=2)

#Button
button = Button(window, text="Download", command=get_video).grid(columnspan=3, row=3)

#Display input
input_disp = Label(window, text="")
input_disp.grid(columnspan=3, row=4)

window.mainloop()