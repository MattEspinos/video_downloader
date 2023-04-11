# Video Downloader
A Python command-line application to download videos from YouTube.

## Requirements
Python 3.x
pytube library

## Installation
1. Install the required packages using pip:
pip install -r requirements.txt
2. Run the script using Python:
python video_downloader.py <url> [-p <path>]

## Usage
Run the script from the command line with the following command:
python video_downloader.py [URL] [-p PATH]
[URL] - The URL of the YouTube video.
[-p PATH] (optional) - The path where the video will be downloaded. If not provided, the video will be downloaded to the current working directory.

## Example
python video_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -p C:\users\Downloads
This will download the video with the URL https://www.youtube.com/watch?v=dQw4w9WgXcQ to the C:\users\Downloads folder.

## Notes
Downloading videos from YouTube may violate the terms of service of these platforms. Make sure you have the necessary permissions before downloading any content.