import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, Label, Entry, Button, GROOVE
from PIL import Image, ImageTk  # Ensure you have Pillow installed

def download_playlist():
    youtube_url = video_link.get()
    download_folder = download_path.get()

    ydl_opts = {
        'outtmpl': f'{download_folder}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        'format': 'best',
        'noplaylist': False,  # Allows downloading of entire playlists
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        messagebox.showinfo("Success", "Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download playlist: {str(e)}")

def browse_folder():
    download_directory = filedialog.askdirectory()
    download_path.set(download_directory)

# Setup the main window
root = tk.Tk()
root.geometry("800x400")
root.resizable(False, False)
root.title("YouTube Playlist Downloader")

# Load and set the background image
bg_image = Image.open("background.jpg")  # Ensure the image file is in the same directory
bg_image = bg_image.resize((800, 400), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Variables to store the link and destination path
video_link = StringVar()
download_path = StringVar()

# Creating and placing the widgets
header_label = Label(root, text="YouTube Playlist Downloader", padx=15, pady=15, font="SegoeUI 24 bold", bg="#ffcc00", fg="#333333")
header_label.place(relx=0.5, rely=0.1, anchor="center")

playlist_link_label = Label(root, text="Playlist Link:", bg="#ff6600", fg="white", pady=10, padx=10, font="Arial 14 bold")
playlist_link_label.place(x=50, y=100, anchor="w")

playlist_link_entry = Entry(root, width=50, textvariable=video_link, font="Arial 14", bd=3, relief=GROOVE)
playlist_link_entry.place(x=200, y=100, anchor="w")

save_folder_label = Label(root, text="Save to Folder:", bg="#ff6600", fg="white", pady=10, padx=10, font="Arial 14 bold")
save_folder_label.place(x=50, y=150, anchor="w")

save_folder_entry = Entry(root, width=37, textvariable=download_path, font="Arial 14", bd=3, relief=GROOVE)
save_folder_entry.place(x=200, y=150, anchor="w")

browse_button = Button(root, text="Browse", command=browse_folder, width=12, bg="#66ff66", fg="black", font="Arial 12 bold", relief=GROOVE)
browse_button.place(x=500, y=145, anchor="w")

download_button = Button(root, text="Download Playlist", command=download_playlist, width=20, bg="#33cc33", fg="white", pady=10, padx=10, relief=GROOVE, font="Georgia 16 bold")
download_button.place(relx=0.5, rely=0.7, anchor="center")

# Footer with disclaimer
footer_label = Label(root, text="This tool is intended solely for educational purposes and complies with YouTube's terms and conditions.", bg="#f0f0f0", fg="#666666", pady=10, font="Arial 10 italic")
footer_label.pack(side="bottom", fill="x")

root.mainloop()
