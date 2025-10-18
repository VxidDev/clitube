# 🎬 CliTube

CliTube is a command-line tool to search, play, and download YouTube videos — directly from your terminal.
It’s lightweight, cross-platform, and built with Python, mpv, and yt-dlp for fast, browser-free playback.

## 🚀 Features

- 🔍 Search YouTube videos by name or ID.

- ▶️ Play videos directly using mpv.

- 💾 Download videos easily with yt-dlp.

- 🔁 Loop playback or disable video/audio streams.

- 🌈 Colored terminal logs powered by Rich.

- 🧠 Debug mode for transparent command output.

## ⚙️ Installation

*🧪 Tested only on Arch Linux (but should work on most UNIX systems)*.

### Clone the repository
```
git clone https://github.com/VxidDev/clitube.git
cd clitube
```
2. Install with pip
```
pip install .
```
## 🧱 Requirements

### Make sure these dependencies are installed and accessible in your system PATH:

- yt-dlp

- mpv

- python >= 3.10

- pip

- rich

- typer

- tomli

## 💡 Usage

### Once installed, run clitube followed by a subcommand.

▶️ Play a video

Play by name:
```
clitube play --name "Rick Astley Never Gonna Give You Up"
```
Play by video ID:
```
clitube play --id dQw4w9WgXcQ
```

Optional flags:

```--loop``` → Loop playback

```--no-audio``` → Disable audio

```--no-video``` → Disable video

```--debug``` → Show detailed logs

💾 Download a video

By name:
```
clitube download --name "Cool Music Mix"
```
By ID:
```
clitube download --id dQw4w9WgXcQ
```
Debug mode example:
```
clitube download --name "Coding Music" --debug
```
🔎 Search for videos

Show multiple search results:
```
clitube search --amount 5 --name "lofi hip hop"
```
🧾 Check version
```
clitube version
```
🧰 Example workflow
```
# Search and find the video ID
clitube search --amount 3 --name "retro synthwave mix"

# Play it
clitube play --id <VIDEO_ID> --loop
```
## 📜 License

MIT License – free to use, modify, and share.
Created with ❤️ by VxidDev
