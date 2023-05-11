import tkinter as tk
from tkinter import filedialog
from pytube import YouTube, Playlist

VERSION = "1.1"

"""Note that downloading YouTube or Instagram videos is against their terms of service, 
and you should not use this project to engage in any activities that violate those terms. 
This application is intended for personal use only and not for any commercial or illegal activities."""

def browse_folder_path():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def download_video():
    youtube_url = url_entry.get()
    save_path = folder_path.get()

    if not save_path:
        save_path = './'

    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(save_path)
        status_label.config(text="Download Successful!")
    except Exception as e:
        error = "Download Failed! Check console for more information."
        status_label.config(text=error)
        print(e)

def download_playlist():
    playlist_url = playlist_entry.get()
    save_path = folder_path.get()

    if not save_path:
        save_path = './'

    try:
        pl = Playlist(playlist_url)
        for video in pl.videos:
            stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            stream.download(save_path)
        status_label.config(text="Download Successful!")
    except Exception as e:
        error = "Download Failed! Check console for more information."
        status_label.config(text=error)
        print(e)

#Initialize GUI root
root = tk.Tk()
title = "Video Downloader GUI Version: " + str(VERSION)
root.title(title)

#Labels
url_label = tk.Label(root, text="YouTube Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

playlist_label = tk.Label(root, text="YouTube Playlist URL:")
playlist_label.grid(row=1, column=0, padx=5, pady=5)

playlist_entry = tk.Entry(root, width=50)
playlist_entry.grid(row=1, column=1, padx=5, pady=5)

folder_label = tk.Label(root, text="Save Video To:")
folder_label.grid(row=2, column=0, padx=5, pady=5)

folder_path = tk.StringVar()
folder_path.set('')
folder_entry = tk.Entry(root, textvariable=folder_path, width=50)
folder_entry.grid(row=2, column=1, padx=5, pady=5)

folder_button = tk.Button(root, text="Browse", command=browse_folder_path)
folder_button.grid(row=2, column=2, padx=5, pady=5)

download_video_button = tk.Button(root, text="Download Video", command=download_video)
download_video_button.grid(row=3, column=1, padx=5, pady=5)

download_playlist_button = tk.Button(root, text="Download Playlist", command=download_playlist)
download_playlist_button.grid(row=4, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="")
status_label.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
