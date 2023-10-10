# YouTube Video Downloader

**Version:** 1.2

A simple GUI-based YouTube video downloader built with Python, tkinter, and PyTube. This program allows you to easily download YouTube videos in MP4 format, selecting the highest available resolution.

**Disclaimer:** Downloading YouTube videos may violate YouTube's Terms of Service. This application is intended for personal use only. Be sure to respect YouTube's policies and use this tool responsibly.

## Features

- Download YouTube videos in MP4 format.
- Choose the save location for downloaded videos.
- Real-time download progress tracking.
- User-friendly GUI interface.

## Installation

1. **Python**: Ensure you have Python 3.x installed on your system. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

2. **Required Packages**: Install the necessary Python packages using pip:

   ```shell
   pip install pytube customtkinter
   ```

3. **Running the Program**: Run the `youtube_video_downloader.py` script to start the YouTube Video Downloader.

   ```shell
   python youtube_video_downloader.py
   ```

4. **Executable (Optional)**: An executable (`.exe`) version of the program can be generated using PyInstaller. Execute the following command to create an executable:

   ```shell
   pyinstaller --onefile youtube_video_downloader.py
   ```

   The executable will be available in the `dist` folder.

## How to Use

1. Launch the program by running `youtube_video_downloader.py`.

2. Paste a valid YouTube video URL into the "Insert a YouTube Video Link" field.

3. Optionally, specify a folder to save the downloaded video in the "Save Video To" field or use the "Browse" button to select a folder.

4. Click the "Download" button to start downloading the video.

5. The download progress will be displayed in real-time with a progress bar and percentage.

6. Once the download is complete, you'll see a "Download Complete!" message.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Python](https://www.python.org/): The programming language used for this project.
- [PyTube](https://pytube.io/): Used for downloading YouTube videos.
- [customtkinter](https://pypi.org/project/customtkinter/): A custom tkinter package used for enhancing the GUI.