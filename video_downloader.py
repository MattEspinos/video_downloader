import argparse
from pytube import YouTube
import instaloader

VERSION = "1.4"

"""Note that downloading YouTube or Instagram videos is against their terms of service, 
and you should not use this project to engage in any activities that violate those terms. 
This application is intended for personal use only and not for any commercial or illegal activities."""

def download_video(yt, path=None):
    if path:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=path)
    else:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("Video downloaded successfully!")

def fetch_video(url, path=None, platform="youtube"):
    try:
        if platform == "youtube":
            yt = YouTube(url)
            print("Video found! Downloading...")
            download_video(yt, path)
        
        elif platform == "instagram":
            L = instaloader.Instaloader()
            L.download_video(url, target=path, quiet=False)
            print("Video downloaded successfully!")
        
        else:
            print("Invalid platform entered. Please choose either 'youtube', or 'instagram'.")

    except Exception as e:
        print("An error has occurred:", e)

def main():
    parser = argparse.ArgumentParser(description="Download a video from YouTube, or Instagram.")
    parser.add_argument("url", help="URL of the video.")
    parser.add_argument("-p", "--path", help="Path to save the video.")
    parser.add_argument("-t", "--type", help="Platform to download from ('youtube', or 'instagram').", default="youtube")
    args = parser.parse_args()

    print("Version:", VERSION)
    print("Welcome to the Video Downloader\n")

    fetch_video(args.url, args.path, args.type)

if __name__ == "__main__":
    main()
