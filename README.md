# **Playlist Automator: YouTube Playlist Downloader**

## Overview  
**Playlist Automator** is a Python-based tool designed to automate the process of downloading YouTube playlists. With an intuitive graphical user interface (GUI), users can input a YouTube playlist URL and specify a folder to save the downloaded videos. The application handles the entire playlist download efficiently, reducing manual effort significantly.

---

## Features  
- **Automated Playlist Download**: Easily download entire YouTube playlists with a single click.  
- **User-Friendly GUI**: Built using Tkinter, providing a simple and clean interface.  
- **Folder Selection**: Allows users to browse and select the folder where downloads will be saved.  
- **Error Handling**: Provides error messages for failed downloads to help users troubleshoot issues.  
- **Customizable Output Format**: Supports downloading videos in the best available format.

---

## Prerequisites  
Make sure you have the following Python packages installed:  
- `yt-dlp` (YouTube Downloader Library)  
- `tkinter` (for GUI development)  
- `Pillow` (for handling image resources)  

You can install these packages using the following command:  
```bash  
pip install yt-dlp pillow  
```  

---

## How to Run  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/abinayagoudjandhyala/Playlist-Automator.git  
   cd Playlist-Automator  
   ```  
2. Run the Python script:  
   ```bash  
   python main.py  
   ```  
3. A GUI window will open asking for the YouTube playlist URL and the download destination.  
4. Enter the playlist URL and select the desired folder to save the downloads.  
5. Click the "Download Playlist" button to start the process.

---

## Project Structure  
```
Playlist-Automator/
│
├── background.jpg         # Background image for GUI (replace with your custom image if needed)  
├── app.py                 # Main Python script to run the app  
└── README.md               # This file  
```

---

## Disclaimer  
**This tool is intended solely for educational purposes and complies with YouTube's terms and conditions. Use responsibly.**
