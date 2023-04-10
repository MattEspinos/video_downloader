from pytube import YouTube

VERSION = 1.0
"""
Version 1.0
This application will download a youtube video from a specified URL. The video will be
downloaded in the highest quality. Note that downloading YouTube videos may violate YouTube's terms of service, 
so make sure you have the necessary permissions before downloading any content. 
"""

def download(yt, path):
     #With path
     streams = yt.streams.get_highest_resolution()
     streams.download(output_path=path)

def download(yt):
    #Without path
    streams = yt.streams.get_highest_resolution()
    streams.download()

def fetch_video():
    again = 'y'
    try:
            while again.lower() == 'y' or again.lower() == 'yes':
                url = str(input("Enter the URL of the YouTube video:\t"))
                yt = YouTube(url)
                print("Title:", yt.title)
                print("Length:", yt.length, "seconds")
                print("Author:", yt.author)

                path = str(input("Enter path for download video to go to. Leave blank for same path as this file:\t"))

                if(path):
                    download(yt, path)
                else:
                    download(yt)
                
                print("Video downloaded successfuly!\n")
                again = str(input("Would you like to download another video? (Y/n):\t"))

                if(not again):
                     again = 'y'


    except:
         print("An error occured")


def main():
    print(VERSION)
    print("Welcome to the Video Downloader\n")

    fetch_video()

main()
