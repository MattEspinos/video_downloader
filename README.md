# Video Downloader
Video Downloader is a Python command-line application that allows you to download videos from YouTube and Instagram.

## Prerequisites
Before using Video Downloader, you need to have the following installed:

* Python 3.5 or later

## Installation
1. Clone the repository or download the source code.

2. Install the dependencies using pip and the requirements.txt file:
    * pip install -r requirements.txt

3. Run the application using Python:
    * python video_downloader.py [options]

## Usage
To download a video, run the video_downloader.py script with the following options:
usage: video_downloader.py [-h] [-p PATH] [-t {youtube,instagram}] url

Download a video from YouTube, or Instagram.

positional arguments:
  url                   URL of the video.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to save the video.
  -t {youtube,instagram}, --type {youtube,instagram}
                        Platform to download from ('youtube', or 'instagram').
                        Default is 'youtube'.
For example, to download a video from YouTube:
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -p ~/Downloads/videos

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
[PyTube](https://pytube.io/en/latest/)
[Instaloader](https://instaloader.github.io/)
