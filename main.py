from pytube import YouTube
from art import *
from Color_Console import ctext
import datetime


# Functions
def timeFormmat(yt):
    return datetime.timedelta(seconds=yt)


def getAuthor(yt):
    return yt.author


def getTitle(yt):
    return yt.title


def getAvailableResolution(yt):
    listOfRes = []
    for res in yt.streams.filter(file_extension="mp4", only_video=True):
        listOfRes.append(res.resolution)
    return listOfRes


def getStreams(yt):
    return yt.streams.filter(file_extension="mp4", only_video=True)


def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 2)
    print(
        f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


# Title--
myTitle = text2art("Elharery\nVideo Downloader")

ctext(myTitle, "red", "black")
ctext("=" * 70, "blue", "black")
ctext("Made By Amr -Elharery | https://amr-elharery.github.io/Elharery-Page/", "white", "red")
ctext("=" * 70, "blue", "black")

# Input URL
while True:
    try:
        url = input("Enter Video url: ").strip()
        youTube = YouTube(url, on_progress)
        break

    except:
        ctext("Not Found url!", "red", "black")

# Show Video Data

ctext(f"Video Name: {getTitle(youTube)}", "green")
ctext("=" * 70, "blue", "black")
ctext(f"Author Of Video: {getAuthor(youTube)}", "green")
ctext("=" * 70, "blue", "black")
ctext(f"Duration Of Video: {timeFormmat(youTube.length)}", "green")
ctext("=" * 70, "blue", "black")

# show qulaities
resolutions = getAvailableResolution(youTube)
print("Available Resolution: ", end='')
ctext(" | ".join(resolutions), "green")

# Take Resolution From User
while True:
    try:
        res = input("Enter Video Resolution [ex: 720p]: ").lower().strip()
        if res not in resolutions:
            raise ValueError("Not Valid")
        else:
            break
    except:
        ctext("Please Choose Quality From List Above ⬆", "red")

# Choose A Quality
for video in getStreams(youTube):
    if video.resolution == res:
        chosenVideo = video

ctext("=" * 70, "blue", "black")

# Show Video Size
print("Video Size: ", end='')
ctext(f"{chosenVideo.filesize_mb} MB", "green")

ctext("=" * 70, "blue", "black")

# Check If Want To Download
down = input("Are you sure to download? 'Y / N' ").upper()
if down == 'Y':
    try:
        chosenVideo.download()
        ctext("Downloaded successfully😃", "green")
        ctext("Thanks use Downloader❤", "white", "blue")
    except:
        ctext("Some thing occured while downloading, please try again.", "red")

else:
    ctext("Thanks use Downloader❤", "white", "blue")


# Pasue Console
input()
