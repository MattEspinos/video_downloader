import argparse
from pytube import YouTube

VERSION = 1.2
"""
Version 1.2
This application will download a youtube video from a specified URL. The video will be
downloaded in the highest quality. Note that downloading YouTube videos may violate YouTube's terms of service, 
so make sure you have the necessary permissions before downloading any content. 
"""

def download_video(yt, path=None):
    if path:
        streams = yt.streams.get_highest_resolution()
        streams.download(output_path=path)
    else:
        yt.streams.get_highest_resolution().download()
    print("Video downloaded successfully!")

def fetch_youtube_video(url, path=None):
    try:
        yt = YouTube(url)
        print("Title:", yt.title)
        print("Length:", yt.length, "seconds")
        print("Author:", yt.author)

        download_video(yt, path)

    except Exception as e:
        print("An error has occurred:", e)

def main():
    parser = argparse.ArgumentParser(description="Download a YouTube video.")
    parser.add_argument("url", help="URL of the YouTube video.")
    parser.add_argument("-p", "--path", help="Path to save the video.")
    args = parser.parse_args()

    print("Version:", VERSION)
    print("Welcome to the Video Downloader\n")

    fetch_youtube_video(args.url, args.path)

if __name__ == "__main__":
    main()
