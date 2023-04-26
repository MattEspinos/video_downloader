# Video Downloader
Video Downloader is a Python command-line and GUI application that allows you to download videos from YouTube and Instagram.

## Prerequisites
Before using Video Downloader, you need to have the following installed:

* Python 3.5 or later
* pip

## Installation
1. Clone the repository or download the source code.

2. Install the dependencies using pip and the requirements.txt file:
  ```
  pip install -r requirements.txt
  ```

3. Run the application using Python:
  ```
  python video_downloader.py [options]
  ```

## Usage
### video_downloader.py
To download a video, run the video_downloader.py script with the following options:
usage: 
```
video_downloader.py [-h] [-p PATH] [-t {youtube,instagram}] url
```

positional arguments:
  * url  -> URL of the video.

optional arguments:
  * -h, --help            show this help message and exit
  * -p PATH, --path PATH  Path to save the video.
  * -t {youtube,instagram}, --type {youtube,instagram}
                        Platform to download from ('youtube', or 'instagram').
                        Default is 'youtube'.
For example, to download a video from YouTube:
```
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -p ~/Downloads/videos
```
### video_downloader_gui.py
1. Open the program by running python youtube_downloader.py in your terminal. Or by clicking on the Python file
2. Enter the URL of a YouTube video or playlist in the appropriate entry field.
3. (Optional) Enter a path to save the downloaded files to in the "Save Video To" entry field. If left blank, the files will be saved to the current directory.
4. Click the "Download Video" button to download a single video, or the "Download Playlist" button to download a whole playlist.
5. If the download is successful, a "Download Successful!" message will be displayed in the program. If the download fails, a "Download Failed!" message will be displayed.
- Note that the program will download videos in the highest available quality in .mp4 format. If the video is not available in .mp4 format, the program will not be able to download it. If you encounter any issues with the program, make sure you have installed Python and PyTube correctly, and that you have a stable internet connection.
- Currently only supports YouTube.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
Note that downloading YouTube or Instagram videos is against their terms of service, 
and you should not use this project to engage in any activities that violate those terms. 
This application is intended for personal use only and not for any commercial or illegal activities.

## Acknowledgments
[PyTube](https://pytube.io/en/latest/)
[Instaloader](https://instaloader.github.io/)