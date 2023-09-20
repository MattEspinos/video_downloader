import tkinter, customtkinter
from pytube import YouTube
from tkinter import messagebox, filedialog

#Functions
def startDownload():
    try:
        ytLink = link.get()
        folder = path_link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        title.configure(text=ytObject.title, text_color='white')
        finishLabel.configure(text='')
        
        if folder != '':
            video.download(folder)
        else:
            video.download()
        
        finishLabel.configure(text='Download Complete!')
    except:
        messagebox.showerror('Invalid URL', 'Please check the URL and try again.')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_completion) / 100)

def browse_folder_path():
    folder_selected = filedialog.askdirectory()
    path_link.insert(0, folder_selected)

#System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

#App Frame
app = customtkinter.CTk()
app.geometry('720x480')
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure((0, 2), weight=1)
app.title('Youtube Video Downloader')

#Title
title = customtkinter.CTkLabel(app, text='YouTube Video Downloader')
title.grid(row=0, column=0, padx=10, sticky="nsew", columnspan=3)

#Insert Link Text
yt_video_label = customtkinter.CTkLabel(app, text='Insert a YouTube Video Link:')
yt_video_label.grid(row=1, column=0, padx=10, sticky="nsew")

#Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=300, height=40, textvariable=url_var)
link.grid(row=1, column=1, sticky="ew")

#Insert folder text
folder_label = customtkinter.CTkLabel(app, text='Save Video To:')
folder_label.grid(row=2, column=0, padx=10, pady=(10,50), sticky="nsew")

#Folder Link Input
folder_path = tkinter.StringVar()
path_link = customtkinter.CTkEntry(app, width=300, height=40, textvariable=folder_path)
path_link.grid(row=2, column=1, pady=(10,50), sticky="ew")

#Browse Button
browse_button = customtkinter.CTkButton(app, text='Browse', command=browse_folder_path)
browse_button.grid(row=2, column=2, padx=10, pady=(10,50))

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.grid(row=3, column=0, columnspan=3, sticky="ew")

#Progress percentage
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.grid(row=4, column=0, columnspan=3)

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.grid(row=5, column=0, padx=10, pady=10, columnspan=3)

#Download Button
download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.grid(row=6, column=0, padx=200, pady=50, columnspan=3)

#Run App
app.mainloop()