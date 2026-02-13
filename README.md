# YouTube Downloader

A simple command-line Python script to download YouTube videos in the highest available resolution.

## Features

- Downloads YouTube videos in the highest resolution available
- Displays video title and view count
- Simple command-line interface

## Requirements

- Python 3.x
- pytube library

## Installation

1. Clone or download this repository

2. Install the required dependency:
```bash
pip install pytube
```

## Usage

Run the script from the command line with a YouTube video URL as an argument:

```bash
python Youtube_Downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Example

```bash
python Youtube_Downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

The script will:
1. Display the video title
2. Show the number of views
3. Download the video in the highest resolution to the current directory

## Customization

To change the download location, modify line 11 in the script:

```python
yd.download('/path/to/your/folder')
```

## Notes

- The downloaded video will be saved in the current directory by default
- Download time depends on your internet connection and video size
- Make sure you have sufficient storage space for the video

## Troubleshooting

If you encounter errors:
- Ensure pytube is properly installed: `pip install --upgrade pytube`
- Check that the YouTube URL is valid and accessible
- Verify you have write permissions in the download directory

## Legal Notice

Please respect copyright laws and YouTube's Terms of Service. Only download videos you have permission to download.

## License

This project is provided as-is for educational purposes.
