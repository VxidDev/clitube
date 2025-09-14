# CliTube

CliTube is a command-line tool to search, play, and download YouTube videos directly from your terminal.  
It’s lightweight, cross-platform (Python + mpv + yt-dlp), and perfect for quick video playback without opening a browser.

---

## Features

- Search YouTube videos by name.
- Play videos in `mpv` directly from terminal.
- Download videos with `yt-dlp`.
- Loop videos or disable video/audio as needed.
- Colored terminal output for status messages and errors.

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/VxidDev/clitube.git
cd clitube
```
### 2. Install using pip
```bash
pip install .
```

## System requirements

Make sure the following are installed and available in your PATH:

- yt-dlp
- mpv
- Python 3.10+
- colorama

## Usage
### Play a video by name
```bash
clitube --name="Song Name" --play
```
### Play a video by ID
```bash
clitube --id=<VIDEO_ID> --play
```
### Download a video by name or ID
```bash
clitube --name="Song Name" --download
clitube --id=<VIDEO_ID> --download
```
### Additional options

- --loop → loop video playback

- --no-video → play audio only

- --no-audio → play video only

### Search for multiple results
```bash
clitube --name="Song Name" --search 5
```
# License

MIT License – feel free to use and modify.




