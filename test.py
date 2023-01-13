from __future__ import unicode_literals
from colorama import init
from pathlib import Path
import numpy as np
import youtube_dl
import os

init()
list = []

Path('songs').mkdir(exist_ok=True)
Path('songs.txt').touch(exist_ok=True)
songsfile = np.loadtxt("songs.txt",dtype="str")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'songs/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

class crs:
    b  = '\033[94m'
    a  = '\033[96m'
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'
    e = '\033[0m'

os.system('cls')

print(f'{crs.b}Do you want to download the audio files with the links on songs.txt or do you want to insert them now?', f'\n{crs.a}Choose: \n [1]: Input now \n [2]: Songs.txt{crs.y}')

dtype = int(input())

if dtype == 1:
    while True:
        os.system('cls')
        
        print(f'{crs.b}Type a link or type {crs.y}"no"')
        respond = input()
        
        if respond == str('no'.lower()):
            break
        else:
            list.append(respond)

if dtype == 2:
    songsfile = list

os.system('cls')
print(f"{crs.y}DOWNLOAD STARTED{crs.e}")

ydl = youtube_dl.YoutubeDL(ydl_opts)
try:
    ydl.download(list)
    print(f"{crs.g}FINISHED DOWNLOADING{crs.e}")

except  youtube_dl.utils.DownloadError:
    print(f"{crs.r}DOWNLOADING ERROR\nReport it on my github, please!\n(Https://www.github.com/Filo35/YouTube-Downloader/){crs.e}")
    exit()